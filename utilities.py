import json

def view_all_symbol_objects():
    try:
        with open('db.json') as f:
            data = json.load(f)
            f.close()
        return data
    except Exception as e:
        print("an exception occured - {}".format(e))

def view_data_object(name_input):
    try:
        with open('db.json') as f:
            data = json.load(f)
            f.close()
        return data[name_input]
    except Exception as e:
        print("an exception occured - {}".format(e))

def view_data(name_input, key_input):
    try:
        with open('db.json') as f:
            data = json.load(f)
            f.close()
        return data[name_input][key_input]
    except Exception as e:
        print("an exception occured - {}".format(e))
        view_data(name_input, key_input)

def add_db_symbol_k_v(symbol, value):
    try:
        access_file = open("db.json", "r")
        json_object = json.load(access_file)
        access_file.close()

        json_object[symbol]= value

        access_file = open("db.json", "w")
        json.dump(json_object, access_file, indent=4)
        access_file.close()
    except Exception as e:
        print("an exception occured - {}".format(e))

def update_db_object_value(name_input, key_input, valueInput):
    name = name_input
    key = key_input
    value = valueInput
    try:
        access_file = open("db.json", "r")
        json_object = json.load(access_file)
        access_file.close()

        json_object[name][key] = value
        return_object = json_object[name]

        access_file = open("db.json", "w")
        json.dump(json_object, access_file, indent=4)
        access_file.close()
        return return_object
    except Exception as e:
        print("an exception occured - {}".format(e))

def clear_db_object(symbol):
    try:
        access_file = open("db.json", "r")
        json_object = json.load(access_file)
        access_file.close()

        json_object[symbol] = {}

        access_file = open("db.json", "w")
        json.dump(json_object, access_file, indent=4)
        access_file.close()
    except Exception as e:
        print("an exception occured - {}".format(e))