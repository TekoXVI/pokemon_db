#!/usr/bin/env python3

import sqlite3
import sys


# ./compare.py pokemon_name1 pokemon_name2

pokemon_name1 = sys.argv[1]
pokemon_name2 = sys.argv[2]

con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute('SELECT * FROM pokemon WHERE name LIKE ?', [pokemon_name1])
for row in cur:
    print(row[1] + ": " + "Attack = " + str(row[2]) + ", Defense = " + str(row[3]) + ", HP = " + str(row[4]))

cur.execute('SELECT * FROM pokemon WHERE name LIKE ?', [pokemon_name2])
for row in cur:
    print(row[1] + ": " + "Attack = " + str(row[2]) + ", Defense = " + str(row[3]) + ", HP = " + str(row[4]))

con.commit()
con.close()