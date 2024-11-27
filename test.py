import os
import MySQLdb

db= MySQLdb.connect(host="host", user="root1", passwd="abcde", db="test")    # connect to database


cur =db.cursor()    # cursor object     
cur.execute("SELECT * FROM table_name")    # execute query  

db.close()    # close connection


