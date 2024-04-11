#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb, sys

db = MySQLdb.connect(host="localhost", port = 3306, sys.argv[1], sys.argv[2], sys.argv[3])

cur = db.cursor()

numrows = cur.execute("SELECT * from {}".format(sys.argv[3]))

print("Num Rows :", numrows)
