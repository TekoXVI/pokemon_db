#!/usr/bin/env python3

import sqlite3
import sys


# ./list_trainer_pokemon.py

con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute('select t.name as Trainer, p.name as Pokemon from trainer_pokemon tp join trainer t on tp.trainer_id = t.id join pokemon p on tp.pokemon_id = p.id;')

rows = cur.fetchall()
for row in rows:
    print("Trainer:", row[0])
    print("Pokemon:", row[1])
    print()

con.commit()
con.close()