# icoer_extractor_v52.py
from sentence_transformers import SentenceTransformer, util
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import spacy
import numpy as np
import re

# Load models
models = {
    "light": SentenceTransformer("all-MiniLM-L6-v2"),
    "multi": SentenceTransformer("sentence-transformers/LaBSE")
}
analyzer = SentimentIntensityAnalyzer()
nlp = spacy.load("en_core_web_sm")

# Cache
_context_cache = {}

def encode(text, model_type="light"):
    try:
        return models[model_type].encode(text, convert_to_tensor=True)
    except Exception as e:
        print(f"Encoding error: {e}")
        return None

def extract_semantic_similarity(text, context="The universe is coherent and structured.", model_type="light"):
    if not text.strip():
        return 0.0
    if (context, model_type) not in _context_cache:
        _context_cache[(context, model_type)] = encode(context, model_type)
    emb1 = encode(text, model_type)
    emb2 = _context_cache.get((context, model_type))
    if emb1 is None or emb2 is None:
        return 0.0
    return float(util.pytorch_cos_sim(emb1, emb2)[0])

def extract_lexical_score(text):
    words = text.split()
    if not words:
        return 0.0
    unique_words = set(words)
    diversity = len(unique_words) / len(words)
    avg_length = np.mean([len(w) for w in words])
    score = 0.5 * diversity + 0.5 * (1 - abs(avg_length - 5) / 5)
    return min(max(score, 0), 1)

def extract_structural_integrity(text):
    clauses = re.split(r'[.,;!?]', text)
    lengths = [len(clause.split()) for clause in clauses if clause.strip()]
    if not lengths:
        return 0.0
    variance = np.var(lengths)
    score = 1 / (1 + variance)
    return min(score, 1.0)

def extract_logical_coherence(text):
    try:
        doc = nlp(text)
        concepts = [(ent.text, token.lemma_) for ent in doc.ents for token in ent.root.subtree]
        score = len(concepts) / max(len(doc), 1)
        return min(score, 1.0)
    except Exception:
        return 0.0

def extract_memory_score(text, memory=[]):
    overlaps = sum(1 for item in memory if item in text)
    return min(overlaps / len(memory), 1.0) if memory else 0.0

def extract_affective_tone(text):
    try:
        vs = analyzer.polarity_scores(text)
        tone_score = abs(vs['compound'])
        return min(tone_score, 1.0)
    except Exception:
        return 0.0

def extract_all(text, memory_context=[], model_type="light"):
    return {
        "S": round(extract_semantic_similarity(text, model_type=model_type), 3),
        "L": round(extract_lexical_score(text), 3),
        "E": round(extract_structural_integrity(text), 3),
        "C": round(extract_logical_coherence(text), 3),
        "M": round(extract_memory_score(text, memory_context), 3),
        "A": round(extract_affective_tone(text), 3)
    }
