import mysql.connector
from frames import *
from main import *
from tkinter.messagebox import askyesno
from datetime import date

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


# def add_two(root, table, value1, value2):
#     value1 = value1.get("1.0", "end-1c")
#     value2 = value2.get("1.0", "end-1c")

#     statment = f"INSERT INTO {table} VALUES (%s, %s)"
#     data = (value1, value2)
#     cursor.execute(statment, data)
#     conn.commit()
#     frames.close_win(root)


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


def deleteBook(view, selected):
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

def deleteTransaction(view, selected):
    def confirm():
        answer = askyesno(
            title="Transaction Deletion",
            message="Are you sure that you want to delete this transaction?",
        )
        if answer:
            query = "DELETE FROM transaction_details WHERE transaction_id=%s"
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

def refreshDisplay_book(searched, view):
    searched.set("")
    sortBookID_book(view)

def refreshDisplay_transaction(searched, view):
    searched.set("")
    sortTransID_transaction(view)

def refreshDisplay_user(searched, view):
    searched.set("")
    sortUserID_users(view)

def sortUserID_users(view):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        "SELECT u.id, u.name, u.email, r.role_name FROM user_details u JOIN role_details r ON u.role_id = r.id ORDER BY u.id ASC"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        )

def sortTransID_transaction(view):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        "SELECT t.transaction_id, b.title, u.id, u.name, t.borrow_date, t.due_date, s.detail FROM transaction_details t JOIN book_details b ON t.book_id = b.id JOIN user_details u ON t.borrower_id = u.id JOIN transactionStatus_details s ON t.borrow_status = s.id ORDER BY t.transaction_id ASC"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        )

def sortBorrowID_transaction(view):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        "SELECT t.transaction_id, b.title, u.id, u.name, t.borrow_date, t.due_date, s.detail FROM transaction_details t JOIN book_details b ON t.book_id = b.id JOIN user_details u ON t.borrower_id = u.id JOIN transactionStatus_details s ON t.borrow_status = s.id ORDER BY u.id ASC"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        )

def sortBorrowName_transaction(view):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        "SELECT t.transaction_id, b.title, u.id, u.name, t.borrow_date, t.due_date, s.detail FROM transaction_details t JOIN book_details b ON t.book_id = b.id JOIN user_details u ON t.borrower_id = u.id JOIN transactionStatus_details s ON t.borrow_status = s.id ORDER BY u.name ASC"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        )

def sortDateAsc_transaction(view):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        "SELECT t.transaction_id, b.title, u.id, u.name, t.borrow_date, t.due_date, s.detail FROM transaction_details t JOIN book_details b ON t.book_id = b.id JOIN user_details u ON t.borrower_id = u.id JOIN transactionStatus_details s ON t.borrow_status = s.id ORDER BY t.borrow_date ASC"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        )

def sortDateDes_transaction(view):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        "SELECT t.transaction_id, b.title, u.id, u.name, t.borrow_date, t.due_date, s.detail FROM transaction_details t JOIN book_details b ON t.book_id = b.id JOIN user_details u ON t.borrower_id = u.id JOIN transactionStatus_details s ON t.borrow_status = s.id ORDER BY t.borrow_date DESC"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        )

def sortDue_transaction(view):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        "SELECT t.transaction_id, b.title, u.id, u.name, t.borrow_date, t.due_date, s.detail FROM transaction_details t JOIN book_details b ON t.book_id = b.id JOIN user_details u ON t.borrower_id = u.id JOIN transactionStatus_details s ON t.borrow_status = s.id WHERE s.detail = 'overdue' ORDER BY t.due_date DESC"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        )

def sortReturned_transaction(view):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        "SELECT t.transaction_id, b.title, u.id, u.name, t.borrow_date, t.due_date, s.detail FROM transaction_details t JOIN book_details b ON t.book_id = b.id JOIN user_details u ON t.borrower_id = u.id JOIN transactionStatus_details s ON t.borrow_status = s.id WHERE s.detail = 'returned' ORDER BY t.borrow_date ASC"
    )
    set = cursor.fetchall()
    for i in set: #type:ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        )

def sortActive_transaction(view):
    for item in view.get_children():
        view.delete(item)
    
    cursor.execute(
        "SELECT t.transaction_id, b.title, u.id, u.name, t.borrow_date, t.due_date, s.detail FROM transaction_details t JOIN book_details b ON t.book_id = b.id JOIN user_details u ON t.borrower_id = u.id JOIN transactionStatus_details s ON t.borrow_status = s.id WHERE s.detail = 'active' ORDER BY t.borrow_date ASC"
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
            query = "UPDATE transaction_detail SET borrow_status = 'returned' WHERE transaction_id = %s"
            # print(view.item(selected['values']))
            select = view.item(selected)["values"][0]
            cursor.execute(query, (select,))
            conn.commit()
            view.delete(selected)

    confirm()

def addTransactionMethod(bookView, userView, bookSelected, userSelected, dateSelected):
    book = bookView.item(bookSelected)["values"][0]
    user = userView.item(userSelected)["values"][0]
    dateStr = dateSelected.strftime("%Y-%m-%d")
    print(type(dateStr))
    print(book, user, dateStr)

