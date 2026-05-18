# ============================================================
# 📝 FastAPI TODO App (CRUD) - MySQL Full Program
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from urllib.parse import quote_plus

# ============================================================
# 🚀 FastAPI App
# ============================================================

app = FastAPI()

# ============================================================
# 🗄️ MySQL Database Configuration
# ============================================================

USERNAME = "root"
PASSWORD = quote_plus("Sbi@2001")
HOST = "localhost"
PORT = "3306"
DATABASE = "todo_db"

DATABASE_URL = (
    f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

# ============================================================
# ⚙️ SQLAlchemy Engine
# ============================================================

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# ============================================================
# 🧱 Database Model
# ============================================================

class TodoDB(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    completed = Column(Boolean, default=False)

# ============================================================
# 🏗️ Create Table
# ============================================================

Base.metadata.create_all(bind=engine)

# ============================================================
# 🧾 Pydantic Schemas
# ============================================================

class TodoCreate(BaseModel):
    title: str
    completed: bool = False


class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool

    class Config:
        from_attributes = True

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
    return {"message": "FastAPI TODO App with MySQL 🚀"}

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
# ✅ READ ALL TODOS
# ============================================================

@app.get("/todos", response_model=list[TodoResponse])
def get_all_todos(db: Session = Depends(get_db)):

    todos = db.query(TodoDB).all()

    return todos

# ============================================================
# ✅ READ SINGLE TODO
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
    updated: TodoCreate,
    db: Session = Depends(get_db)
):

    todo = db.query(TodoDB).filter(TodoDB.id == todo_id).first()

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    todo.title = updated.title
    todo.completed = updated.completed

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

    return {"message": "Todo deleted successfully"}

# ============================================================
# ▶️ Run Command
# ============================================================

# python -m uvicorn main:app --reload