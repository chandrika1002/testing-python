from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Student REST API")

# Student Model
class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str

# Temporary Database (List)
students = [
    {"id": 1, "name": "Imran", "age": 25, "course": "Python"},
    {"id": 2, "name": "Rahul", "age": 24, "course": "Java"},
    {"id": 3, "name": "John", "age": 23, "course": "DevOps"}
]

# Home API
@app.get("/")
def home():
    return {"message": "Welcome to Student REST API"}

# Get All Students
@app.get("/students")
def get_students():
    return students

# Get Student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    return {"message": "Student not found"}

# Add Student
@app.post("/students")
def add_student(student: Student):
    students.append(student.dict())
    return {
        "message": "Student Added Successfully",
        "student": student
    }

# Update Student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            students[index] = updated_student.dict()
            return {
                "message": "Student Updated Successfully",
                "student": updated_student
            }
    return {"message": "Student not found"}

# Delete Student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {"message": "Student Deleted Successfully"}
    return {"message": "Student not found"}
#
