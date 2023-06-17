#!/usr/bin/python3

'''
Script that takes in the name of a state as an argument
and lists all cities of that state

The script should take 4 arguments: mysql username,
mysql password, database name and state name
'''

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id;")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
