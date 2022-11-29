from getpass import getpass
from mysql.connector import connect, Error

this = """
CREATE TABLE movies(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    release_year YEAR(4),
    genre VARCHAR(100),
    collection_in_mil INT
)
"""

try:
    with connect(
        host="35.238.148.78",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database = "LibraryDB"
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(this)
            connection.commit()
except Error as e:
    print(e)