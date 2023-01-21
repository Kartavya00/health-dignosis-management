from pymysql import *
import mysql.connector
conn = ""
cur = ""

selectedpid = 0


def connecttodb():
    global conn
    global cur

    try:
        # providing connection string
        conn = connect(host='localhost', user='root',
                       password='root123', db='hospitaldb')

        # Connect to Database
        cur = conn.cursor()

        return True

    except:
        return False



def closeConnection():
    global conn
    conn.close()
