#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb, sys



def list_states(username, passwd, db):
    """
    Mysql Connection & lists all states
    """
    db = MySQLdb.connect(host="localhost", port = 3306, username = username, password = passwd, database = db)
    cur = db.cursor()
    numrows = cur.execute("SELECT * from {}".format(db))
    print("Num Rows :", numrows)

    cursor.close()

if __name__ == "__main__":
    #check args len
    if (len(sys.argv)) != 4:
            sys.exit(1)

    username = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    list_states(username, passwd, db)
