#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

def list_states(username, passwd, db):
    """
    Mysql Connection & lists all states
    """
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            password=passwd,
            database=db)
    cur = db.cursor()
    cur.execute("SELECT * from states order by states.id asc")
    states = cur.fetchall()

    for row in states:
        print(row)

    cur.close()


if __name__ == "__main__":
    """check args len"""
    if (len(sys.argv)) != 4:
            sys.exit(1)

    username = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    list_states(username, passwd, db)
