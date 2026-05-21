# ============================================================
# 📚 FASTAPI LIBRARY MANAGEMENT SYSTEM WITH MYSQL
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# ============================================================
# 🚀 CREATE FASTAPI APP
# ============================================================

app = FastAPI()

# ============================================================
# 🛢️ MYSQL DATABASE CONNECTION
# ============================================================

DATABASE_URL = "mysql+pymysql://root:Sbi%402001@localhost/library_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# ============================================================
# 📚 TABLE 1 : TOTAL BOOKS LIST IN LIBRARY
# ============================================================

class LibraryBooksTable(Base):

    __tablename__ = "library_books"

    sl_no = Column(Integer, primary_key=True, index=True)
    book_name = Column(String(100))
    edition = Column(String(50))
    author = Column(String(100))

# ============================================================
# 👨‍🎓 TABLE 2 : LIBRARY CLIENTS INFORMATION
# ============================================================

class ClientsTable(Base):

    __tablename__ = "clients"

    sl_no = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(50))
    contact_no = Column(String(20))
    premium_due_date = Column(String(50))

# ============================================================
# 📕 TABLE 3 : ISSUED BOOKS INFORMATION
# ============================================================

class IssuedBooksTable(Base):

    __tablename__ = "issued_books"

    sl_no = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(50))
    book_name = Column(String(100))
    edition = Column(String(50))
    author = Column(String(100))
    handing_over_date = Column(String(50))
    renewal_date = Column(String(50))
    due_date = Column(String(50))

# ============================================================
# 🏗️ CREATE ALL TABLES
# ============================================================

Base.metadata.create_all(bind=engine)

# ============================================================
# 📘 PYDANTIC MODELS
# ============================================================

# ---------------------------
# BOOKS MODEL
# ---------------------------

class LibraryBook(BaseModel):

    sl_no: int
    book_name: str
    edition: str
    author: str

# ---------------------------
# CLIENT MODEL
# ---------------------------

class Client(BaseModel):

    sl_no: int
    user_id: str
    contact_no: str
    premium_due_date: str

# ---------------------------
# ISSUED BOOK MODEL
# ---------------------------

class IssuedBook(BaseModel):

    sl_no: int
    user_id: str
    book_name: str
    edition: str
    author: str
    handing_over_date: str
    renewal_date: str
    due_date: str

# ============================================================
# 📚 LIBRARY BOOKS CRUD
# ============================================================

# ➕ ADD BOOK

@app.post("/library_books")
def add_library_book(book: LibraryBook):

    db = SessionLocal()

    new_book = LibraryBooksTable(
        sl_no=book.sl_no,
        book_name=book.book_name,
        edition=book.edition,
        author=book.author
    )

    db.add(new_book)
    db.commit()

    return {
        "message": "Library Book Added Successfully"
    }

# 📖 GET ALL BOOKS

@app.get("/library_books")
def get_library_books():

    db = SessionLocal()

    books = db.query(LibraryBooksTable).all()

    return {
        "total_books": len(books),
        "books": books
    }

# 🔍 GET SINGLE BOOK

@app.get("/library_books/{id}")
def get_library_book(id: int):

    db = SessionLocal()

    book = db.query(LibraryBooksTable).filter(
        LibraryBooksTable.sl_no == id
    ).first()

    if not book:

        raise HTTPException(
            status_code=404,
            detail="Book Not Found"
        )

    return book

# ✏️ UPDATE BOOK

@app.put("/library_books/{id}")
def update_library_book(id: int, updated_book: LibraryBook):

    db = SessionLocal()

    book = db.query(LibraryBooksTable).filter(
        LibraryBooksTable.sl_no == id
    ).first()

    if not book:

        raise HTTPException(
            status_code=404,
            detail="Book Not Found"
        )

    book.book_name = updated_book.book_name
    book.edition = updated_book.edition
    book.author = updated_book.author

    db.commit()

    return {
        "message": "Library Book Updated Successfully"
    }

# ❌ DELETE BOOK

@app.delete("/library_books/{id}")
def delete_library_book(id: int):

    db = SessionLocal()

    book = db.query(LibraryBooksTable).filter(
        LibraryBooksTable.sl_no == id
    ).first()

    if not book:

        raise HTTPException(
            status_code=404,
            detail="Book Not Found"
        )

    db.delete(book)
    db.commit()

    return {
        "message": "Library Book Deleted Successfully"
    }

# ============================================================
# 👨‍🎓 CLIENTS CRUD
# ============================================================

