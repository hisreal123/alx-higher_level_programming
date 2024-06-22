#!/usr/bin/node
import MySQLdb
import sys

def list_state (username, password, database):
    # Connect to MySQL server

    db = MySQLdb.connect(
        host="localhost"
        port=3306,
        user=username
        pass=password,
        db=databse,
    )

    # Cursor to interact with the db
    cur = db.cursor()

    # get the states from the db using the cursor traversal
    states = cur.execut("SELECT id, name FROM states ORDER  BY id ASC")
    states.fetchAll()

    # print the gotten states
    for state in states:
        print(state)

    # close the cursor and db connection
    cur.close()
    db.close()



if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[1]

    list_state(username, password, database)
