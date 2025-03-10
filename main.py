from fastapi import FastAPI, Request
import json

# routes
from app.routes.user_routes import router as user_router

app = FastAPI()


@app.get("/")
def home(req: Request):
    headers = dict(req.headers)
    print(json.dumps(headers, indent=3))
    message: str = "Hello World"
    return {"message": message}


app.include_router(user_router)
