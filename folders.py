import json


def read_json():
    with open("user_friends.json") as f:
        diction = json.load(f)
    return diction


def beautiful(lst):
    return "<" + " | ".join(lst) + ">"
    

def get_keys(folder):
    lst_of_keys = []
    if type(folder) == dict:
        for key in folder:
            lst_of_keys.append(key)
        print(beautiful(lst_of_keys))
    elif type(folder) == list:
        counter = 0
        for key in folder:
            counter += 1
            lst_of_keys.append("elem" + str(counter-1))
        print(beautiful(lst_of_keys))
    else:
        print(folder)
    

def open_folder(folder, key):
    return folder[key]



def main_pro():
    position = []
    folder = read_json()
    key = input("Press Enter to start.")

    if key == "":
        while key != "finish":
            print()
            print("Your position: " + " -> ".join(position))
            if type(folder) == dict:
                get_keys(folder)
                print()
                key = input("Write the name of the folder: ")
                position.append(key)
                folder = open_folder(folder, key)
            elif type(folder) == list:
                get_keys(folder)
                print()
                key = int(input("Write the number of the folder starting from 0: "))
                position.append("elem" + str(key))
                folder = open_folder(folder, key)
            else:
                get_keys(folder)
                key = "finish"

main_pro()
    
            











    
