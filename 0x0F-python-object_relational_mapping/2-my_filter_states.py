#!/usr/bin/python3

'''
script that takes in an argument and displays all values in
    the states table of hbtn_0e_0_usa where name
    matches the argument

Script should take 4 arguments: mysql username,
    mysql password, database name and state name searched
'''

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY states.id ASC""".format(sys.argv[4]).strip("'"))
    [print(state) for state in c.fetchall()]
