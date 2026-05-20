# ============================================================
# 🔐 FastAPI TODO App + JWT Authentication + MySQL
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session

from urllib.parse import quote_plus

# ============================================================
# 🚀 FastAPI App
# ============================================================

app = FastAPI()

# ============================================================
# 🔐 JWT Configuration
# ============================================================

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

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
# ⚙️ SQLAlchemy Setup
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

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    completed = Column(Boolean, default=False)

# ============================================================
# 🏗️ Create Tables
# ============================================================

Base.metadata.create_all(bind=engine)

# ============================================================
# 🧾 Pydantic Schemas
# ============================================================

class Login(BaseModel):
    username: str
    password: str


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
# 🔐 Create JWT Token
# ============================================================

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

# ============================================================
# 🔐 Verify Token
# ============================================================

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# ------------------------------------------------------------

def verify_token(token: str = Depends(oauth2_scheme)):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return username

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Token expired or invalid"
        )

# ============================================================
# 🏠 Home Route
# ============================================================

@app.get("/")
def home():

    return {
        "message": "FastAPI TODO + JWT + MySQL 🚀"
    }

# ============================================================
# 🔐 Login API
# ============================================================

@app.post("/login")
def login(user: Login):

    # 👇 Static Username & Password
    if user.username != "admin" or user.password != "Sbi@2001":

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        data={"sub": user.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# ============================================================
# ✅ CREATE TODO
# ============================================================

@app.post("/todos", response_model=TodoResponse)
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

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
def get_all_todos(
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    todos = db.query(TodoDB).all()

    return todos

# ============================================================
# ✅ READ SINGLE TODO
# ============================================================

@app.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    todo = db.query(TodoDB).filter(
        TodoDB.id == todo_id
    ).first()

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
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    todo = db.query(TodoDB).filter(
        TodoDB.id == todo_id
    ).first()

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
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    todo = db.query(TodoDB).filter(
        TodoDB.id == todo_id
    ).first()

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
# ▶️ RUN COMMAND
# ============================================================

# python -m uvicorn TodoToken_MYSQL:app --reload