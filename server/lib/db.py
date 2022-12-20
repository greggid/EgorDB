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


def isValidUserExist(username: str, password: str) -> bool:
    try:
        cursor = __mydb.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s AND password = %s;", [username, password])
        row = cursor.fetchall()
        return bool(row[0][0])
    except Exception as e:
        print(e)

def setCookieInDB(username: str, password: str):
    cursor = __mydb.cursor()
    cursor.execute("SELECT password FROM users WHERE username = %s", [username])
    row = cursor.fetchall()
    ValidPass = row[0]
    if ValidPass == password:
        cursor.execute("UPDATE users SET ilovecookie = %s WHERE username = %s", [set_cookie, username])
        result = cursor.fetchall()
        print(result)
        



 




