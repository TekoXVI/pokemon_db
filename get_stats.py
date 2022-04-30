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

stat = get_stats(pokemon, choice)
if choice == 'all':
    number = stat[0]
    name = stat[1]
    attack = stat[2]
    defense = stat[3]
    hp = stat[4]
    print('Pokemon number', str(number) + ':', name)
    print('Attack:', attack)
    print('Defense:', defense)
    print('HP:', hp)
elif choice == 'number':
    print(pokemon.title(), 'is pokemon number', str(stat) + '. ')
elif choice == 'name':
    print(pokemon.title() + "'s name is", stat + '. Obviously...')
elif choice == 'attack':
    print(pokemon.title(), 'has', stat, 'attack. ')
elif choice == 'defense':
    print(pokemon.title(), 'has', stat, 'defense. ')
elif choice == 'hp':
    print(pokemon.title(), 'has', stat, 'HP. ')
    



con.commit()
con.close()