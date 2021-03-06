import os
import pymysql

# Get username from workspace(Gitpod)
# (modify this variable if running from another environment)
username = os.getenv('USER')

# connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')
try:
    # run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # close connection, regardless of whether the above was successful.
    connection.close()
