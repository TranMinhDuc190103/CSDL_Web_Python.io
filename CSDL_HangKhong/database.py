import mysql.connector

host = "127.0.0.1"
user = "root"
password = ""
database = "your_database"

conn = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = database
)

cursor = conn.cursor()
