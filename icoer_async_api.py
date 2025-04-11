# icoer_async_api.py
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import matplotlib.pyplot as plt
import io
import base64
from icoer_extractor_v52 import extract_all
from icoer_visualizer import plot_icoer_factors

app = FastAPI()

class CoherenceRequest(BaseModel):
    text: str
    memory: list[str] = []
    model_type: str = "light"
    visualize: bool = False

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok", "version": "5.3"}

@app.post("/extract")
async def extract_coherence(data: CoherenceRequest):
    try:
        results = extract_all(data.text, memory_context=data.memory, model_type=data.model_type)

        if data.visualize:
            fig = plt.figure()
            plot_icoer_factors(results)
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            img_base64 = base64.b64encode(buf.read()).decode('utf-8')
            buf.close()
            return {"scores": results, "image": img_base64}
        else:
            return {"scores": results}

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run("icoer_async_api:app", host="0.0.0.0", port=8000, reload=True)
