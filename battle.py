#!/usr/bin/env python3

import sqlite3
import sys
import random

# from check_effectiveness import *
# from get_stats import get_stats


# ./battle.py trainer_1 trainer_2
(trainer_1, trainer_2) = sys.argv[1:3]

con = sqlite3.connect('database.db')
cur = con.cursor()

def get_name(trainer):
	names = cur.execute('select a.name, c.name from trainer a join trainer_pokemon b on a.id = b.trainer_id join pokemon c on b.pokemon_id = c.id where a.name like ?', [trainer])
	return names 

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

	# print(mon1_type1, mon1_type2, mon2_type1, mon2_type2)
	# print(e11, e12, e21, e22)
	# print(t1_m2, t2_m2)

	if t1_m2 == 4.0 or t2_m2 == 4.0:
		print(mon1, 'is super effective (4x) against', mon2 + '!')
		return 4.0
	elif t1_m2 == 2.0 or t2_m2 == 2.0:
		print(mon1, 'is super effective against', mon2 + '!')
		return 2.0
	elif t1_m2 == 1.0 or t2_m2 == 1.0:
		print(mon1, 'is normally effective against', mon2 + '.')
		return 1.0
	elif t1_m2 == 0.5 and t2_m2 == 0.5:
		print(mon1, 'is not very effective against', mon2 + '.')
		return 0.5
	elif t1_m2 == 0.25 and t2_m2 == 0.25:
		print(mon1, 'is not very effective (0.25x) against', mon2 + '.')
		return 0.25
	elif t1_m2 == 0.0 and t2_m2 == 0.0:
		print(mon1, 'is not effective against', mon2 + '...')
		return 0.0

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
		
def print_effect_win(pname_1, pname_2, tname_1, tname_2):
	print()
	print(pname_1, 'defeats', pname_2 + '. ')
	print()
	print(tname_1, 'wins the battle against', tname_2 + '! ')
	
def print_attack_win(pname_1, pname_2, tname_1, tname_2):
	print()
	print(pname_1, 'has more attack than', pname_2 + '. ')
	print_effect_win(pname_1, pname_2, tname_1, tname_2)
	
def print_defense_win(pname_1, pname_2, tname_1, tname_2):
	print()
	print(pname_1, 'has the same attack, but more defense than', pname_2 + '. ')
	print_effect_win(pname_1, pname_2, tname_1, tname_2)
	
def print_hp_win(pname_1, pname_2, tname_1, tname_2):
	print()
	print(pname_1, 'has the same attack and defense, but more hp than', pname_2 + '. ')
	print_effect_win(pname_1, pname_2, tname_1, tname_2)

t1 = next(get_name(trainer_1))
tname_1 = t1[0]
pname_1 = t1[1]

t2 = next(get_name(trainer_2))
tname_2 = t2[0]
pname_2 = t2[1]

print(tname_1, 'brings his', pname_1, 'into battle against', tname_2 + '\'s', pname_2 + '. ')
print()

mon1 = next(get_mon(pname_1))
mon1_name = mon1[0]
mon1_type1 = mon1[1]
mon1_type2 = mon1[2]

mon2 = next(get_mon(pname_2))
mon2_name = mon2[0]
mon2_type1 = mon2[1]
mon2_type2 = mon2[2]

effect12 = effect(pname_1, pname_2)
effect21 = effect(pname_2, pname_1)

# compare types
if effect12 > effect21:
	print_effect_win(pname_1, pname_2, tname_1, tname_2)
elif effect12 < effect21:
	print_effect_win(pname_1, pname_2, tname_1, tname_2)                    
else:
	# compare attack if same type
	if get_stats(pname_1, 'attack') > get_stats(pname_2, 'attack'):
		print_attack_win(pname_1, pname_2, tname_1, tname_2)
	elif get_stats(pname_1, 'attack') < get_stats(pname_2, 'attack'):
		print_attack_win(pname_2, pname_1, tname_2, tname_1)
	else:
		# compare defense if same attack
		if get_stats(pname_1, 'defense') > get_stats(pname_2, 'defense'):
			print_defense_win(pname_1, pname_2, tname_1, tname_2)
		elif get_stats(pname_1, 'defense') < get_stats(pname_2, 'defense'):
			print_defense_win(pname_2, pname_1, tname_2, tname_1)
		else:
			# compare hp if same defense
			if get_stats(pname_1, 'hp') > get_stats(pname_2, 'hp'):
				print_hp_win(pname_1, pname_2, tname_1, tname_2)
			elif get_stats(pname_1, 'hp') < get_stats(pname_2, 'hp'):
				print_hp_win(pname_2, pname_1, tname_2, tname_1)
			else:
				r = random.randint(0,1)
				if r == 0:
					print_effect_win(pname_1, pname_2, tname_1, tname_2)
				else:
					print_effect_win(pname_2, pname_1, tname_2, tname_1)
					
con.commit()
con.close()
