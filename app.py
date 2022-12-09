import mysql.connector
from frames import *
from main import *

conn=mysql.connector.connect(
    host = '35.238.148.78',
    user = 'staniswinata',
    password = 'staniswinata07',
    database = 'LibraryDB',
    auth_plugin='mysql_native_password'
)

cursor = conn.cursor()

def upload(id, title, author_id, publisher, status, isbn, group_id):
    id = id.get("1.0", "end-1c")
    title = title.get("1.0", "end-1c")
    publisher = publisher.get("1.0", "end-1c")
    author_id = author_id.get("1.0", "end-1c")
    status = status.get("1.0", "end-1c")
    isbn = isbn.get("1.0", "end-1c")
    group_id = group_id.get("1.0", "end-1c")

    statment = ("INSERT INTO book_details VALUES (%s, %s, %s, %s, %s, %s)")
    data = (id, title, author_id, status, isbn, group_id)
    cursor.execute(statment, data)
    conn.commit()

def dropDown(table):
    cursor.execute(f"SELECT * from {table}")
    choose = ["new"]
    count = cursor.fetchall()
    for row in count: # type: ignore
        choose.append(row[1])
    
    return choose

def addAuthor(id, fName, lName):
    id = id.get("1.0", "end-1c")
    fName = fName.get("1.0", "end-1c")
    lName = lName.get("1.0", "end-1c")

    statment = ("INSERT INTO author_details VALUES (%s, %s, %s)")
    data = (id, fName, lName)
    cursor.execute(statment, data)
    conn.commit()

def author_search(root, first):
    if first == "new":
        frames.author_popup(root)
    else:
        statment = f"SELECT id FROM author_details WHERE firstName = '{first}'"
        cursor.execute(statment)
        for i in cursor:  # type: ignore
            print(i[0])
