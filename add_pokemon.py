#!/usr/bin/env python3

import sqlite3
import sys


# ./add_pokemon.py trainer_id pokemon_id

(trainer_id, pokemon_id) = sys.argv[1:3]

con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute('REPLACE INTO trainer_pokemon (trainer_id, pokemon_id) VALUES (?, ?)', [trainer_id, pokemon_id])

mon = cur.execute('select name from pokemon where id = ?', [pokemon_id])
mname = next(mon)[0]

trainer = cur.execute('select name from trainer where id = ?', [trainer_id])
tname = next(trainer)[0]

print(tname + "'s pokemon is now:", mname)

con.commit()
con.close()