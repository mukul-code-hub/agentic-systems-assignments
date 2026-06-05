#  python -m venv .venv
# .venv\Scripts\Activate.ps1
# pip install requests
import requests

#OLLAMA_HOST = "http://localhost:11434"
API_PATH = "http://localhost:11434/api/chat"
MODEL_NAME = "qwen3.5:0.8b"

prompt = "Explain rest api in beginner friendly way."

#request body
payload = {
    "model" : MODEL_NAME,
    "messages": [
        {
            "role": "user",
            "content" : prompt
        }
    ],
    "stream" : False
}

response = requests.post(
    API_PATH,
    json=payload,
    timeout=5
)

data = response.json()

print(data["message"]["content"])

