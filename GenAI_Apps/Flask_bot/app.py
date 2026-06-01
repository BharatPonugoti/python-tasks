from flask import Flask, render_template, request, redirect, session
from google import genai
from dotenv import load_dotenv
import sqlite3
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = "gemini_secret_key"

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# -------------------------------
# Database Initialization
# -------------------------------

def init_db():

    conn = sqlite3.connect("chatbot.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS chats(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        answer TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# -------------------------------
# Home Page
# -------------------------------

@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""

    if request.method == "POST":

        question = request.form["question"]

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=question
            )

            answer = response.text

            session["last_question"] = question

            conn = sqlite3.connect("chatbot.db")
            cur = conn.cursor()

            cur.execute(
                "INSERT INTO chats(question,answer) VALUES(?,?)",
                (question, answer)
            )

            conn.commit()
            conn.close()

        except Exception:

            answer = "⚠️ Gemini server is busy. Please try again."

    return render_template(
        "index.html",
        answer=answer
    )

# -------------------------------
# History
# -------------------------------

@app.route("/history")
def history():

    conn = sqlite3.connect("chatbot.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM chats ORDER BY id DESC"
    )

    chats = cur.fetchall()

    conn.close()

    return render_template(
        "history.html",
        chats=chats
    )

# -------------------------------
# Analytics
# -------------------------------

@app.route("/analytics")
def analytics():

    conn = sqlite3.connect("chatbot.db")
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM chats")

    total = cur.fetchone()[0]

    conn.close()

    return render_template(
        "analytics.html",
        total=total
    )

# -------------------------------
# New Chat
# -------------------------------

@app.route("/new_chat")
def new_chat():

    session.pop("last_question", None)

    return redirect("/")

# -------------------------------
# Retry
# -------------------------------

@app.route("/retry")
def retry():

    question = session.get("last_question")

    if not question:
        return redirect("/")

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question
        )

        answer = response.text

        conn = sqlite3.connect("chatbot.db")
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO chats(question,answer) VALUES(?,?)",
            (question, answer)
        )

        conn.commit()
        conn.close()

        return render_template(
            "index.html",
            answer=answer
        )

    except Exception:

        return render_template(
            "index.html",
            answer="⚠️ Retry failed."
        )

# -------------------------------
# About
# -------------------------------

@app.route("/about")
def about():

    return render_template("about.html")

# -------------------------------
# Settings
# -------------------------------

@app.route("/settings")
def settings():

    return render_template("settings.html")

if __name__ == "__main__":
    app.run(debug=True)