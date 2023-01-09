import mysql.connector
from frames import *
from main import *
from tkinter.messagebox import askyesno

conn = mysql.connector.connect(
    host="35.238.148.78",
    user="staniswinata",
    password="staniswinata07",
    database="LibraryDB",
    auth_plugin="mysql_native_password",
)
global cursor
cursor = conn.cursor()

# create a dropdown
def searchBooks(table):
    cursor.execute(f"SELECT * from {table}")
    choose = []
    count = cursor.fetchall()
    for row in count:  # type: ignore
        choose.append(row[1])
    return choose


# to upload hte books to book_details database
def upload(root, id, title, author_name, publisher, isbn, group, status, damages):
    id = id.get()
    title = title.get()
    author_name = author_name.get()
    author_id = check_dropdown_three(
        root, "author_details", "firstName", author_name, "id", "firstName", "lastName"
    )

    publisher = publisher.get()
    pub_id = check_dropdown_three(
        root, "publisher_details", "name", publisher, "id", "name", "email"
    )

    isbn = isbn.get()

    group = group.get()
    group_id = check_dropdown_three(
        root, "group_details", "group_name", group, "id", "group_name", "location"
    )

    status = status.get()
    status_id = check_dropdown_two("status_details", "detail", status)

    damages = damages.get()
    damages_id = check_dropdown_two("damages_details", "detail", damages)

    statment = "INSERT INTO book_details VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
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
    for row in count:  # type: ignore
        choose.append(row[1])
    return choose


# create a dropdown withouth 'New' option, default inputs
def dropDown(table):
    cursor.execute(f"SELECT * from {table}")
    choose = []
    count = cursor.fetchall()
    for row in count:  # type: ignore
        choose.append(row[1])
    return choose


def add_three(root, table, value1, value2, value3):
    value1 = value1.get()
    value2 = value2.get()
    value3 = value3.get()

    statment = f"INSERT INTO {table} VALUES (%s, %s, %s)"
    data = (value1, value2, value3)
    cursor.execute(statment, data)
    conn.commit()

    frames.close_win(root)


def add_two(root, table, value1, value2):
    value1 = value1.get("1.0", "end-1c")
    value2 = value2.get("1.0", "end-1c")

    statment = f"INSERT INTO {table} VALUES (%s, %s)"
    data = (value1, value2)
    cursor.execute(statment, data)
    conn.commit()
    frames.close_win(root)


def check_dropdown_three(root, table, parameter, value, text1, text2, text3):
    if value == "new":
        frames.popup_three(root, text1, text2, text3, table)
    else:
        statment = f"SELECT id FROM {table} WHERE {parameter} = '{value}'"
        cursor.execute(statment)
        for i in cursor:  # type: ignore
            return i[0]


def check_dropdown_two(table, parameter, value):
    statment = f"SELECT id FROM {table} WHERE {parameter} = '{value}'"
    cursor.execute(statment)
    for i in cursor:  # type: ignore
        return i[0]


def delete(view, selected):
    def confirm():
        answer = askyesno(
            title="Book Deletion",
            message="Are you sure that you want to delete this book?",
        )
        if answer:
            query = "DELETE FROM book_details WHERE id=%s"
            # print(view.item(selected['values']))
            select = view.item(selected)["values"][0]
            cursor.execute(query, (select,))
            conn.commit()
            view.delete(selected)

    confirm()

def sortAuthor_book(view):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        "select b.id, b.title, a.firstName, a.lastName, p.name, b.isbn, g.group_name, s.detail, d.detail from book_details b join author_details a on b.author_id = a.id join publisher_details p on b.pub_id = p.id join group_details g on b.group_id = g.id join status_details s on b.status_id = s.id join damages_details d on b.damages_id = d.id ORDER BY p.name ASC"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
        )

def sortBookID_book(view):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        "select b.id, b.title, a.firstName, a.lastName, p.name, b.isbn, g.group_name, s.detail, d.detail from book_details b join author_details a on b.author_id = a.id join publisher_details p on b.pub_id = p.id join group_details g on b.group_id = g.id join status_details s on b.status_id = s.id join damages_details d on b.damages_id = d.id ORDER BY b.id ASC"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
        )

def sortTitle_book(view):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        "select b.id, b.title, a.firstName, a.lastName, p.name, b.isbn, g.group_name, s.detail, d.detail from book_details b join author_details a on b.author_id = a.id join publisher_details p on b.pub_id = p.id join group_details g on b.group_id = g.id join status_details s on b.status_id = s.id join damages_details d on b.damages_id = d.id ORDER BY b.title ASC"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
        )

def sortPublisher_book(view):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        "select b.id, b.title, a.firstName, a.lastName, p.name, b.isbn, g.group_name, s.detail, d.detail from book_details b join author_details a on b.author_id = a.id join publisher_details p on b.pub_id = p.id join group_details g on b.group_id = g.id join status_details s on b.status_id = s.id join damages_details d on b.damages_id = d.id ORDER BY p.name ASC"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
        )

def sortStatusAvail_book(view):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        "select b.id, b.title, a.firstName, a.lastName, p.name, b.isbn, g.group_name, s.detail, d.detail from book_details b join author_details a on b.author_id = a.id join publisher_details p on b.pub_id = p.id join group_details g on b.group_id = g.id join status_details s on b.status_id = s.id join damages_details d on b.damages_id = d.id WHERE s.detail = 'available'"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
        )

def sortStatusUnavail_book(view):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        "select b.id, b.title, a.firstName, a.lastName, p.name, b.isbn, g.group_name, s.detail, d.detail from book_details b join author_details a on b.author_id = a.id join publisher_details p on b.pub_id = p.id join group_details g on b.group_id = g.id join status_details s on b.status_id = s.id join damages_details d on b.damages_id = d.id WHERE s.detail = 'unavailable'"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
        )


def searchTitle(view, title):
    for item in view.get_children():
        view.delete(item)
    statement =  f"select b.id, b.title, a.firstName, a.lastName, p.name, b.isbn, g.group_name, s.detail, d.detail from book_details b join author_details a on b.author_id = a.id join publisher_details p on b.pub_id = p.id join group_details g on b.group_id = g.id join status_details s on b.status_id = s.id join damages_details d on b.damages_id = d.id WHERE b.title = '{title}'"
    cursor.execute(statement)
    
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
        )

