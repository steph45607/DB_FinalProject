import mysql.connector
from frames import *
from main import *
from tkinter.messagebox import askyesno

conn=mysql.connector.connect(
    host = '35.238.148.78',
    user = 'staniswinata',
    password = 'staniswinata07',
    database = 'LibraryDB',
    auth_plugin='mysql_native_password'
)
global cursor
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
    id = id.get()
    title = title.get()
    author_name = author_name.get()
    author_id = check_dropdown_three(root, "author_details", "firstName", author_name, "id", "firstName", "lastName")

    publisher = publisher.get()
    pub_id = check_dropdown_three(root, "publisher_details", "name", publisher, "id", "name", "email")

    isbn = isbn.get()

    group = group.get()
    group_id = check_dropdown_three(root, "group_details", "group_name", group, "id", "group_name", "location")

    status = status.get()
    status_id = check_dropdown_two("status_details", "detail", status)
    
    damages = damages.get()
    damages_id = check_dropdown_two("damages_details", "detail", damages)

    statment = ("INSERT INTO book_details VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    data = (id, title, author_id, pub_id, isbn, group_id, status_id, damages_id)
    cursor.execute(statment, data)
    conn.commit()
    print("inserted")
    frames.menuPage(root)

# create a dropdown with 'New' option
def dropDownWithNew(table):
    cursor.execute(f"SELECT * from {table}")
    choose = ["new"]
    count = cursor.fetchall()
    for row in count: # type: ignore
        choose.append(row[1])
    return choose
# create a dropdown withouth 'New' option, default inputs
def dropDown(table):
    cursor.execute(f"SELECT * from {table}")
    choose = []
    count = cursor.fetchall()
    for row in count: # type: ignore
        choose.append(row[1])
    return choose

def add_three(root, table, value1, value2, value3):
    value1 = value1.get()
    value2 = value2.get()
    value3 = value3.get()

    statment = (f"INSERT INTO {table} VALUES (%s, %s, %s)")
    data = (value1, value2, value3)
    cursor.execute(statment, data)
    conn.commit()
    
    frames.close_win(root)

def add_two(root, table, value1, value2):
    value1 = value1.get("1.0", "end-1c")
    value2 = value2.get("1.0", "end-1c")

    statment = (f"INSERT INTO {table} VALUES (%s, %s)")
    data = (value1, value2)
    cursor.execute(statment, data)
    conn.commit()
    frames.close_win(root)
    
def check_dropdown_three(root, table, parameter,value, text1, text2, text3):
    if value == "new":
        frames.popup_three(root, text1, text2, text3, table)
    else:
        statment = f"SELECT id FROM {table} WHERE {parameter} = '{value}'"
        cursor.execute(statment)
        for i in cursor:  # type: ignore
            return i[0]
def check_dropdown_two(table,parameter, value):
    statment = f"SELECT id FROM {table} WHERE {parameter} = '{value}'"
    cursor.execute(statment)
    for i in cursor:  # type: ignore
        return i[0]

def delete(view,selected):
    def confirm():
        answer = askyesno(title='Book Deletion',
                        message='Are you sure that you want to delete this book?')
        if answer:
            query = "DELETE FROM book_details WHERE id=%s"
            # print(view.item(selected['values']))
            this = view.item(selected)['values'][0]
            cursor.execute(query, (this, ))
            conn.commit()
            view.delete(selected)
    confirm()
    # query = "DELETE FROM book_details WHERE id=%s"
    # # print(view.item(selected['values']))
    # this = view.item(selected)['values'][0]
    # cursor.execute(query, (this, ))
    # conn.commit()
    # view.delete(selected)