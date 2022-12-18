#!/usr/bin/env python3
import mysql.connector
from lib import credentials
from . import settings

def connectToDB():
    try:
        __mydb = mysql.connector.connect(
        host="localhost",
        user="egordb",
        password="egordb_password",
        database ="egordb"

        )
        return __mydb
    except Exception as e:
        raise SystemExit(e)


__mydb = connectToDB()


def sqlRequest(login):
    mycursor = __mydb.cursor()
    mycursor.execute("SELECT * FROM users")
    myresult = mycursor.fetchone()
    return myresult
