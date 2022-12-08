import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error

conn=mysql.connect(
    host = '35.238.148.78',
    user = 'staniswinata',
    password = 'staniswinata07',
    database = 'LibraryDB',
    auth_plugin='mysql_native_password'
)

cursor = conn.cursor()
stamtment = 'insert into book_details values (&s, &s, &s, &s, &s, &s)'
data = pd.read_csv()