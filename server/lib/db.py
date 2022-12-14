#!/usr/bin/env python3
import mysql.connector
from lib import credentials


def connectToDB():
    try:
        mydb = mysql.connector.connect(
        )
        return mydb
    except Exception as e:
        raise SystemExit(e)


__mydb = connectToDB()


def connectMysql(login):
    mycursor = __mydb.cursor()
    mycursor.execute("SELECT * FROM users")
    myresult = mycursor.fetchone()
    print(myresult)
