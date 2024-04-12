#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
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
    cur.execute("SELECT * FROM cities ORDER BY id ASC")

    # Fetching all results
    rows = cur.fetchall()

    # Printing results
    for row in rows:
        print(row)

    # Clean-up
    cur.close()
    db.close()
