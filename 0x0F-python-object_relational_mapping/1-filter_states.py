#!/usr/bin/python3

'''
Script that lists all states with a name starting with N

Script should take 3 arguments: mysql username,
       mysql password 
       and database name
'''


import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        if state[1][0] == 'N':
            print(state)

    cur.close()
    db.close()
