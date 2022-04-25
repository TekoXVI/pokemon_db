#!/usr/bin/env python3

import sqlite3
import sys

# ./get_stats pokemon choice
(pokemon, choice) = sys.argv[1:3]

con = sqlite3.connect('database.db')
cur = con.cursor()

def get_stats(pokemon, choice):
    stat = cur.execute('select * from pokemon where name like ?', [pokemon])
    mon = next(stat)
    if choice == 'all':
        return mon
    elif choice == 'number':
        return mon[0]
    elif choice == 'name':
        return mon[1]
    elif choice == 'attack':
        return mon[2]
    elif choice == 'defense':
        return mon[3] 
    elif choice == 'hp':
        return mon[4] 
    

print(get_stats(pokemon, choice))


con.commit()
con.close()