#!/usr/bin/python3
"""
Script that lists all cities of a specific state from the database hbtn_0e_4_usa
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

    # Prepare SQL query to select cities of the specified state
    query = """
            SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ')
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            """

    # Execute SQL query with state name as parameter
    cur.execute(query, (sys.argv[4],))

    # Fetch result
    result = cur.fetchone()

    # Print cities if result is not None
    if result and result[0]:
        print(result[0])
    else:
        print("")

    # Close cursor and database connection
    cur.close()
    db.close()
