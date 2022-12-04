#!/usr/bin/python3
"""
Returns all values in the states table of hbtn_0e_0_usa where name matches
 the given argument
Arguments: mysql username, mysql password, database name and
 state name searched
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
                 WHERE name LIKE '{:s}' ORDER BY id ASC""".format(argv[4])
    cursor.execute(sql_query)
    for row in cursor.fetchall():
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db.close()
