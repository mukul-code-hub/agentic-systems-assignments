#.venv\Scripts\Activate.ps1
import os
import requests

#OLLAMA_HOST = "http://localhost:11434"
API_PATH = "https://ollama.com/api/chat"
MODEL_NAME = "gpt-oss:120b"

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

apikey = os.getenv("OLLAMA_KEY")

if not apikey:
    raise ValueError("Api key not found")

header = {
    "Authorization" : f"Bearer {apikey}"
}

response = requests.post(
     API_PATH,
     headers=header,
     json=payload,
     timeout=60
)

output = response.json()
print(output["message"]["content"])

#print(os.getenv("OLLAMA_KEY"))