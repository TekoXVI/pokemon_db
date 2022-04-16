import sqlite3

choice = input("Construct or destruct the db?")

def main():

    if choice.lower() == "construct":
        build_pokemon_table()
        build_effectiveness_table()
        build_types_table()
        build_evolves_table()
    elif choice.lower() == "destruct":
        destruct_db()
    else:
        print("Please enter 'construct' to construct the db or 'destruct' to destroy the db.")


def build_pokemon_table():
    
    fin = open("pokemon.txt", "r")
    for line in fin:
        #this is just stripping all the unnecessary characters out of each line to make it easier to
        #insert into the db
        line = line.replace("(", "")
        line = line.replace(")", "")
        line = line.replace("'", "")
        line = line.replace(" ", "")
        line = line.replace("\n", "")
        line = line.split(",")

        con = sqlite3.connect('database.db')
        cur = con.cursor()

        cur.execute('INSERT INTO pokemon (id, name, attack, defense, hp) VALUES (?, ?, ?, ?, ?)', [line[0], line[1], line[2], line[3], line[4]])
        con.commit()
        con.close()
    fin.close()

def build_effectiveness_table():
    fin = open("effectiveness.txt", "r")
    for line in fin:
        #this is just stripping all the unnecessary characters out of each line to make it easier to
        #insert into the db
        line = line.replace("(", "")
        line = line.replace(")", "")
        line = line.replace("'", "")
        line = line.replace(" ", "")
        line = line.replace("\n", "")
        line = line.split(",")

        con = sqlite3.connect('database.db')
        cur = con.cursor()

        cur.execute('INSERT INTO effectiveness (attack_type, defense_type, effect) VALUES (?, ?, ?)', [line[0], line[1], line[2]])
        con.commit()
        con.close()
    fin.close()

def build_types_table():
    fin = open("types.txt", "r")
    for line in fin:
        #this is just stripping all the unnecessary characters out of each line to make it easier to
        #insert into the db
        line = line.replace("(", "")
        line = line.replace(")", "")
        line = line.replace("'", "")
        line = line.replace(" ", "")
        line = line.replace("\n", "")
        line = line.split(",")

        con = sqlite3.connect('database.db')
        cur = con.cursor()

        cur.execute('INSERT INTO pokemon_type (id, type_1, type_2) VALUES (?, ?, ?)', [line[0], line[1], line[2]])
        con.commit()
        con.close()
    fin.close()

def build_evolves_table():
    fin = open("evolves.txt", "r")
    for line in fin:
        #this is just stripping all the unnecessary characters out of each line to make it easier to
        #insert into the db
        line = line.replace("(", "")
        line = line.replace(")", "")
        line = line.replace("'", "")
        line = line.replace(" ", "")
        line = line.replace("\n", "")
        line = line.split(",")

        con = sqlite3.connect('database.db')
        cur = con.cursor()

        cur.execute('INSERT INTO evolves (id, from_id, to_id) VALUES (?, ?, ?)', [line[0], line[1], line[2]])
        con.commit()
        con.close()
    fin.close()

def destruct_db():
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    cur.execute('DELETE FROM pokemon')
    cur.execute('DELETE FROM effectiveness')
    cur.execute('DELETE FROM pokemon_type')
    cur.execute('DELETE FROM evolves')
    con.commit()
    con.close()

main()