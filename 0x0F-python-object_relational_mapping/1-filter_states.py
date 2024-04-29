#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

def filter_states(username, password, database):
    """
    Retrieves and prints all states with names starting with 'N'
    from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the database.

    Returns:
        None
    """
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)

        # Create a cursor object to execute queries
        cursor = db.cursor()

        # Execute SQL query to select states starting with 'N'
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Print results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close cursor and database connection
        cursor.close()
        db.close()

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Extract command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call function to filter and print states
    filter_states(username, password, database)
