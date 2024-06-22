#!/usr/bin/env python3
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve all states sorted by id
    cursor.execute("SELECT * FROM states ORDER")

    # Fetch all the results
    states = cursor.fetchall()

    # Print each state
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
