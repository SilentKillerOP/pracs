import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password="Pass@123"
)

print(mydb)
