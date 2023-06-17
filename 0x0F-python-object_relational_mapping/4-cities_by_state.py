#!/usr/bin/python3

'''
A script that lists all cities from the database hbtn_0e_4_usa

Should take 3 arguments: mysql username,
    mysql password and database name
'''

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states
                ON cities.state_id=states.id
                ORDER BY cities.id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
