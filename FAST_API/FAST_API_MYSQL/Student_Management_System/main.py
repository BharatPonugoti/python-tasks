# ============================================================
# 📝 FastAPI TODO CRUD App with MySQL
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# ============================================================
# 🚀 FastAPI App
# ============================================================

app = FastAPI()

# ============================================================
# 🗄️ MySQL Database Configuration
# ============================================================

# Password = Sbi@2001
# '@' becomes '%40'

DATABASE_URL = "mysql+pymysql://root:Sbi%402001@localhost/todo_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# ============================================================
# 🧱 Database Table
# ============================================================

class TodoDB(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    completed = Column(Boolean, default=False)

# Create table automatically
Base.metadata.create_all(bind=engine)

# ============================================================
# 🧾 Pydantic Schemas
# ============================================================

class TodoCreate(BaseModel):
    title: str
    completed: bool = False


class TodoUpdate(BaseModel):
    title: str
    completed: bool


class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool

    class Config:
        orm_mode = True

# ============================================================
# 🔌 Database Dependency
# ============================================================

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ============================================================
# 🏠 Home Route
# ============================================================

@app.get("/")
def home():
    return {
        "message": "FastAPI TODO App with MySQL 🚀"
    }

# ============================================================
# ✅ CREATE TODO
# ============================================================

@app.post("/todos", response_model=TodoResponse)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):

    new_todo = TodoDB(
        title=todo.title,
        completed=todo.completed
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo

# ============================================================
# ✅ GET ALL TODOS
# ============================================================

@app.get("/todos", response_model=list[TodoResponse])
def get_all_todos(db: Session = Depends(get_db)):

    todos = db.query(TodoDB).all()

    return todos

# ============================================================
# ✅ GET SINGLE TODO
# ============================================================

@app.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):

    todo = db.query(TodoDB).filter(TodoDB.id == todo_id).first()

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return todo

# ============================================================
# ✅ UPDATE TODO
# ============================================================

@app.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: int,
    updated_todo: TodoUpdate,
    db: Session = Depends(get_db)
):

    todo = db.query(TodoDB).filter(TodoDB.id == todo_id).first()

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    todo.title = updated_todo.title
    todo.completed = updated_todo.completed

    db.commit()
    db.refresh(todo)

    return todo

# ============================================================
# ✅ DELETE TODO
# ============================================================

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):

    todo = db.query(TodoDB).filter(TodoDB.id == todo_id).first()

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    db.delete(todo)
    db.commit()

    return {
        "message": "Todo deleted successfully"
    }

# ============================================================
# ▶️ HOW TO RUN
# ============================================================

# 1️⃣ Install packages:
# pip install fastapi uvicorn sqlalchemy pymysql

# 2️⃣ Create database in MySQL:
# CREATE DATABASE todo_db;

# 3️⃣ Save this file as:
# main.py

# 4️⃣ Run server:
# uvicorn main:app --reload

# 5️⃣ Open Swagger UI:
# http://127.0.0.1:8000/docs