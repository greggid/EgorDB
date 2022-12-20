#!/usr/bin/env python3
import mysql.connector
from fastapi import Request, APIRouter
from .db import isValidUserExist

router = APIRouter()


def credentialsExist(data: dict) -> bool:
    uname = data.get("username", None)
    upass = data.get("password", None)
    if not uname or not upass:
        return False
    if isValidUserExist(uname, upass):
        return True
    return False

def credId(data: dict) -> bool:
    idsearch = data.get("id", None)
    if not (idsearch):
        return False
    if getAllById(idsearch):
        return True
    return False

@router.post("/server/login")
async def login(request: Request) -> dict:
    data = await request.json()
    if credentialsExist(data):
        return data
    return False


