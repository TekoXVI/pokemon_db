#!/usr/bin/env python3

import sqlite3
import sys


# ./add_trainer.py id name

(id, name) = sys.argv[1:3]

con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute('REPLACE INTO trainer (id, name) VALUES (?, ?)', [id, name])

con.commit()
con.close()