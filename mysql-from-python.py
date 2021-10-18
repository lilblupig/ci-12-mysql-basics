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
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
    # Close connection, whether or not successful
    connection.close()