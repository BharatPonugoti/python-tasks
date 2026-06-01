import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

question = input("Ask Question : ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
You are a Python Trainer.

Answer only Python related questions.

Question:
{question}
"""
)

print(response.text)