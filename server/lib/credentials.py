#!/usr/bin/env python3
import mysql.connector
from fastapi import Request, APIRouter
from . import db

router = APIRouter()


def cookieExist(cookie: str) -> bool:
    cookie = request.cookies
    if not egoSession in cookie:
        
        return False
    return True

@router.post("/server/login")
async def login(request: Request):
    cookie = request.cookies.get("egoSession")
    data = await request.json()
    uname = data.get("username", None)
    upass = data.get("password", None)
    if not uname or not upass:
        return False
    if not db.login(uname, upass, cookie):
        return False
    return True

