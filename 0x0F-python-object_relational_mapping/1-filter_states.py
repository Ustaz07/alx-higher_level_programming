#!/usr/bin/python3
"""Script that lists all states with a name starting with N from the database hbtn_0e_0_usa."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    args = sys.argv
    username = args[1]
    password = args[2]
    database = args[3]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database,
                         charset="utf8")

    # Create cursor object
    cur = db.cursor()

    # Execute SQL query to select states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows
    rows = cur.fetchall()

    # Print the selected states
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
