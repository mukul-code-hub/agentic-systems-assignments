# python -m venv .venv
# .\.venv\Scripts\Activate.ps1
from langchain_openai import ChatOpenAI
import os

client = ChatOpenAI(
    model="gpt-5.2"
)

response = client.invoke("Explain SQL indexes to the beginner student in simple words")

print(response)

