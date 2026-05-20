# ============================================================
# 📝 FastAPI TODO CRUD App with SQLite
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

# ============================================================
# 🚀 Create FastAPI App
# ============================================================

app = FastAPI()

# ============================================================
# 🗄️ SQLite Database Connection
# ============================================================

conn = sqlite3.connect("todo.db", check_same_thread=False)
cursor = conn.cursor()

# ============================================================
# 📋 Create Table
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT 0
)
""")

conn.commit()

# ============================================================
# 🧾 Pydantic Model
# ============================================================

class Todo(BaseModel):
    title: str
    completed: bool = False

# ============================================================
# 🏠 Home Route
# ============================================================

@app.get("/")
def home():
    return {
        "message": "FastAPI SQLite CRUD App 🚀"
    }

# ============================================================
# ✅ CREATE TODO
# ============================================================

@app.post("/todos")
def create_todo(todo: Todo):

    cursor.execute(
        "INSERT INTO todos (title, completed) VALUES (?, ?)",
        (todo.title, todo.completed)
    )

    conn.commit()

    todo_id = cursor.lastrowid

    return {
        "message": "Todo created successfully",
        "todo": {
            "id": todo_id,
            "title": todo.title,
            "completed": todo.completed
        }
    }

# ============================================================
# ✅ GET ALL TODOS
# ============================================================

@app.get("/todos")
def get_all_todos():

    cursor.execute("SELECT * FROM todos")

    todos = cursor.fetchall()

    todo_list = []

    for todo in todos:
        todo_list.append({
            "id": todo[0],
            "title": todo[1],
            "completed": bool(todo[2])
        })

    return todo_list

# ============================================================
# ✅ GET TODO BY ID
# ============================================================

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):

    cursor.execute(
        "SELECT * FROM todos WHERE id=?",
        (todo_id,)
    )

    todo = cursor.fetchone()

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return {
        "id": todo[0],
        "title": todo[1],
        "completed": bool(todo[2])
    }

# ============================================================
# ✅ UPDATE TODO
# ============================================================

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):

    cursor.execute(
        "SELECT * FROM todos WHERE id=?",
        (todo_id,)
    )

    todo = cursor.fetchone()

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    cursor.execute(
        """
        UPDATE todos
        SET title=?, completed=?
        WHERE id=?
        """,
        (
            updated_todo.title,
            updated_todo.completed,
            todo_id
        )
    )

    conn.commit()

    return {
        "message": "Todo updated successfully",
        "todo": {
            "id": todo_id,
            "title": updated_todo.title,
            "completed": updated_todo.completed
        }
    }

# ============================================================
# ✅ DELETE TODO
# ============================================================

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):

    cursor.execute(
        "SELECT * FROM todos WHERE id=?",
        (todo_id,)
    )

    todo = cursor.fetchone()

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    cursor.execute(
        "DELETE FROM todos WHERE id=?",
        (todo_id,)
    )

    conn.commit()

    return {
        "message": "Todo deleted successfully"
    }

# ============================================================
# ▶️ HOW TO RUN
# ============================================================

# 1️⃣ Install Packages
# pip install fastapi uvicorn

# 2️⃣ Save file as:
# main.py

# 3️⃣ Run FastAPI Server
# python -m uvicorn main:app --reload

# 4️⃣ Open Swagger UI
# http://127.0.0.1:8000/docs