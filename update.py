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
    update student set name="aa" where name="anis"

"""

my_cursor.execute(sqlQuery)
mydbconnection.commit()
print("update table successfully")