#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


if __name__ == '__main__':
    # Connect to MySQL database
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Get the state name to search for
    state_name = sys.argv[4]

    # Create cursor object
    cur = db.cursor()

    # Execute SQL query to select states matching the provided name
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Fetch all rows
    rows = cur.fetchall()

    # Print the selected states
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
