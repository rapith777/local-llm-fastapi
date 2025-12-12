import json
import requests

def ask_llm_json(system_message: str, user_message: str) -> dict | None:
    url = "http://localhost:11434/api/chat"

    payload = {
        "model": "llama3.1",
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ],
        "stream": False,
        "options": {"num_predict": 180}
    }

    resp = requests.post(url, json=payload)
    resp.raise_for_status()
    data = resp.json()

    reply_text = data["message"]["content"]

    try:
        return json.loads(reply_text)
    except json.JSONDecodeError:
        print("Model did NOT return valid JSON:")
        print(reply_text)
        return None

if __name__ == "__main__":
    system_msg = (
        "You are a JSON-only assistant. Return valid JSON only. "
        "No markdown, no extra text."
    )

    user_msg = """
Explain what a programming loop is.
Use EXACTLY this JSON format:

{
  "definition": "",
  "simple_example": "",
  "difficulty": "easy"
}
"""

    result = ask_llm_json(system_msg, user_msg)
    print("Parsed JSON:", result)
