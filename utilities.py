import json

def view_data(name_input, key_input):
    name = name_input
    key = key_input
    try:
        with open('db.json') as f:
            data = json.load(f)
            f.close()
        return data[name][key]
    except Exception as e:
        print("an exception occured - {}".format(e))
        view_data(name, key)

def update_data(name_input, key_input, valueInput):
    name = name_input
    key = key_input
    value = valueInput
    try:
        access_file = open("db.json", "r")
        json_object = json.load(access_file)
        access_file.close()

        json_object[name][key] = value

        access_file = open("db.json", "w")
        json.dump(json_object, access_file, indent=4)
        access_file.close()
    except Exception as e:
        print("an exception occured - {}".format(e))
        update_data(name, key, value)