#!/usr/bin/env python3
import MySQLdb
import sys


def list_states(username, password, database):
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results
    states = cursor.fetchall()

    # Print each state
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
   list_states(sys.argv[1], sys.argv[2], sys.argv[3])
