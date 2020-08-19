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
        add_ability(data)

    elif(table_name == "Move"):
        add_move(data)

    elif(table_name == "Item"):
        add_item(data)

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
    # check data to see if it matches this format:
    # damage_class (text) - indicates the type of damage (status or physical), accuracy (int), effect(text), id (int),
    # power(int), 
    keys = {'damage_class':str, 'accuracy': int,  'id': int, 'power':int, 'name':str, 'pp':int,
            'type':str, 'effects': str
            }
    check = lambda keys, d: all([k in keys.keys() and type(d[k]) == keys[k] for k in d.keys()])
    if False == check(keys, data):
        raise Exception(
            "Dictionary data not formatted probably. Should be formated like this: {}. Data: {}".format(keys, data))

    # define cursor and connection objects
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    #insert into move table
    try:
        cur.execute("""INSERT INTO move VALUES ('{}','{}', {}, {}, '{}', {}, '{}', "{}");""".format(
        data['damage_class'], data['accuracy'],  data['id'], data['power'], data['name'], data['pp'],
            data['type'], data['effects']
        ))

    # allowing user input for exception handling, in the ability case there are some cases where "" are used for the descriptions.
    except Exception as e:
        print("An error occured! Exception: {}".format(e))
        print("Here's the id: {}. Data: {}".format(data['id'], data))
        effects = input("effects: ")
        cur.execute("""INSERT INTO move VALUES ('{}','{}', {}, {}, '{}', {}, '{}', "{}");""".format(
            data['damage_class'], data['accuracy'], data['id'], data['power'], data['name'], data['pp'],
            data['type'], effects
        ))

        print("Modifications made successfully to move {}!".format(data['id']))


    conn.commit()

    conn.close()
    print("Move {} was successfully added to the {} table in the {} database".format(data['name'], "Ability", db))
    return data

#for the items table in database
def add_item(data:dict):
    # check data to see if it matches this format:
    # damage_class (text) - indicates the type of damage (status or physical), accuracy (int), effect(text), id (int),
    # power(int),
    keys = { 'id': int,  'name': str, 'effect': str
            }

    check = lambda keys, d: all([k in keys.keys() and type(d[k]) == keys[k] for k in d.keys()])
    if False == check(keys, data):
        raise Exception(
            "Dictionary data not formatted probably. Should be formated like this: {}. Data: {}".format(keys, data)
        )


    # create cursor and conn objects
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    # insert into item table
    try:
        cur.execute("""INSERT INTO item VALUES ({},'{}', '{}');""".format(
           int(data['id']), data['name'], data['effect'].replace("'", "")
        ))

    except Exception as e:
        print("Exception {} occured on line 165".format(e))
        a = input("Would you like to modify the data (y/n): ")
        if(a=="y"):
            effects = input("effects: ")

            cur.execute("""INSERT INTO item VALUES ({},'{}', '{}');""".format(
                int(data['id']), data['name'], effects
            ))

    # commit command
    conn.commit()

    # close conn object
    conn.close()

    print("Successfully entered {} item in item table".format(data['name']))

#returns true if an input is in the table in hte database
def search(table_name:str , item:dict):
    try:
        # create cursor and connection objects
        conn = sqlite3.connect(db)
        cur = conn.cursor()

        # execute command
        cur.execute("""SELECT * FROM {} WHERE {}={}.""".format(table_name, 'id', item['id']))

        # commit command
        conn.commit()

        return True

    except Exception as e:
        print("ERROR {} occured in search() function!".format(e))
        return False


# returns an item given input
def get(table_name:str, item:dict):
    # Error checking
    if('id' not in item.keys()):
        raise Exception("ERROR! item dict doesn't have id as a key")

    if(not search(table_name, item)):
        raise Exception("ERROR! Item: {} does not exist in table {}".format(item, table_name))

    # create connection and cursor objects
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    # find item
    cur.execute('''SELECT * FROM {} WHERE id={}'''.format(table_name, item['id']))

    # get the data
    rows = cur.fetchall()

    # commit changes
    conn.commit()

    # close objects
    cur.close()
    conn.close()

    return rows[0]

# edit item given a table name, id to identify the item and the new item you want to replace
def edit(table_name:str, id:int, new_data:dict):
    # define conn and cur objects
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    # generate aString - string that covers the SET part using new_data dict
    aString = ",".join([str(k)+"="+str(new_data[k]) for k in new_data.keys()])
    print("edit_item(), line 242: " + aString)


    # UPDATE item
    cur.execute('''UPDATE {} SET {} WHERE id={}'''.format(table_name, aString, id))

    # commit changes
    conn.commit()

    # close objects
    cur.close()
    conn.close()


# delete an item given a table name and the item itself
def delete(id:int, table_name:str):
    # create conn and cur objects
    conn = sqlite3.connect(db)
    cur = conn.cursor

    # execute command
    cur.execute('''DELETE FROM {} WHERE id={}'''.format(table_name, id))

    # commit changes
    conn.commit()

    # close objects
    cur.close()
    conn.close()



