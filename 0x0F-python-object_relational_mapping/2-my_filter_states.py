#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa where name
matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Database connection
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Cursor object creation
    cur = db.cursor()

    # Query execution
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (sys.argv[4],))

    # Fetching all results
    rows = cur.fetchall()

    # Printing results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
