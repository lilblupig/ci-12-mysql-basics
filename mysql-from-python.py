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
        cursor.execute("DELETE FROM Friends WHERE name in ('Jim', 'Bob')")
        connection.commit()
finally:
    # Close connection, whether or not successful
    connection.close()