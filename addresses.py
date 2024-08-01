addresses = {}

def create_addresses():
    global addresses
    alleys = int(input('Введите колличество аллей: '))
    meters = int(input('Введите длинну аллеи: '))
    for i in range(1, alleys+1):
        for j in range(1, meters+1):
            addresses[(f'{i}-{j}L')] = {}
            addresses[(f'{i}-{j}R')] = {}
    print(addresses)
def delete_alley():
    global addresses
    # print(addresses)
    num_alley = input('Введите номер аллеи для удаления: ')
    temp_adresses = {}
    for key in addresses.keys():
        if key.split('-')[0] != num_alley:
            temp_adresses[key] = {}
    addresses = temp_adresses
    print(addresses)
    
def add_alley():
    global addresses
    alley = int(input('Введите номер аллеи: '))
    meters = int(input('Введите длинну аллеи: '))
    for i in range(1, meters+1):
        addresses[f'{alley}-{i}L']={}
        addresses[f'{alley}-{i}R']={}
    print(addresses)

create_addresses()
delete_alley()
add_alley()