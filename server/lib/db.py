#!/usr/bin/env python3
import mysql.connector
from . import credentials
from . import settings


def connectToDB():
    try:
        test1 = mysql.connector.connect(
            host="localhost",
            user="egordb",
            password="egordb_password",
            database="egordb",
        )
        print("Connection to MySQL DB successful")
        return test1
    except Exception as e:
        print("Connection to MySQL DB unsuccessful")
        print(e)


__mydb = connectToDB()


def login(username: str, password: str, cookie: str) -> bool:
    if isValidUserExist(username, password):
        setCookie(username, password, cookie)
        return True
    return False


def isValidUserExist(username: str, password: str) -> bool:
    try:
        cursor = __mydb.cursor()
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
        cursor = __mydb.cursor()
        cursor.execute(
            "UPDATE users SET ilovecookie = %s WHERE username = %s AND password = %s;",
            [cookie, username, password],
    )
        __mydb.commit()
    except Exception as e:
        print(e)

