from fastapi import APIRouter, HTTPException
from app.database import db

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/")
async def get_users():
    try:
        users = await db["users"].find().to_list()
        print("Inside get all users")
        return {"users": users}
    except Exception as e:
        print("error: ", e)
        raise HTTPException(status_code=500, detail=str(e))
