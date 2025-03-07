from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


class Students(BaseModel):
    name: str


students = {
    1: {"name": "Kaushal Shakya"},
    2: {"name": "Sujata Bajracharya"},
    3: {"name": "Bailey Rani"},
    4: {"name": "Puntu Maya"},
}


@app.get("/")
def home(req: Request):
    host = req.headers["host"]
    print("host", host)
    message: str = "Hello World"
    return {"message": message, "students": students}


@app.get("/{id}")
def return_name(req: Request):
    id = int(req.path_params["id"])
    if id not in students:
        return JSONResponse(
            status_code=400,
            content={"message": "Student not available"},
        )
    return {"message": f"The student {students[id]['name']} exists"}


@app.post("/")
def register_student(req: Request, student: Students):
    print({"student_keys": max(list(students.keys()))})
    new_id = max(list(students.keys())) + 1
    students[new_id] = {"name": student.name}
    return {
        "message": f"Student {student.name} has been registered successfully",
        "data": students,
    }


@app.patch("/{id}")
def update_student(req: Request, body: Students):
    id = int(req.path_params["id"])

    if id not in students:
        return JSONResponse(
            status_code=400, content={"message": "Student not available"}
        )

    students[id]["name"] = body.name
    return JSONResponse(
        status_code=200, content={"message": "Student name updated", "data": students}
    )


@app.delete("/{id}")
def delete_student(req: Request):
    id = int(req.path_params["id"])

    if id not in students:
        return JSONResponse(
            status_code=400, content={"message": "Student not available"}
        )

    del students[id]
    return JSONResponse(
        status_code=200,
        content={
            "message": f"Student with ID: {id} deleted succesfully",
            "data": students,
        },
    )
