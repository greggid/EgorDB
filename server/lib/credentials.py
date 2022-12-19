#!/usr/bin/env python3
import mysql.connector
from fastapi import Request, APIRouter

router = APIRouter()


def credentialsExist(data: dict) -> bool:
    uname = data.get("username", None)
    upass = data.get("password", None)
    if not uname or not upass:
        return False
    return True


@router.post("/server/login")
async def login(request: Request) -> dict:
    data = await request.json()
    if credentialsExist(data):
        return data
    return False

def separateData(login):
    string_uname = data["uname"]
    string_pass = data["pass"]
    return string_uname, string_pass
