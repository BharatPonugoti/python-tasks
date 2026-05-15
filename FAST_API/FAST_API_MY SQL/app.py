# ============================================================
# 📝 FastAPI Todo Management System App (CRUD) - SQLite
# Database: todos.db
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# ============================================================
# Create FastAPI App
# ============================================================

app = FastAPI()

# ============================================================
# Database Configuration (SQLite)
# ============================================================

DATABASE_URL = "sqlite:///./todos.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# ============================================================
# Database Model
# ============================================================

class Todo(Base):

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(200), nullable=False)

    description = Column(String(500))

    completed = Column(Boolean, default=False)

# ============================================================
# Create Tables
# ============================================================

Base.metadata.create_all(bind=engine)

# ============================================================
# Pydantic Models
# ============================================================

class TodoCreate(BaseModel):

    id: int

    title: str

    description: str


class TodoResponse(BaseModel):

    id: int

    title: str

    description: str

    completed: bool

    class Config:

        from_attributes = True

# ============================================================
# Database Dependency
# ============================================================

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()

# ============================================================
# Home Route
# ============================================================

@app.get("/")

def home():

    return {

        "message": "Welcome to Todo Management System API"

    }

# ============================================================
# Create Todo
# ============================================================

@app.post("/todos/")

def create_todo(

    todo: TodoCreate,

    db: Session = Depends(get_db)

):

    existing_todo = (

        db.query(Todo)

        .filter(Todo.id == todo.id)

        .first()

    )

    if existing_todo:

        raise HTTPException(

            status_code=400,

            detail="Todo with this ID already exists"

        )

    new_todo = Todo(

        id=todo.id,

        title=todo.title,

        description=todo.description,

        completed=False

    )

    db.add(new_todo)

    db.commit()

    db.refresh(new_todo)

    return {

        "message": "Todo created successfully",

        "todo": {

            "id": new_todo.id,

            "title": new_todo.title,

            "description": new_todo.description,

            "completed": new_todo.completed

        }

    }

# ============================================================
# Get All Todos
# ============================================================

@app.get("/todos/")

def get_all_todos(

    db: Session = Depends(get_db)

):

    todos = db.query(Todo).all()

    todo_list = []

    for todo in todos:

        todo_list.append({

            "id": todo.id,

            "title": todo.title,

            "description": todo.description,

            "completed": todo.completed

        })

    return {

        "count": len(todo_list),

        "todos": todo_list

    }

# ============================================================
# Get Todo By ID
# ============================================================

@app.get("/todos/{todo_id}")

def get_todo(

    todo_id: int,

    db: Session = Depends(get_db)

):

    todo = (

        db.query(Todo)

        .filter(Todo.id == todo_id)

        .first()

    )

    if not todo:

        raise HTTPException(

            status_code=404,

            detail="Todo not found"

        )

    return {

        "todo": {

            "id": todo.id,

            "title": todo.title,

            "description": todo.description,

            "completed": todo.completed

        }

    }

# ============================================================
# Update Todo
# ============================================================

@app.put("/todos/{todo_id}")

def update_todo(

    todo_id: int,

    updated_todo: TodoCreate,

    db: Session = Depends(get_db)

):

    todo = (

        db.query(Todo)

        .filter(Todo.id == todo_id)

        .first()

    )

    if not todo:

        raise HTTPException(

            status_code=404,

            detail="Todo not found"

        )

    todo.title = updated_todo.title

    todo.description = updated_todo.description

    db.commit()

    db.refresh(todo)

    return {

        "message": "Todo updated successfully",

        "todo": {

            "id": todo.id,

            "title": todo.title,

            "description": todo.description,

            "completed": todo.completed

        }

    }

# ============================================================
# Mark Todo Completed
# ============================================================

@app.put("/todos/{todo_id}/complete")

def complete_todo(

    todo_id: int,

    db: Session = Depends(get_db)

):

    todo = (

        db.query(Todo)

        .filter(Todo.id == todo_id)

        .first()

    )

    if not todo:

        raise HTTPException(

            status_code=404,

            detail="Todo not found"

        )

    todo.completed = True

    db.commit()

    db.refresh(todo)

    return {

        "message": "Todo marked as completed",

        "todo": {

            "id": todo.id,

            "title": todo.title,

            "description": todo.description,

            "completed": todo.completed

        }

    }

# ============================================================
# Delete Todo
# ============================================================

@app.delete("/todos/{todo_id}")

def delete_todo(

    todo_id: int,

    db: Session = Depends(get_db)

):

    todo = (

        db.query(Todo)

        .filter(Todo.id == todo_id)

        .first()

    )

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

