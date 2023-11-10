import mysql.connector as connector

host = "localhost"
user = "root"
password = ""
database = "quan_ly_de_an"

try:
    conn = connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )
    
    cursor = conn.cursor()
except Exception as e:
    print("Error: ", e)