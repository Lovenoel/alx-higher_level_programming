#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
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
    cur.execute("SELECT cities.name FROM cities INNER JOIN states \
            ON cities.state_id=states.id WHERE states.name=%s \
            ORDER BY cities.id ASC", (sys.argv[4],))

    # Fetching all results
    rows = cur.fetchall()

    # Printing results
    print(", ".join(row[0] for row in rows))

    # Clean-up
    cur.close()
    db.close()
