# ============================================================
# 📚 Library Management System using FastAPI + MySQL
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from urllib.parse import quote_plus

# ============================================================
# 🚀 Create FastAPI App
# ============================================================

app = FastAPI()

# ============================================================
# 🗄️ MySQL Database Configuration
# ============================================================

MYSQL_USER = "root"
MYSQL_PASSWORD = quote_plus("Sbi@2001")
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DATABASE = "library_db"

DATABASE_URL = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}"
    f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# ============================================================
# 📚 Database Model
# ============================================================

class BookDB(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    author = Column(String(200), nullable=False)
    published_year = Column(Integer)
    is_issued = Column(Boolean, default=False)

# Create Table
Base.metadata.create_all(bind=engine)

# ============================================================
# 📦 Pydantic Schema
# ============================================================

class Book(BaseModel):
    title: str
    author: str
    published_year: int

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
# ➕ Add Book
# ============================================================

@app.post("/books")
def add_book(book: Book, db: Session = Depends(get_db)):

    new_book = BookDB(
        title=book.title,
        author=book.author,
        published_year=book.published_year
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return {
        "message": "Book added successfully",
        "book": new_book
    }

# ============================================================
# 📖 Get All Books
# ============================================================

@app.get("/books")
def get_books(db: Session = Depends(get_db)):

    books = db.query(BookDB).all()

    return books

# ============================================================
# 🔍 Get Book By ID
# ============================================================

@app.get("/books/{id}")
def get_book(id: int, db: Session = Depends(get_db)):

    book = db.query(BookDB).filter(BookDB.id == id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book

# ============================================================
# ✏️ Update Book
# ============================================================

@app.put("/books/{id}")
def update_book(id: int, updated_book: Book, db: Session = Depends(get_db)):

    book = db.query(BookDB).filter(BookDB.id == id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    book.title = updated_book.title
    book.author = updated_book.author
    book.published_year = updated_book.published_year

    db.commit()
    db.refresh(book)

    return {
        "message": "Book updated successfully",
        "book": book
    }

# ============================================================
# ❌ Delete Book
# ============================================================

@app.delete("/books/{id}")
def delete_book(id: int, db: Session = Depends(get_db)):

    book = db.query(BookDB).filter(BookDB.id == id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()

    return {
        "message": "Book deleted successfully"
    }

# ============================================================
# 📕 Issue Book
# ============================================================

@app.post("/issue-book/{id}")
def issue_book(id: int, db: Session = Depends(get_db)):

    book = db.query(BookDB).filter(BookDB.id == id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if book.is_issued:
        raise HTTPException(status_code=400, detail="Book already issued")

    book.is_issued = True

    db.commit()
    db.refresh(book)

    return {
        "message": "Book issued successfully"
    }

# ============================================================
# 📗 Return Book
# ============================================================

@app.post("/return-book/{id}")
def return_book(id: int, db: Session = Depends(get_db)):

    book = db.query(BookDB).filter(BookDB.id == id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if not book.is_issued:
        raise HTTPException(status_code=400, detail="Book is not issued")

    book.is_issued = False

    db.commit()
    db.refresh(book)

    return {
        "message": "Book returned successfully"
    }

# ============================================================
# ✅ Available Books
# ============================================================

@app.get("/available-books")
def available_books(db: Session = Depends(get_db)):

    books = db.query(BookDB).filter(BookDB.is_issued == False).all()

    return books

# ============================================================
# 📚 Issued Books
# ============================================================

@app.get("/issued-books")
def issued_books(db: Session = Depends(get_db)):

    books = db.query(BookDB).filter(BookDB.is_issued == True).all()

    return books

# ============================================================
# 🔎 Search Book
# ============================================================

@app.get("/search-book/{title}")
def search_book(title: str, db: Session = Depends(get_db)):

    books = db.query(BookDB).filter(
        BookDB.title.ilike(f"%{title}%")
    ).all()

    if not books:
        raise HTTPException(status_code=404, detail="No books found")

    return books

# ============================================================
# ▶️ Run Server
# ============================================================

# uvicorn main:app --reload