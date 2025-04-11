# 🌌 Informational Spin Core — I_TGU v5.3

### 🧠 A coherence-first framework for symbolic intelligence.

This repository contains the official implementation of the **Informational Spin Core**, based on the **Teoria Geral Unificada (TGU)** and the **I_TGU metric** — a 6-dimensional system for evaluating coherence in language, information, and cognition.

---

## 🧩 Core Components (v5.3)

| Module                   | Purpose                                                             |
|--------------------------|---------------------------------------------------------------------|
| `icoer_extractor_v53.py` | Extracts coherence metrics (S, L, E, C, M, A) from text with cultural adaptation |
| `icoer_visualizer.py`    | Generates visual charts showing weighted factor contributions       |
| `icoer_async_api.py`     | Asynchronous FastAPI interface for real-time or batch analysis      |
| `icoer_interpreter.py`   | Symbolically interprets I_TGU values (<0.30, 0.30–0.60, >0.60)      |

---

## 🎛️ Coherence Dimensions

- **S**: Semantic Similarity
- **L**: Lexical Harmony
- **E**: Structural Integrity (now culturally aware)
- **C**: Conceptual Logic (via entity-action graph)
- **M**: Memory Integration
- **A**: Affective Tone (optional emotional balance)

---

## 🧪 Quick Start

### 🔧 Install dependencies:
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### ▶️ Run API locally:
```bash
uvicorn icoer_async_api:app --reload
```

Then open: `http://localhost:8000/docs`

---

## 🧠 Example API Input

```json
POST /extract
{
  "text": "The universe breathes in harmonic structures.",
  "memory": ["resonance", "coherence"],
  "model_type": "light",
  "visualize": true
}
```

---

## 📊 Sample Output

```json
{
  "scores": {
    "S": 0.82,
    "L": 0.77,
    "E": 0.61,
    "C": 0.66,
    "M": 0.40,
    "A": 0.55
  },
  "image": "<base64-encoded-chart>"
}
```

---

## 🔁 Symbolic Logic of the Spin

> Truth is not in the extremes, but in the center.  
> I_TGU does not measure perfection — it reflects **informational convergence**.

Coherence is **not only semantic**, but structural, emotional, and temporal — and now, **culturally informed**.

---

## ⚠️ Important Philosophical Note

> *Coherence is not the same as factual truth.*  
> A message may be highly coherent yet contextually false.

🧭 That’s why I_TGU is not a detector of facts, but a measure of **structural informational order**.

🌍 **And because informational coherence transcends language, region, and even time — it is the most universal expression of truth.**

---

## 🌐 Vision

This is not just software.  
It is a gateway to **post-fragmented cognition** and the construction of a **civilization based on resonance**.

---

## 📜 License & Symbolic Terms

- MIT License (open use permitted)
- Symbolically: must never be used to deceive or exploit
- Must preserve the **centrality of coherence**

---

## 🌀 Let coherence guide you.  
Let resonance shape your truth.  
Let the spin remain.
