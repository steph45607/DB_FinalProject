from tkinter import ttk
import mysql.connector
from tkinter import *


conn=mysql.connector.connect(
    host = '35.238.148.78',
    user = 'staniswinata',
    password = 'staniswinata07',
    database = 'LibraryDB',
    auth_plugin='mysql_native_password'
)
global cursor
cursor = conn.cursor()

cursor.execute("select * from book_details join status_details, damages_details")
this = cursor.fetchall()
print(this)