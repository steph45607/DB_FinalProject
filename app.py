from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

app = Flask(__name__)

# app.config['MYSQL_HOST'] = '35.238.148.78:3306'
# app.config['MYSQL_USER'] = 'staniswinata'
# app.config['MYSQL_PASSWORD'] = 'staniswinata07'
# app.config['MYSQL_DB'] = 'LibraryDB'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://staniswinata:staniswinata07@35.238.148.78/LibraryDB'
db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    author_id = db.Column(db.String(255))
    status = db.Column(db.String(255), default = "Availabe")
    isbn = db.Column(db.String(255))
    group_id = db.Column(db.String(255))

    def __repr__(self):
        return '<Book %r>' % self.id

# @app.route('/form')
# def form():
#     return render_template('form.html')

# @app.route('/login', methods = ['POST', 'GET'])
# def login():
#     if request.method == 'GET':
#         return 'Login via the login form'
    
#     if request.method == 'POST':
#         id = request.form['book id']
#         title = request.form['title']
#         author = request.form['author_id']
#         status = request.form['status']
#         isbn = request.form['isbn']
#         group_id = request.form['group']
#         cursor = db.connection.cursor()
#         cursor.execute ('''INSERT INTO book_details VALUES (%d, %s, %s, %s, %s, %s)''', (id, title, author, status, isbn, group_id))
#         db.connection.commit()
#         cursor.close()
#         return "Done!"

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        pass
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
# app.run(debug=True)