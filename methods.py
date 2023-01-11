import mysql.connector
from frames import *
from main import *
from tkinter.messagebox import askyesno, showinfo
from datetime import timedelta, date

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
def upload(root, title, author_name, publisher, isbn, group, status, damages):
    queryID = "select id from book_details ORDER BY id DESC LIMIT 1;"
    cursor.execute(queryID)
    id = cursor.fetchall()
    for i in id: # type: ignore
        id = i[0] + 1

    title = title.get()

    author_name = author_name.get()
    author_id = check_dropdown_three(
        root, "author_details", "firstName", "lastName", author_name, "id", "firstName", "lastName"
    )

    publisher = publisher.get()
    pub_id = check_dropdown_three(
        root, "publisher_details", "name", "email", publisher, "id", "name", "email"
    )

    isbn = isbn.get()

    group = group.get()
    group_id = check_dropdown_three(
        root, "group_details", "group_name", "location", group, "id", "group_name", "location"
    )

    status = status.get()
    status_id = check_dropdown_two("status_details", "detail", status)

    damages = damages.get()
    damages_id = check_dropdown_two("damages_details", "detail", damages)

    statment = "INSERT INTO book_details VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    data = (id, title, author_id, pub_id, isbn, group_id, status_id, damages_id)
    cursor.execute(statment, data)
    conn.commit()
    showinfo("Data added to database", "Book Added")


# create a dropdown with 'New' option
def dropDownWithNew(table):
    cursor.execute(f"SELECT * from {table}")
    choose = ["new"]
    count = cursor.fetchall()
    for row in count:  # type: ignore
        choose.append(row[1] + " " + row[2])
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


# def add_two(root, table, value1, value2):
#     value1 = value1.get("1.0", "end-1c")
#     value2 = value2.get("1.0", "end-1c")

#     statment = f"INSERT INTO {table} VALUES (%s, %s)"
#     data = (value1, value2)
#     cursor.execute(statment, data)
#     conn.commit()
#     frames.close_win(root)


def check_dropdown_three(root, table, parameter1, parameter2, value, text1, text2, text3):
    if value == "new":
        frames.popup_three(root, text1, text2, text3, table)
    else:
        statment = f"SELECT id FROM {table} WHERE CONCAT({parameter1}, ' ', {parameter2}) = '{value}'"
        cursor.execute(statment)
        for i in cursor:  # type: ignore
            return i[0]


def check_dropdown_two(table, parameter, value):
    statment = f"SELECT id FROM {table} WHERE {parameter} = '{value}'"
    cursor.execute(statment)
    for i in cursor:  # type: ignore
        return i[0]


def deleteBook(view, selected):
    def confirm():
        answer = askyesno(
            title="Book Deletion",
            message="Are you sure that you want to delete this book?",
        )
        if answer:
            query = "DELETE FROM book_details WHERE id=%s"
            select = view.item(selected)["values"][0]
            cursor.execute(query, (select,))
            conn.commit()
            view.delete(selected)

    confirm()

def deleteTransaction(view, selected):
    def confirm():
        answer = askyesno(
            title="Transaction Deletion",
            message="Are you sure that you want to delete this transaction?",
        )
        if answer:
            query = "DELETE FROM transaction_details WHERE transaction_id=%s"
            select = view.item(selected)["values"][0]
            cursor.execute(query, (select,))
            conn.commit()
            view.delete(selected)

    confirm()

def sortStatusBooks(view, parameter, value):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        f"select b.id, b.title, a.firstName, a.lastName, p.name, b.isbn, g.group_name, s.detail, d.detail from book_details b join author_details a on b.author_id = a.id join publisher_details p on b.pub_id = p.id join group_details g on b.group_id = g.id join status_details s on b.status_id = s.id join damages_details d on b.damages_id = d.id WHERE {parameter} = '{value}'"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
        )

def sortStatusTransaction(view, parameter, parameter2, value, order):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        f"SELECT t.transaction_id, b.title, u.id, u.name, t.borrow_date, t.due_date, s.detail FROM transaction_details t JOIN book_details b ON t.book_id = b.id JOIN user_details u ON t.borrower_id = u.id JOIN transactionStatus_details s ON t.borrow_status = s.id WHERE {parameter} = '{value}' ORDER BY {parameter2} {order}"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))


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

def searchTitle_book(view, searched):
    title = searched.get()
    for item in view.get_children():
        view.delete(item)
    statement =  f"select b.id, b.title, a.firstName, a.lastName, p.name, b.isbn, g.group_name, s.detail, d.detail from book_details b join author_details a on b.author_id = a.id join publisher_details p on b.pub_id = p.id join group_details g on b.group_id = g.id join status_details s on b.status_id = s.id join damages_details d on b.damages_id = d.id WHERE b.title = '{title}'"
    cursor.execute(statement)
    
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
        )

