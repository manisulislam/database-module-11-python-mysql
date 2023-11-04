import mysql.connector

dbName="my_test_dB"
mydbconnection=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database=dbName
)


my_cursor=mydbconnection.cursor()

sqlQuery="""
    create table student(
        roll varchar(5),
        name varchar(10)
    )

"""

my_cursor.execute(sqlQuery)
print("create table successfully")