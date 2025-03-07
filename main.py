from typing import Union
from fastapi import FastAPI, Request, Response
import json

app = FastAPI()


@app.get("/")
def home(req: Request):
    headers = dict(req.headers)
    print(json.dumps(headers, indent=3))
    message: str = "Hello World"
    return {"message": message}