def searchBorrowerID_transaction(view, searched):
    id = searched.get()
    for item in view.get_children():
        view.delete(item)
    statement =  f"SELECT t.transaction_id, b.title, u.id, u.name, t.borrow_date, t.due_date, s.detail FROM transaction_details t JOIN book_details b ON t.book_id = b.id JOIN user_details u ON t.borrower_id = u.id JOIN transactionStatus_details s ON t.borrow_status = s.id WHERE u.id = '{id}'"
    cursor.execute(statement)
    
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        )

def searchUserID_user(view, searched):
    id = searched.get()
    for item in view.get_children():
        view.delete(item)
    statement =  f"SELECT u.id, u.name, u.email, r.role_name FROM user_details u JOIN role_details r ON u.role_id = r.id WHERE u.id = '{id}'"
    cursor.execute(statement)
    
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3])
        )

def searchAuthorID(view, searched):
    id = searched.get()
    for item in view.get_children():
        view.delete(item)
    statement =  f"SELECT * FROM author_details WHERE id = '{id}'"
    cursor.execute(statement)
    
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2])
        )

def searchPubID(view, searched):
    id = searched.get()
    for item in view.get_children():
        view.delete(item)
    statement =  f"SELECT * FROM publisher_details WHERE id = '{id}'"
    cursor.execute(statement)
    
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2])
        )

def refreshDisplay_book(searched, view):
    searched.set("")
    sortBooks(view, "b.id", "ASC")

def refreshDisplay_transaction(searched, view):
    searched.set("")
    sortTransaction(view, "transaction_id", "ASC")

def refreshDisplay_user(searched, view):
    searched.set("")
    sortUsers(view, "u.id", "ASC")

def refreshDisplay_pub(searched, view):
    searched.set("")
    sortPublisher(view, "id", "ASC")

def refreshDisplay_author(searched, view):
    searched.set("")
    sortAuthor(view, "id", "ASC")

def sortBooks(view, parameter, order):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        f"select b.id, b.title, a.firstName, a.lastName, p.name, b.isbn, g.group_name, s.detail, d.detail from book_details b join author_details a on b.author_id = a.id join publisher_details p on b.pub_id = p.id join group_details g on b.group_id = g.id join status_details s on b.status_id = s.id join damages_details d on b.damages_id = d.id ORDER BY {parameter} {order}"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
        )

def sortUsers(view, parameter, order):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        f"SELECT u.id, u.name, u.email, r.role_name FROM user_details u JOIN role_details r ON u.role_id = r.id ORDER BY {parameter} {order}"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3])
        )

def sortAuthor(view, parameter, order):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        f"SELECT * FROM author_details ORDER BY {parameter} {order}"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2])
        )

def sortPublisher(view, parameter, order):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        f"SELECT * FROM publisher_details ORDER BY {parameter} {order}"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2])
        )

def sortUserRoles(view, parameter, value):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        f"SELECT u.id, u.name, u.email, r.role_name FROM user_details u JOIN role_details r ON u.role_id = r.id WHERE {parameter} = '{value}'"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3])
        )

def sortTransaction(view, parameter, order):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        f"SELECT t.transaction_id, b.title, u.id, u.name, t.borrow_date, t.due_date, s.detail FROM transaction_details t JOIN book_details b ON t.book_id = b.id JOIN user_details u ON t.borrower_id = u.id JOIN transactionStatus_details s ON t.borrow_status = s.id ORDER BY {parameter} {order}"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        )

def isReturned(view, selected):
    def confirm():
        answer = askyesno(
            title="Book Return",
            message="The book has been returned?",
        )
        if answer:
            query = "UPDATE transaction_details SET borrow_status = 1 WHERE transaction_id = %s"
            select = view.item(selected)["values"][0]
            cursor.execute(query, (select,))
            conn.commit()
            view.delete(selected)
            sortTransaction(view, "transaction_id", "ASC")

    confirm()

def addTransactionMethod(bookView, userView, bookSelected, userSelected, dateSelected):
    book = bookView.item(bookSelected)["values"][0]
    user = userView.item(userSelected)["values"][0]
    dateStr = dateSelected.strftime("%Y-%m-%d")
    due = dateSelected + timedelta(days=14)

    queryID = "select transaction_id from transaction_details ORDER BY transaction_id DESC LIMIT 1;"
    cursor.execute(queryID)
    id = cursor.fetchall()
    for i in id: # type: ignore
        id = i[0] + 1

    query = "INSERT INTO transaction_details VALUES (%s, %s, %s, %s, %s, %s)"
    data = (id, book, user, dateStr, due, 0)
    cursor.execute(query, data)
    conn.commit()
    showinfo("Data added to database", "Transaction Added")

def checkOverdue():
    queryStatus = "SELECT transaction_id, due_date FROM transaction_details WHERE borrow_status = 0 "
    cursor.execute(queryStatus)
    activeID = cursor.fetchall()


    for i in activeID: # type: ignore
        if i[1] < date.today():
            queryOverdue = f"UPDATE transaction_details set borrow_status = 2 WHERE transaction_id = {i[0]}"
            cursor.execute(queryOverdue)
            conn.commit()

