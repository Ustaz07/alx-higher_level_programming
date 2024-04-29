#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
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

    # Create cursor object
    cur = db.cursor()

    # Execute SQL query to select all cities along with their states
    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
            """
    cur.execute(query)

    # Fetch all rows
    rows = cur.fetchall()

    # Print the cities and their respective states
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
