#!/usr/bin/env python3
from fastapi import FastAPI
from fastapi import Request
from fastapi import Response
from lib import validation
import uvicorn
from lib import db
from lib import helpers

app = FastAPI()
app.include_router(validation.router)


@app.middleware("http")
async def create_cookie(request: Request, call_next):
    response = await call_next(request)
    if "egoSession" not in request.cookies:
        response.set_cookie(
            key="egoSession",
            value=helpers.randomStr(43),
            httponly=True,
            samesite="none",
        )
    return response


def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, workers=1)


if __name__ == "__main__":
    main()
