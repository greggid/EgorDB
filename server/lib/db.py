#!/usr/bin/env python3
import mysql.connector
from . import validation
from . import settings
from fastapi import Request


def connectToDB():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="egordb",
            password="egordb_password",
            database="egordb",
        )
        return mydb
    except Exception as e:
        print(e)


__mydb = connectToDB()
cursor = __mydb.cursor()


def getAllData():
    try:
        cursor.execute("SELECT * from data;")
    except Exception as e:
        print(e)


def login(username: str, password: str, cookie: str) -> bool:
    if isValidUserExist(username, password):
        setCookie(username, password, cookie)
        return True
    return False


def isValidUserExist(username: str, password: str) -> bool:
    try:
        cursor.execute(
            "SELECT COUNT(*) FROM users WHERE username = %s AND password = %s;",
            [username, password],
        )
        row = cursor.fetchall()
        return bool(row[0][0])
    except Exception as e:
        print(e)


def setCookie(username: str, password: str, cookie: str) -> None:
    try:
        cursor.execute(
            "UPDATE users SET ilovecookie = %s WHERE username = %s AND password = %s;",
            [cookie, username, password],
        )
        __mydb.commit()
    except Exception as e:
        print(e)
