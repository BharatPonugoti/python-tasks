import os
from google import genai
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def generate(question: str):

    # Create Gemini client
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    # Gemini model
    model = "gemini-2.5-flash"

    # Stream response
    response = client.models.generate_content_stream(
        model=model,
        contents=question
    )

    # Print response
    for chunk in response:
        if chunk.text:
            print(chunk.text, end="")

if __name__ == "__main__":

    question = input("Enter your question: ")
    generate(question)