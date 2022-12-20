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

# create a dropdown 
def searchBooks(table):
    cursor.execute(f"SELECT * from {table}")
    choose = []
    count = cursor.fetchall()
    for row in count: # type: ignore
        choose.append(row[1])
    return choose

# to upload hte books to book_details database
def upload(root, id, title, author_name, publisher, isbn, group, status, damages):
    id = id.get("1.0", "end-1c")
    title = title.get("1.0", "end-1c")
    author_name = author_name.get()
    author_id = check_dropdown(root, "author_details", "firstName", author_name, "id", "firstName", "lastName")

    publisher = publisher.get()
    pub_id = check_dropdown(root, "publisher_details", "name", publisher, "id", "name", "email")

    isbn = isbn.get("1.0", "end-1c")

    group = group.get()
    group_id = check_dropdown(root, "group_details", "group_name", group, "id", "group_name", "location")

    status = status.get()
    status_id = check_dropdown(root, "status_details", "detail", status, "id", "detail", "")
    
    damages = damages.get()
    damages_id = check_dropdown(root, "damages_details", "detail", damages, "id", "detail", "")

    statment = ("INSERT INTO book_details VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    data = (id, title, author_id, pub_id, isbn, group_id, status_id, damages_id)
    cursor.execute(statment, data)
    conn.commit()
    print("inserted")

# create a dropdown 
def dropDown(table):
    cursor.execute(f"SELECT * from {table}")
    choose = ["new"]
    count = cursor.fetchall()
    for row in count: # type: ignore
        choose.append(row[1])
    return choose

def add(root, table, value1, value2, value3):
    value1 = value1.get("1.0", "end-1c")
    value2 = value2.get("1.0", "end-1c")
    value3 = value3.get("1.0", "end-1c")

    statment = (f"INSERT INTO {table} VALUES (%s, %s, %s)")
    data = (value1, value2, value3)
    cursor.execute(statment, data)
    conn.commit()
    frames.close_win(root)
    

def check_dropdown(root, table, parameter,value, text1, text2, text3):
    if value == "new":
        frames.popup_three(root, text1, text2, text3, table)
    else:
        statment = f"SELECT id FROM {table} WHERE {parameter} = '{value}'"
        cursor.execute(statment)
        for i in cursor:  # type: ignore
            return i[0]

