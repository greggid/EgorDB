#!/usr/bin/env python3
import mysql.connector
from . import credentials
from . import settings
from fastapi import APIRouter

router = APIRouter()


def connectToDB():
    try:
        __mydb = mysql.connector.connect(
            host="localhost",
            user="egordb",
            password="egordb_password",
            database="egordb",
        )
        print("Connection to MySQL DB successful")
        return __mydb
    except Exception as e:
        print("Connection to MySQL DB unsuccessful")


__mydb = connectToDB()


@router.post("/server/login")
async def sqlRequest(separateData, __mydb):
    try:
        mycursor = await __mydb.cursor()
        mycursor.execute("SELECT * FROM users WHERE username = string_uname")
        row = mycursor.fetchall()
        return row
    except Exception as e:
        raise SystemExit(e)


# string_uname, string_pass
