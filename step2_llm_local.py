import requests

def ask_llm_local(system_message: str, user_message: str) -> str:
    url = "http://localhost:11434/api/chat"

    payload = {
        "model": "llama3.1",
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ],
        "stream": False,
        "options": {"num_predict": 120}
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()
    data = response.json()

    return data["message"]["content"]

if __name__ == "__main__":
    reply = ask_llm_local(
        "You are a Python tutor. Answer in max 2 short sentences. Stay on topic.",
        "Explain what a programming loop is in very simple words. No extra details."
    )
    print("LLM reply:", reply)
