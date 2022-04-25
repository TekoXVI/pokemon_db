#!/usr/bin/env python3

import sqlite3
import sys

def get_mon(name):
	mon = cur.execute('select a.name, b.type_1, b.type_2 from pokemon a join pokemon_type b using(id) where a.name like ?' , [name])
	return mon
	
# ./get_type.py name
name = sys.argv[1]

con = sqlite3.connect('database.db')
cur = con.cursor()

row = next(get_mon(name))
mon = row[0]
type1 = row[1]
type2 = row[2]

if type2 == '':
    print(mon, 'is a', type1 + '-type pokemon. ')
else:
    print(mon, 'is a', type1 + '- and', type2 + '-type pokemon. ')

con.commit()
con.close()