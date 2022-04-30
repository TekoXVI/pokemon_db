#!/usr/bin/env python3

import sqlite3
import sys


# ./compare.py pokemon_name1 pokemon_name2

pokemon_name1 = sys.argv[1]
pokemon_name2 = sys.argv[2]

con = sqlite3.connect('database.db')
cur = con.cursor()

#select * from pokemon A inner join pokemon_type B on A.id = B.id;
#select * from pokemon A inner join pokemon_type B on A.id = B.id where A.id = ?;

cur.execute('select * from pokemon A inner join pokemon_type B on A.id = B.id where A.name = ?', [pokemon_name1])
for row in cur:
    if row[7] == "":
        print(row[1] + ": " + "Attack = " + str(row[2]) + ", Defense = " + str(row[3]) + ", HP = " + str(row[4]) + ", Type = " + row[6])
    else:
        print(row[1] + ": " + "Attack = " + str(row[2]) + ", Defense = " + str(row[3]) + ", HP = " + str(row[4]) + ", Type = " + row[6] + ", Type2 = " + row[7])

cur.execute('select * from pokemon A inner join pokemon_type B on A.id = B.id where A.name = ?', [pokemon_name2])
for row in cur:
    if row[7] == "":
        print(row[1] + ": " + "Attack = " + str(row[2]) + ", Defense = " + str(row[3]) + ", HP = " + str(row[4]) + ", Type = " + row[6])
    else:
        print(row[1] + ": " + "Attack = " + str(row[2]) + ", Defense = " + str(row[3]) + ", HP = " + str(row[4]) + ", Type = " + row[6] + ", Type2 = " + row[7])

con.commit()
con.close()