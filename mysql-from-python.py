import os
import datetime
import pymysql

# Get username from Gitpod
username = os.getenv('C9_USER')

# Connect to database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    #Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        rows = [(23, 'Bob'),
                (24, 'Jim'),
                (25, 'Del')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;", rows)
        connection.commit()
finally:
    # Close connection, whether or not successful
    connection.close()