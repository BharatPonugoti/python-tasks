import os
from fastapi import FastAPI
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI()

# Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Home Route
@app.get("/")
def home():
    return {"message": "Gemini AI API Running Successfully"}

# AI API Route
@app.get("/ask")
def ask_ai(question: str):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    return {
        "question": question,
        "answer": response.text
    }