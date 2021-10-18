import os
import pymysql

# Get username from Gitpod
username = os.getenv('C9_USER')

# Connect to database
connection = pymysql.connect(host='localhost',
                            user = username,
                            password='',
                            db='Chinook')

try:
    #Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #Close connection, whether or not successful
    connection.close()