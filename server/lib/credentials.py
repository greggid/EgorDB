#!/usr/bin/env python3
import mysql.connector
from fastapi import Request, APIRouter

router = APIRouter()


def credentialsExist(data: dict) -> bool:
    username = data.get("username", None)
    password = data.get("password", None)
    if not username or not password:
        return False
    return True


@router.post("/server/login")
async def login(request: Request) -> dict:
    data = await request.json()
    if credentialsExist(data):
        return data
    return False
