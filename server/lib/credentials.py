#!/usr/bin/env python3
import mysql.connector
from fastapi import Request, APIRouter
from . import db
from fastapi import Response
from fastapi.responses import JSONResponse

router = APIRouter()


def cookieExist(cookie: str) -> bool:
    cookie = request.cookies
    if not egoSession in cookie:
        return False
    return True


@router.post("/server/login")
async def login(request: Request):
    incorrect = {"succesful": False, "reason": "Incorrect login or password"}
    missing = {"succesful": False, "reason": "Missing data"}
    correct = {"succesful": True}
    cookie = request.cookies.get("egoSession")
    data = await request.json()
    uname = data.get("username", None)
    upass = data.get("password", None)
    if not uname or not upass:
        return JSONResponse(status_code=401, content = missing)    
    if not db.login(uname, upass, cookie):
        return JSONResponse(status_code=402, content = incorrect)
    return JSONResponse(status_code=200, content = correct)
