#!/usr/bin/env python3
from fastapi import FastAPI
from fastapi import Request
from fastapi import Response
from lib import credentials
import random
import string
import uvicorn
from lib import db

app = FastAPI()
app.include_router(credentials.router)


def randomStr(size):
    source = string.ascii_letters + string.digits
    result_str = "".join((random.choice(source) for i in range(size)))
    return result_str


@app.middleware("http")
async def create_cookie(request: Request, call_next):
    response = await call_next(request)
    if "egoSession" not in request.cookies:
        response.set_cookie(
            key="egoSession", value=randomStr(43), httponly=True, samesite="none"
        )
    return response

@app.post("server/login")

def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, workers=1)


if __name__ == "__main__":
    main()
