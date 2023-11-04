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
    insert into student(roll, name) values("1","anis")

"""

my_cursor.execute(sqlQuery)
mydbconnection.commit()
print("insert table successfully")