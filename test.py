import mysql.connector

mydbconnection=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password"
)

print(mydbconnection)
