import mysql.connector

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

def dropDown():
    cursor.execute("SELECT * from test")
    choose = []
    count = cursor.fetchall()
    for row in count:
        choose.append(row[1])

    return choose

def author_search(first):
    statment = f"SELECT id FROM test WHERE name = '{first}'"
    cursor.execute(statment)
    for i in cursor:
        print(i[0])