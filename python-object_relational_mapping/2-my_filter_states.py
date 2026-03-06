#!/usr/bin/python3
"""Displays all states where name matches the argument."""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = db.cursor()

    query = "SELECT id, name FROM states WHERE name = '{}' ORDER BY id ASC".format(argv[4])
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()