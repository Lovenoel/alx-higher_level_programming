#!/usr/bin/python3
"""
Lists all values in the states table of hbtn_0e_0_usa where name matches
the argument, safely.
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
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", (sys.argv[4],))

    # Fetching all results
    rows = cur.fetchall()

    # Printing results
    for row in rows:
        print(row)

    # Clean-up
    cur.close()
    db.close()
