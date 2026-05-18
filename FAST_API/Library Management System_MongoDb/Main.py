# ============================================================
# 📝 FastAPI TODO CRUD App with MongoDB
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId

# ============================================================
# 🚀 Create FastAPI App
# ============================================================

app = FastAPI()

# ============================================================
# 🍃 MongoDB Connection
# ============================================================

client = MongoClient("mongodb://localhost:27017")

# Database
db = client["todo_db"]

# Collection
todo_collection = db["todos"]

# ============================================================
# 🧾 Pydantic Model
# ============================================================

class Todo(BaseModel):
    title: str
    completed: bool = False

# ============================================================
# 🔄 MongoDB Serializer
# ============================================================

def todo_serializer(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "completed": todo["completed"]
    }

# ============================================================
# 🏠 Home Route
# ============================================================

@app.get("/")
def home():
    return {
        "message": "FastAPI MongoDB CRUD App 🚀"
    }

# ============================================================
# ✅ CREATE TODO
# ============================================================

@app.post("/todos")
def create_todo(todo: Todo):

    new_todo = {
        "title": todo.title,
        "completed": todo.completed
    }

    result = todo_collection.insert_one(new_todo)

    created_todo = todo_collection.find_one(
        {"_id": result.inserted_id}
    )

    return {
        "message": "Todo created successfully",
        "todo": todo_serializer(created_todo)
    }

# ============================================================
# ✅ GET ALL TODOS
# ============================================================

@app.get("/todos")
def get_all_todos():

    todos = []

    for todo in todo_collection.find():
        todos.append(todo_serializer(todo))

    return todos

# ============================================================
# ✅ GET TODO BY ID
# ============================================================

@app.get("/todos/{todo_id}")
def get_todo(todo_id: str):

    try:
        todo = todo_collection.find_one(
            {"_id": ObjectId(todo_id)}
        )

        if not todo:
            raise HTTPException(
                status_code=404,
                detail="Todo not found"
            )

        return todo_serializer(todo)

    except:
        raise HTTPException(
            status_code=400,
            detail="Invalid Todo ID"
        )

# ============================================================
# ✅ UPDATE TODO
# ============================================================

@app.put("/todos/{todo_id}")
def update_todo(todo_id: str, updated_todo: Todo):

    try:
        todo = todo_collection.find_one(
            {"_id": ObjectId(todo_id)}
        )

        if not todo:
            raise HTTPException(
                status_code=404,
                detail="Todo not found"
            )

        todo_collection.update_one(
            {"_id": ObjectId(todo_id)},
            {
                "$set": {
                    "title": updated_todo.title,
                    "completed": updated_todo.completed
                }
            }
        )

        updated = todo_collection.find_one(
            {"_id": ObjectId(todo_id)}
        )

        return {
            "message": "Todo updated successfully",
            "todo": todo_serializer(updated)
        }

    except:
        raise HTTPException(
            status_code=400,
            detail="Invalid Todo ID"
        )

# ============================================================
# ✅ DELETE TODO
# ============================================================

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: str):

    try:
        todo = todo_collection.find_one(
            {"_id": ObjectId(todo_id)}
        )

        if not todo:
            raise HTTPException(
                status_code=404,
                detail="Todo not found"
            )

        todo_collection.delete_one(
            {"_id": ObjectId(todo_id)}
        )

        return {
            "message": "Todo deleted successfully"
        }

    except:
        raise HTTPException(
            status_code=400,
            detail="Invalid Todo ID"
        )

# ============================================================
# ▶️ HOW TO RUN
# ============================================================

# 1️⃣ Install Packages
# pip install fastapi uvicorn pymongo

# 2️⃣ Start MongoDB Server
# mongod

# 3️⃣ Save file as:
# main.py

# 4️⃣ Run FastAPI Server
# python -m uvicorn main:app --reload

# 5️⃣ Open Swagger UI
# http://127.0.0.1:8000/docs