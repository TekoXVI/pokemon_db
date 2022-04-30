#!/usr/bin/env python3

import sqlite3
import sys

def stat_limit_type():
    cur.execute("SELECT * FROM pokemon A INNER JOIN pokemon_type B ON A.id = B.id WHERE B.type_1 = '"+type+"' OR B.type_2 = '"+type+"' ORDER BY "+stat+" DESC LIMIT ?", [limit])
    for row in cur:
        if row[7] == "":
            print(row[1] + ": Attack = " + str(row[2]) + ", Defense = " + str(row[3]) + ", HP = " + str(row[4]) + ", Type = " + row[6])
        else:
            print(row[1] + ": Attack = " + str(row[2]) + ", Defense = " + str(row[3]) + ", HP = " + str(row[4]) + ", Type1 = " + row[6] + ", Type2 = " + row[7])
def stat_limit():
    cur.execute("SELECT * FROM pokemon ORDER BY "+stat+" DESC LIMIT ?", [limit])
    for row in cur:
        print(row[1] + ": Attack = " + str(row[2]) + ", Defense = " + str(row[3]) + ", HP = " + str(row[4]))

def stat_function():
    cur.execute("SELECT * FROM pokemon ORDER BY "+stat+" DESC")
    for row in cur:
        print(row[1] + ": Attack = " + str(row[2]) + ", Defense = " + str(row[3]) + ", HP = " + str(row[4]))

con = sqlite3.connect('database.db')
cur = con.cursor()

# ./get_top.py type limit(optional) type(optional)
try:
    (stat, limit, type) = sys.argv[1:4]
    stat_limit_type()
except:
    try:
        (stat, limit) = sys.argv[1:3]
        stat_limit()
    except:
        stat = sys.argv[1]
        stat_function()

con.commit()
con.close()