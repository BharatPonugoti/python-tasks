import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

allowed_topics = [
    "python",
    "fastapi",
    "flask",
    "streamlit",
    "ai",
    "machine learning"
]

question = input("Enter Question: ")

if any(topic in question.lower() for topic in allowed_topics):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    print(response.text)

else:
    print("Only AI and Python related questions are allowed.")