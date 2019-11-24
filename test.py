import pymysql
import hashlib
import os
import time
import getpass
import platform 
import datetime

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

conn = pymysql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = "1234",
    database = "store"
)

c = conn.cursor()

def purchase(userid):
    print(userid)
    input()
    pass

lst = [1,2,3,4,5]
lst1 = [6,7,8,9,0]
lst[1] = 1000