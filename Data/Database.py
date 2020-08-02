import sqlite3
db = "Pokemon.db"

#helper function to check if a table exists
# check if the table exists
def check_table(db="Pokemon.db", table_name="Pokemon"):
    # Create connection and cursor objects
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    try:
        cur.execute('''SELECT * FROM Pokemon''')
        conn.commit()
    except sqlite3.OperationalError as e:
        print(e)
        return "no such table" in e.args[0]
    cur.close()
    conn.close()
    return True

def add(data:dict, table_name:str):
    # Create a connection and cursor object

    table_exists = check_table(table_name=table_name)
    if(table_exists != True):
        raise Exception(table_exists)
    print(table_exists)

    if(table_name=="Pokemon"):
        add_pokemon(data)

    elif(table_name=="Ability"):
        add_abillity(data)

    elif(table_name == "Move"):
        pass

    elif(table_name == "Item"):
        pass

# function to add data to the pokemon table.
def add_pokemon(data:dict):
    # check data to see if it matters that the keys matter this format: id (real), name (text), types (text),
    # weight (real), height (real), hp (real), attack (real), sp_atk (real), defense (real), sp_def (real), speed (real), abilities (text).
    keys = {"id":int, "name":str, "types":str, 'weight':int, 'height':int, 'hp':int, 'attack':int, 'special-attack':int, 'defense':int,
            'special-defense': int, 'speed': int, 'abilities':str
            }
    check = lambda keys, d: all([k in keys.keys() and type(d[k])==keys[k] for k in d.keys()])
    if False == check(keys, data):
        raise Exception("Dictionary data not formatted probably. Should be formated like this: {}. Data: {}".format(keys,data))

    # define connection and cursor object
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.execute("""INSERT INTO Pokemon VALUES ({},'{}','{}',{},{},{},{},{},{},{},{},'{}')""".format(
        data['id'], data['name'], data['types'], data['weight'], data['height'], data['hp'], data['attack'],
        data['special-attack'], data['defense'], data['special-defense'], data['speed'], data['abilities']
    ))

    conn.commit()

    conn.close()
    print("Pokemon {} was successfully added to the {} table in the {} database".format(data['name'], "Pokemon", db))
    return data

def add_ability(data:dict):
    #check data to see if it matches this format:
    #name(text), effect(text), pokemon(list - of effected pokemon)
    keys = {"name":str, 'effect':str, "pokemon":list}
    check = lambda keys, d: all([k in keys.keys() and type(d[k]) == keys[k] for k in d.keys()])
    if False == check(keys, data):
        raise Exception(
            "Dictionary data not formatted probably. Should be formated like this: {}. Data: {}".format(keys, data))

    #define cursor and connection objects
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    print(data)
    try:
        cur.execute("""INSERT INTO ability VALUES ('{}',"{}");""".format(
        data['name'], data['effect']
        ))

    # allowing user input for exception handling, in the ability case there are some cases where "" are used for the descriptions.
    except Exception as e:
        userInput = input("An exception occured! Here's the data generated: {}. Would you like to modify it: ".format(data))
        if(userInput=="y"):
            new_effect = input("Please enter the new effect you would like for this entry: ")
            cur.execute("""INSERT INTO ability VALUES ('{}', "{}");""".format(
                data['name'], new_effect
            ))
        else:
            return False


    conn.commit()

    conn.close()
    print("Ability {} was successfully added to the {} table in the {} database".format(data['name'], "Ability", db))
    return data

def add_move(data:dict):
    pass

def add_item(data:dict):
    pass

def search():
    pass

def get():
    pass

def delete_item():
    pass