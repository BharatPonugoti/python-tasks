# ============================================================
# 🔐 FastAPI TODO App + JWT Authentication (Array Version)
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import List

# ============================================================
# 🚀 CREATE FASTAPI APP
# ============================================================

app = FastAPI()

# ============================================================
# 🔐 JWT CONFIGURATION
# ============================================================

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = timedelta(minutes=5)

# ============================================================
# 🧾 Pydantic Models
# ============================================================

class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False

# ------------------------------------------------------------

class Login(BaseModel):
    username: str
    password: str

# ============================================================
# 🗃️ TEMPORARY DATABASE
# ============================================================

todos: List[Todo] = []

# ============================================================
# 🔐 CREATE JWT TOKEN
# ============================================================

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + ACCESS_TOKEN_EXPIRE

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

# ============================================================
# 🔐 TOKEN VALIDATION
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
# 🏠 HOME API
# ============================================================

@app.get("/")
def home():

    return {
        "message": "FastAPI + JWT + Array CRUD 🚀"
    }

# ============================================================
# 🔐 LOGIN API
# ============================================================

@app.post("/login")
def login(user: Login):

    # 👇 UPDATED PASSWORD HERE
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
        "token_type": "bearer",
        "expires_in": "5 minutes"
    }

# ============================================================
# ✅ CREATE TODO
# ============================================================

@app.post("/todos")
def create_todo(
    todo: Todo,
    user: str = Depends(verify_token)
):

    for existing in todos:

        if existing.id == todo.id:

            raise HTTPException(
                status_code=400,
                detail="ID already exists"
            )

    todos.append(todo)

    return {
        "message": "Todo created",
        "data": todo
    }

# ============================================================
# ✅ READ ALL TODOS
# ============================================================

@app.get("/todos")
def get_all_todos(
    user: str = Depends(verify_token)
):

    return {
        "count": len(todos),
        "data": todos
    }

# ============================================================
# ✅ READ SINGLE TODO
# ============================================================

@app.get("/todos/{todo_id}")
def get_todo(
    todo_id: int,
    user: str = Depends(verify_token)
):

    for todo in todos:

        if todo.id == todo_id:

            return todo

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )

# ============================================================
# ✅ UPDATE TODO
# ============================================================

@app.put("/todos/{todo_id}")
def update_todo(
    todo_id: int,
    updated: Todo,
    user: str = Depends(verify_token)
):

    for index, todo in enumerate(todos):

        if todo.id == todo_id:

            todos[index] = updated

            return {
                "message": "Todo updated successfully",
                "data": updated
            }

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )

# ============================================================
# ✅ DELETE TODO
# ============================================================

@app.delete("/todos/{todo_id}")
def delete_todo(
    todo_id: int,
    user: str = Depends(verify_token)
):

    for index, todo in enumerate(todos):

        if todo.id == todo_id:

            deleted = todos.pop(index)

            return {
                "message": "Todo deleted successfully",
                "data": deleted
            }

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )