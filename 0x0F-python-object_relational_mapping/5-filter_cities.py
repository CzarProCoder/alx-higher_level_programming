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
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id""")
    print(", ".join([city[2]
                     for city in c.fetchall()
                     if city[4] == sys.argv[4]]))
