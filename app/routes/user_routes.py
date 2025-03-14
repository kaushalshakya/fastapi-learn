from fastapi import APIRouter, HTTPException
from app.database import db
from app.models.student import *

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/")
async def get_users():
    try:
        users = await db["users"].find().to_list()
        print("Inside get all users")
        return ResponseModel(users, "Users fetched successfully", 200)
    except Exception as e:
        print("error: ", e)
        return ErrorResponseModel(str(e), 500, e)


@router.post("/")
async def create_user(student: StudentSchema):
    try:
        if (
            not student.fullname
            or not student.email
            or not student.course_of_study
            or not student.gpa
            or not student.year
            or not student.password
        ):
            print("all data not provided")
            raise HTTPException(
                status_code=400, detail="All required data not provided"
            )

        payload = {
            "fullname": student.fullname,
            "email": student.email,
            "course_of_study": student.course_of_study,
            "gpa": student.gpa,
            "year": student.year,
        }

        result = await db["users"].insert_one(payload)

        new_user = {
            "_id": str(result.inserted_id),
            "fullname": student.fullname,
            "email": student.email,
            "course_of_study": student.course_of_study,
            "gpa": student.gpa,
            "year": student.year,
        }

        return ResponseModel(new_user, "User created successfully", 201)
    except HTTPException as error:
        return ErrorResponseModel(str(error.detail), error.status_code, error)
    except Exception as e:
        print(e)
        return ErrorResponseModel(str(e), 500, e)


@router.patch("/{id}")
def updateUser(id: str, body: UpdateStudentModel):
    try:
        pass
    except HTTPException as error:
        return ErrorResponseModel(str(error.detail), error.status_code, error)
