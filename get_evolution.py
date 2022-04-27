#!/usr/bin/env python3

import sqlite3
import sys


# ./get_evolution.py (from OR to) pokemon_name

choice = sys.argv[1]
pokemon_name = sys.argv[2]

def evolves_from():
    cur.execute('''SELECT A.name as Pokemon, C.name as evolves_from
               FROM pokemon A
               INNER JOIN evolves B
               ON A.id = B.id
               INNER JOIN pokemon C
               ON B.from_id = C.id
               WHERE A.name = ?''', [pokemon_name])

    for row in cur:
        print(row[0] + " evolves from: " + row[1])


def evolves_to():
    cur.execute('''SELECT A.name as Pokemon, C.name as evolves_to
               FROM pokemon A
               INNER JOIN evolves B
               ON A.id = B.id
               INNER JOIN pokemon C
               ON B.to_id = C.id
               WHERE A.name = ?''', [pokemon_name])

    for row in cur:
        print(row[0] + " evolves to: " + row[1])


con = sqlite3.connect('database.db')
cur = con.cursor()

if choice == "from":
    evolves_from()
elif choice == "to":
    evolves_to()

con.commit()
con.close()