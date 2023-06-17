#!/usr/bin/python3

'''
Script that takes in the name of a state as an argument
and lists all cities of that state

The script should take 4 arguments: mysql username,
mysql password, database name and state name
'''

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name
                 FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 WHERE states.name LIKE %s
                 ORDER BY cities.id ASC""")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
