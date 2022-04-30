#!/usr/bin/env python3

import sqlite3
import sys

# ./check_effectiveness.py name1 name2
(name1, name2) = sys.argv[1:3]

con = sqlite3.connect('database.db')
cur = con.cursor()

def check(type1, type2):
	effect = cur.execute('select * from effectiveness where attack_type like ? and defense_type like ?', [type1, type2])
	return effect
	
def get_mon(name):
	mon = cur.execute('select a.name, b.type_1, b.type_2 from pokemon a join pokemon_type b using(id) where a.name like ?' , [name])
	return mon

def effect(name_1, name_2):
    row1 = next(get_mon(name_1))
    mon1 = row1[0]
    mon1_type1 = row1[1]
    mon1_type2 = row1[2]

    row2 = next(get_mon(name_2))
    mon2 = row2[0]
    mon2_type1 = row2[1]
    mon2_type2 = row2[2]

    row11 = next(check(mon1_type1, mon2_type1))
    e11 = row11[2]
    print(e11)

    if mon2_type2 != '':
    	row12 = next(check(mon1_type1, mon2_type2))
    	e12 = row12[2]
    else:
    	e12 = e11

    if mon1_type2 != '':
    	row21 = next(check(mon1_type2, mon2_type1))
    	e21 = row21[2]
    	if mon2_type2 != '':
    		row22 = next(check(mon1_type2, mon2_type2))
    		e22 = row22[2]
    	else:
    		e22 = e21
    else:
    	e21 = e11
    	e22 = e12
    	  
    if mon1_type2 != '' and mon2_type2 != '':
    	t1_m2 = e11 * e12
    	t2_m2 = e21 * e22
    elif mon1_type2 == '' and mon2_type2 != '':
    	t1_m2 = e11 * e12
    	t2_m2 = t1_m2
    elif mon1_type2 != '' and mon2_type2 == '':
    	t2_m2 = e21
    	t1_m2 = e11
    else:
        t1_m2 = e11
        t2_m2 = t1_m2

    print(mon1_type1, mon1_type2, mon2_type1, mon2_type2)
    print(e11, e12, e21, e22)
    print(t1_m2, t2_m2)

    if t1_m2 == 4.0 or t2_m2 == 4.0:
    	print(mon1, 'is super effective (4x) against', mon2 + '!')
    	# return 4.0
    elif t1_m2 == 2.0 or t2_m2 == 2.0:
    	print(mon1, 'is super effective against', mon2 + '!')
    	# return 2.0
    elif t1_m2 == 1.0 or t2_m2 == 1.0:
    	print(mon1, 'is normally effective against', mon2 + '.')
    	# return 1.0
    elif t1_m2 == 0.5 or t2_m2 == 0.5:
    	print(mon1, 'is not very effective against', mon2 + '.')
    	# return 0.5
    elif t1_m2 == 0.25 or t2_m2 == 0.25:
    	print(mon1, 'is not very effective (0.25x) against', mon2 + '.')
    	# return 0.25
    elif t1_m2 == 0.0 or t2_m2 == 0.0:
    	print(mon1, 'is not effective against', mon2 + '...') 
    	# return 0.0


effect(name1, name2)

con.commit()
con.close()
