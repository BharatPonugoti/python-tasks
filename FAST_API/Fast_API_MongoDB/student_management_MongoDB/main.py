# ============================================================
# 📝 FastAPI TODO CRUD App with MongoDB Atlas
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from urllib.parse import quote_plus

# ============================================================
# 🚀 FastAPI App
# ============================================================

app = FastAPI()

# ============================================================
# 🍃 MongoDB Atlas Configuration
# ============================================================

password = quote_plus("Sbi@2001")

MONGO_URL = f"mongodb+srv://pbharat6078_db_user:{password}@cluster0.pkxjyhk.mongodb.net/todo_db?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URL)

# Database
db = client["todo_db"]

# Collection
todo_collection = db["todos"]

# ============================================================
# 🧾 Pydantic Schemas
# ============================================================

class TodoCreate(BaseModel):
    title: str
    completed: bool = False


class TodoUpdate(BaseModel):
    title: str
    completed: bool


# ============================================================
# 🔄 Convert MongoDB ObjectId to String
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
        "message": "FastAPI TODO App with MongoDB Atlas 🚀"
    }

# ============================================================
# ✅ CREATE TODO
# ============================================================

@app.post("/todos")
def create_todo(todo: TodoCreate):

    new_todo = {
        "title": todo.title,
        "completed": todo.completed
    }

    result = todo_collection.insert_one(new_todo)

    created_todo = todo_collection.find_one(
        {"_id": result.inserted_id}
    )

    return todo_serializer(created_todo)

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
# ✅ GET SINGLE TODO
# ============================================================

@app.get("/todos/{todo_id}")
def get_todo(todo_id: str):

    todo = todo_collection.find_one(
        {"_id": ObjectId(todo_id)}
    )

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return todo_serializer(todo)

# ============================================================
# ✅ UPDATE TODO
# ============================================================

@app.put("/todos/{todo_id}")
def update_todo(todo_id: str, updated_todo: TodoUpdate):

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

    return todo_serializer(updated)

# ============================================================
# ✅ DELETE TODO
# ============================================================

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: str):

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

# ============================================================
# ▶️ HOW TO RUN
# ============================================================

# Install packages:
# pip install fastapi uvicorn pymongo dnspython

# Run:
# python -m uvicorn main:app --reload

# Swagger UI:
# http://127.0.0.1:8000/docs