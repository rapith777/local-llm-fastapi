import json
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3.1"

class AskRequest(BaseModel):
    question: str

@app.get("/")
def root():
    return {"status": "ok", "docs": "http://127.0.0.1:8000/docs"}

def ask_llm_json(question: str) -> dict:
    system_msg = (
        "You are a JSON-only assistant. "
        "You MUST return valid JSON only. "
        "No markdown, no extra text."
    )

    user_msg = f"""
Answer the question using EXACTLY this JSON format:

{{
  "answer": "",
  "key_points": [],
  "confidence": "low|medium|high"
}}

Question: {question}
"""

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg},
        ],
        "stream": False,
        "options": {"num_predict": 180},
    }

    resp = requests.post(OLLAMA_URL, json=payload)
    resp.raise_for_status()
    data = resp.json()

    reply_text = data["message"]["content"]

    try:
        return json.loads(reply_text)
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=422,
            detail={"error": "Model returned invalid JSON", "raw": reply_text},
        )

@app.post("/ask")
def ask(req: AskRequest):
    return ask_llm_json(req.question)
