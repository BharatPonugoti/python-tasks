import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

st.title("Gemini AI Chatbot")

question = st.text_input("Ask a Question")

if st.button("Generate"):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    st.write(response.text)