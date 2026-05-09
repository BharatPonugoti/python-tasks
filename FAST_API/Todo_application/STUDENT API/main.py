from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Student Model
class Student(BaseModel):
    name: str
    age: int
    course: str
    marks: int

# Temporary database
students = []

# 1 & 2. Add Student
@app.post("/students")
def add_student(student: Student):
    student_data = student.dict()
    student_data["id"] = len(students) + 1
    students.append(student_data)

    return {
        "message": "Student added successfully"
    }

# 3. Get All Students
@app.get("/students")
def get_students():
    return students

# 4. Get Student By ID
@app.get("/students/{id}")
def get_student(id: int):
    for student in students:
        if student["id"] == id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")

# 5. Update Student
@app.put("/students/{id}")
def update_student(id: int, updated_student: Student):
    for student in students:
        if student["id"] == id:
            student["name"] = updated_student.name
            student["age"] = updated_student.age
            student["course"] = updated_student.course
            student["marks"] = updated_student.marks

            return {
                "message": "Student updated successfully"
            }

    raise HTTPException(status_code=404, detail="Student not found")

# 6. Delete Student
@app.delete("/students/{id}")
def delete_student(id: int):
    for student in students:
        if student["id"] == id:
            students.remove(student)

            return {
                "message": "Student deleted successfully"
            }

    raise HTTPException(status_code=404, detail="Student not found")
