import json


addresses = {'1-1L': {'10073940': 40}, '1-1R': {'10072745': 52}, '1-2L': {'10073940': 30}, '1-2R': {'10072630': 68}, '1-3L': {'15163427': 56}, '1-3R': {},
             '1-4L': {}, '1-4R': {}, '1-5L': {'10072745': 52}, '1-5R': {'15163427': 56}, '2-1L': {'10073940': 40}, '2-1R': {}, '2-2L': {'10073940': 40}, '2-2R': {},
             '2-3L': {}, '2-3R': {'10072745': 52}, '2-4L': {}, '2-4R': {}, '2-5L': {}, '2-5R': {}}


def create_addresses():
    global addresses
    alleys = int(input('Введите колличество аллей: '))
    meters = int(input('Введите длинну аллеи: '))
    for i in range(1, alleys+1):
        for j in range(1, meters+1):
            addresses[(f'{i}-{j}L')] = {}
            addresses[(f'{i}-{j}R')] = {}
    print(addresses)
    return addresses
def delete_alley():
    addresses = json_load()
    num_alley = input('Введите номер аллеи для удаления: ')
    temp_adresses = {}
    for key in addresses.keys():
        if key.split('-')[0] != num_alley:
            temp_adresses[key] = {}
    addresses = temp_adresses
    json_save(addresses)
    print(addresses)
    
def add_alley():
    # global addresses
    addresses = json_load()
    alley = int(input('Введите номер аллеи: '))
    meters = int(input('Введите длинну аллеи: '))
    for i in range(1, meters+1):
        addresses[f'{alley}-{i}L']={}
        addresses[f'{alley}-{i}R']={}
    print(addresses)
    json_save(addresses)

def json_save(my_dict):
    with open('addresses.json', 'w') as f:
        json.dump(my_dict, f)

def json_load():
    with open('addresses.json', 'r', encoding='utf-8') as f:
        json_file = json.load(f)
        return json_file



# json_save(addresses)
# json_load()
delete_alley()
# add_alley()