# ➕ ADD CLIENT

@app.post("/clients")
def add_client(client: Client):

    db = SessionLocal()

    new_client = ClientsTable(
        sl_no=client.sl_no,
        user_id=client.user_id,
        contact_no=client.contact_no,
        premium_due_date=client.premium_due_date
    )

    db.add(new_client)
    db.commit()

    return {
        "message": "Client Added Successfully"
    }

# 📖 GET ALL CLIENTS

@app.get("/clients")
def get_clients():

    db = SessionLocal()

    clients = db.query(ClientsTable).all()

    return {
        "total_clients": len(clients),
        "clients": clients
    }

# 🔍 GET SINGLE CLIENT

@app.get("/clients/{id}")
def get_client(id: int):

    db = SessionLocal()

    client = db.query(ClientsTable).filter(
        ClientsTable.sl_no == id
    ).first()

    if not client:

        raise HTTPException(
            status_code=404,
            detail="Client Not Found"
        )

    return client

# ✏️ UPDATE CLIENT

@app.put("/clients/{id}")
def update_client(id: int, updated_client: Client):

    db = SessionLocal()

    client = db.query(ClientsTable).filter(
        ClientsTable.sl_no == id
    ).first()

    if not client:

        raise HTTPException(
            status_code=404,
            detail="Client Not Found"
        )

    client.user_id = updated_client.user_id
    client.contact_no = updated_client.contact_no
    client.premium_due_date = updated_client.premium_due_date

    db.commit()

    return {
        "message": "Client Updated Successfully"
    }

# ❌ DELETE CLIENT

@app.delete("/clients/{id}")
def delete_client(id: int):

    db = SessionLocal()

    client = db.query(ClientsTable).filter(
        ClientsTable.sl_no == id
    ).first()

    if not client:

        raise HTTPException(
            status_code=404,
            detail="Client Not Found"
        )

    db.delete(client)
    db.commit()

    return {
        "message": "Client Deleted Successfully"
    }

# ============================================================
# 📕 ISSUED BOOKS CRUD
# ============================================================

# ➕ ADD ISSUED BOOK

@app.post("/issued_books")
def add_issued_book(book: IssuedBook):

    db = SessionLocal()

    new_book = IssuedBooksTable(
        sl_no=book.sl_no,
        user_id=book.user_id,
        book_name=book.book_name,
        edition=book.edition,
        author=book.author,
        handing_over_date=book.handing_over_date,
        renewal_date=book.renewal_date,
        due_date=book.due_date
    )

    db.add(new_book)
    db.commit()

    return {
        "message": "Issued Book Added Successfully"
    }

# 📖 GET ALL ISSUED BOOKS

@app.get("/issued_books")
def get_issued_books():

    db = SessionLocal()

    books = db.query(IssuedBooksTable).all()

    return {
        "total_issued_books": len(books),
        "issued_books": books
    }

# 🔍 GET SINGLE ISSUED BOOK

@app.get("/issued_books/{id}")
def get_issued_book(id: int):

    db = SessionLocal()

    book = db.query(IssuedBooksTable).filter(
        IssuedBooksTable.sl_no == id
    ).first()

    if not book:

        raise HTTPException(
            status_code=404,
            detail="Issued Book Not Found"
        )

    return book

# ✏️ UPDATE ISSUED BOOK

@app.put("/issued_books/{id}")
def update_issued_book(id: int, updated_book: IssuedBook):

    db = SessionLocal()

    book = db.query(IssuedBooksTable).filter(
        IssuedBooksTable.sl_no == id
    ).first()

    if not book:

        raise HTTPException(
            status_code=404,
            detail="Issued Book Not Found"
        )

    book.user_id = updated_book.user_id
    book.book_name = updated_book.book_name
    book.edition = updated_book.edition
    book.author = updated_book.author
    book.handing_over_date = updated_book.handing_over_date
    book.renewal_date = updated_book.renewal_date
    book.due_date = updated_book.due_date

    db.commit()

    return {
        "message": "Issued Book Updated Successfully"
    }

# ❌ DELETE ISSUED BOOK

@app.delete("/issued_books/{id}")
def delete_issued_book(id: int):

    db = SessionLocal()

    book = db.query(IssuedBooksTable).filter(
        IssuedBooksTable.sl_no == id
    ).first()

    if not book:

        raise HTTPException(
            status_code=404,
            detail="Issued Book Not Found"
        )

    db.delete(book)
    db.commit()

    return {
        "message": "Issued Book Deleted Successfully"
    }