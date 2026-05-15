# ============================================================

# 📝 FastAPI Student Management System App (CRUD) - MySQL

# ============================================================
 
from fastapi import FastAPI, HTTPException, Depends

from pydantic import BaseModel

from sqlalchemy import create_engine, Column, Integer, String, Boolean

from sqlalchemy.orm import declarative_base, sessionmaker, Session

from urllib.parse import quote_plus
 
# ============================================================

# Create FastAPI App

# ============================================================
 
app = FastAPI()
 
# ============================================================

# Database Configuration

# ============================================================
 
DB_USER = "root"
 
# Replace with your actual MySQL password

DB_PASSWORD = quote_plus("Sbi@2001")
 
DB_HOST = "127.0.0.1"

DB_PORT = "3306"

DB_NAME = "student_management"
 
DATABASE_URL = (

    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

)
 
engine = create_engine(

    DATABASE_URL,

    pool_pre_ping=True

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
 
class Student(Base):

    __tablename__ = "students"
 
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), index=True)

    age = Column(Integer)

    marks = Column(Integer)

    course = Column(String(100))

    is_active = Column(Boolean, default=True)
 
# ============================================================

# Create Tables

# ============================================================
 
Base.metadata.create_all(bind=engine)
 
# ============================================================

# Pydantic Models

# ============================================================
 
class StudentCreate(BaseModel):

    id: int

    name: str

    age: int

    marks: int

    course: str
 
 
class StudentResponse(BaseModel):

    id: int

    name: str

    age: int

    marks: int

    course: str

    is_active: bool
 
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

        "message": "Welcome to Student Management System API"

    }
 
# ============================================================

# Create Student

# ============================================================
 
@app.post("/students/")

def create_student(

    student: StudentCreate,

    db: Session = Depends(get_db)

):
 
    existing_student = (

        db.query(Student)

        .filter(Student.id == student.id)

        .first()

    )
 
    if existing_student:
 
        raise HTTPException(

            status_code=400,

            detail="Student with this ID already exists"

        )
 
    new_student = Student(

        id=student.id,

        name=student.name,

        age=student.age,

        marks=student.marks,

        course=student.course,

        is_active=True

    )
 
    db.add(new_student)

    db.commit()

    db.refresh(new_student)
 
    return {

        "message": "Student created successfully",

        "student": {

            "id": new_student.id,

            "name": new_student.name,

            "age": new_student.age,

            "marks": new_student.marks,

            "course": new_student.course,

            "is_active": new_student.is_active

        }

    }
 
# ============================================================

# Get All Students

# ============================================================
 
@app.get("/students/")

def get_all_students(

    db: Session = Depends(get_db)

):
 
    students = db.query(Student).all()
 
    student_list = []
 
    for student in students:
 
        student_list.append({

            "id": student.id,

            "name": student.name,

            "age": student.age,

            "marks": student.marks,

            "course": student.course,

            "is_active": student.is_active

        })
 
    return {

        "count": len(student_list),

        "students": student_list

    }
 
# ============================================================

# Get Student By ID

# ============================================================
 
@app.get("/students/{student_id}")

def get_student(

    student_id: int,

    db: Session = Depends(get_db)

):
 
    student = (

        db.query(Student)

        .filter(Student.id == student_id)

        .first()

    )
 
    if not student:
 
        raise HTTPException(

            status_code=404,

            detail="Student not found"

        )
 
    return {

        "student": {

            "id": student.id,

            "name": student.name,

            "age": student.age,

            "marks": student.marks,

            "course": student.course,

            "is_active": student.is_active

        }

    }
 
# ============================================================

# Update Student

# ============================================================
 
@app.put("/students/{student_id}")

def update_student(

    student_id: int,

    updated_student: StudentCreate,

    db: Session = Depends(get_db)

):
 
    student = (

        db.query(Student)

        .filter(Student.id == student_id)

        .first()

    )
 
    if not student:
 
        raise HTTPException(

            status_code=404,

            detail="Student not found"

        )
 
    student.name = updated_student.name

    student.age = updated_student.age

    student.marks = updated_student.marks

    student.course = updated_student.course
 
    db.commit()

    db.refresh(student)
 
    return {

        "message": "Student updated successfully",

        "student": {

            "id": student.id,

            "name": student.name,

            "age": student.age,

            "marks": student.marks,

            "course": student.course,

            "is_active": student.is_active

        }

    }
 
# ============================================================

# Delete Student

# ============================================================
 
@app.delete("/students/{student_id}")

def delete_student(

    student_id: int,

    db: Session = Depends(get_db)

):
 
    student = (

        db.query(Student)

        .filter(Student.id == student_id)

        .first()

    )
 
    if not student:
 
        raise HTTPException(

            status_code=404,

            detail="Student not found"

        )
 
    db.delete(student)

    db.commit()
 
    return {

        "message": "Student deleted successfully"

    }
 