#!/usr/bin/python3
"""
Returns all values in the states table of hbtn_0e_0_usa;
safe from MySQL injections
Arguments: mysql username, mysql password, database name and state name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()
    sql_query = """SELECT *
                 FROM states
                 WHERE name=%s ORDER BY id ASC"""
    cursor.execute(sql_query, (argv[4],))

    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
