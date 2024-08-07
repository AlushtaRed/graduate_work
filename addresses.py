import json
from main import load_json,save_json
'''
каждый артикул на адрессе имеет вместимость, то есть количество, которое помещается на полку

'''

# addresses = {'1-1L': {'10073940': 40,'10072745': 52}, '1-1R': {'10072745': 52}, '1-2L': {'10073940': 30}, '1-2R': {'10072630': 68}, '1-3L': {'15163427': 56}, '1-3R': {},
#              '1-4L': {}, '1-4R': {}, '1-5L': {'10072745': 52}, '1-5R': {'15163427': 56}, '2-1L': {'10073940': 40}, '2-1R': {}, '2-2L': {'10073940': 40}, '2-2R': {},
#              '2-3L': {}, '2-3R': {'10072745': 52}, '2-4L': {}, '2-4R': {}, '2-5L': {}, '2-5R': {}}


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
    addresses = load_json('addresses.json')
    num_alley = input('Введите номер аллеи для удаления: ')
    temp_adresses = {}
    for key in addresses.keys():
        if key.split('-')[0] != num_alley:
            temp_adresses[key] = {}
    addresses = temp_adresses
    save_json('addresses.json', addresses)
    print(addresses)
    
def add_alley():
    addresses = load_json('addresses.json')
    alley = int(input('Введите номер аллеи: '))
    meters = int(input('Введите длинну аллеи: '))
    for i in range(1, meters+1):
        addresses[f'{alley}-{i}L']={}
        addresses[f'{alley}-{i}R']={}
    print(addresses)
    save_json('addresses.json', addresses)

    
def show_address():
    addresses = load_json('addresses.json')
    names = load_json('article_database.json')
    print(addresses)
    len_max = max(list(names.values()), key=len)
    len_max = len(len_max)

    address_id = input('Введите адрес: ')
    if address_id in addresses.keys():
        if addresses.get(address_id):
            
            print('Артикул  Наименование          Вместимость')
            for id,capacity in addresses.get(address_id).items():
                print(f'{id} {names.get(id)} - {capacity:>{len_max-len(names.get(id))}}')
        else:
            print('Адрес пустой')
    else:
        print('Адрес не найден')



show_address()
# load_json('addresses.json')
# delete_alley()
# add_alley()