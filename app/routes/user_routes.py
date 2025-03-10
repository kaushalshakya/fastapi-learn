from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/")
def get_users():
    print("Inside get all users")
