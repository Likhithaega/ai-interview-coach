import requests
from app.core.config import settings

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def call_llm(prompt: str):
    headers = {
        "Authorization": f"Bearer {settings.GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(GROQ_URL, headers=headers, json=data)

    if response.status_code != 200:
        raise Exception(f"LLM Error: {response.text}")

    return response.json()["choices"][0]["message"]["content"]