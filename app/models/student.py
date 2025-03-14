from pydantic import BaseModel, Field, EmailStr
from typing import Any, Optional, Dict, Union


class StudentSchema(BaseModel):
    fullname: str
    email: EmailStr
    course_of_study: str
    year: int = Field(..., gt=0, lt=4)
    gpa: float = Field(..., le=4.0)
    password: str

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Kaushal Shakya",
                "email": "kaushal.shakya@olivegroup.io",
                "year": 4,
                "gpa": "3.45",
            }
        }


class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources and environmental engineering",
                "year": 4,
                "gpa": "4.0",
            }
        }


def ResponseModel(
    data: Any, message: str, code: int
) -> Dict[str, Union[Any, str, int]]:
    return {"data": data, "message": message, "code": code}


def ErrorResponseModel(
    message: str, code: int, error: Optional[str] = None
) -> Dict[str, Union[str | None, str, int]]:
    return {"error": error, "message": message, "code": code}
