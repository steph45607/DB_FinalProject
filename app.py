from flask import Flask, redirect, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

conn=mysql.connector.connect(
    host = '35.238.148.78',
    user = 'staniswinata',
    password = 'staniswinata07',
    database = 'LibraryDB',
    auth_plugin='mysql_native_password'
)

cursor = conn.cursor()

def upload(id, name):
    idpar = id.get("1.0", "end-1c")
    namepar = name.get("1.0", "end-1c")
    statment = ("INSERT INTO test VALUES (%s, %s)")
    data = (idpar, namepar)
    cursor.execute(statment, data)
    conn.commit()

