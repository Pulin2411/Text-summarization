from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

GEMINI_API_KEY = "AIzaSyBdeglrdIwYD_9D2WvTOz_bFsocGwJlOKE"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

class SummarizationRequest(BaseModel):
    text: str
    summary_length: str = "short"  # optional: "short", "medium", "detailed"

@app.post("/summarize")
def summarize_text(request: SummarizationRequest):
    headers = {
        "Content-Type": "application/json"
    }
    params = {
        "key": GEMINI_API_KEY
    }
    # Prompt to instruct summarization
    prompt = (
        f"Summarize the following text in a {request.summary_length} and clear way:\n\n"
        f"{request.text}"
    )
    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    response = requests.post(GEMINI_API_URL, headers=headers, params=params, json=payload)

    if response.status_code != 200:
        return {"error": response.text}

    data = response.json()
    summarized_text = (
        data.get("candidates", [{}])[0]
        .get("content", {})
        .get("parts", [{}])[0]
        .get("text", "")
    )

    return {"summarized_text": summarized_text}
