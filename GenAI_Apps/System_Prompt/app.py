import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

system_prompt = """
You are an AI Assistant.

Rules:
1. Answer professionally.
2. Give examples.
3. Keep answers concise.
"""

question = input("Question: ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"{system_prompt}\n\n{question}"
)

print(response.text)