import json

"""
stock - наличие товара суммарно в магазине на складе
addresses - список адресов в торговом зале, на которых размещены определенные артикулы с заданной вместимостью
warehouse - наличие товара на складе магазина
article_database - список артикулов с названиями

сотрудник торгового зала создает список адрессов, сответствующий торговому оборудованию, 
прописывает, какой товар там должен лежать и в каком количестве

сотрудник торгового зала при выкладке товара на полку, списвает его со склада

отчеты:
    пополнение - програма расчитывает нужно ли пополнять товар со склада в торговый зал
    неучтенный товар - если вместимость плюс запас на складе меньше стока, значит мы не знаем, 
    где часть товара и нужно его найти
    аномалии склада - если на складе числится товар, которого нет на остатках магазина
    
"""


addresses = {'1-1L': {'10073940': 40}, '1-1R': {'10072745': 52}, '1-2L': {'10073940': 30}, '1-2R': {'10072630': 68}, '1-3L': {'15163427': 56}, '1-3R': {},
             '1-4L': {}, '1-4R': {}, '1-5L': {'10072745': 52}, '1-5R': {'15163427': 56}, '2-1L': {'10073940': 40}, '2-1R': {}, '2-2L': {'10073940': 40}, '2-2R': {},
             '2-3L': {}, '2-3R': {'10072745': 52}, '2-4L': {}, '2-4R': {}, '2-5L': {}, '2-5R': {}}

def save_json(my_dict, saving_dict):
    with open(my_dict, 'w', encoding="utf-8") as f:
        json.dump(saving_dict, f)

def load_json(my_dict):
    with open(my_dict, 'r', encoding='utf-8') as f:
        json_file = json.load(f)
        return json_file

def add():
    print(addresses)
    temp_meaning = input('Введите адрес: ')
    temp_id = input('Введите артикул: ')
    temp_quantity = int(input('Введите количество: '))
    if addresses.get(temp_meaning).setdefault(temp_id):
        addresses.get(temp_meaning)[temp_id] = addresses.get(
            temp_meaning)[temp_id] + temp_quantity
    else:
        addresses.get(temp_meaning)[temp_id] = temp_quantity

    print(addresses)


def replace_():
    find_result = find()
    replace_id = str(find_result[0][0])
    print(addresses)
    current_address = input('Введите адрес, с которого переносим: ')
    new_address = input('Введите адрес, куда переносим: ')
    temp_quantity = int(input('Введите количество: '))
    sum_id = 0
    result = []
    curent_quantity = 0
    for i in find_result:
        if current_address in i:
            curent_quantity = i[2]
    if curent_quantity == 0:
        print('На этом адресе нет данного артикула')
    else:    
        if temp_quantity < curent_quantity:
            if addresses.get(new_address).setdefault(replace_id):
                addresses.get(new_address)[replace_id] = addresses.get(
                    new_address)[replace_id] + temp_quantity
            else:
                addresses.get(new_address)[replace_id] = temp_quantity
            addresses.get(current_address)[replace_id] -= temp_quantity
        elif curent_quantity == temp_quantity:
            if addresses.get(new_address).setdefault(replace_id):
                addresses.get(new_address)[replace_id] = addresses.get(
                    new_address)[replace_id] + temp_quantity
            else:
                addresses.get(new_address)[replace_id] = temp_quantity
            del addresses.get(current_address)[replace_id]
        else:
            print('На адресе не хватает товара')

    for address, item in addresses.items():
        if replace_id in item.keys():
            sum_id += item[replace_id]
            print(f'Артикул {replace_id} - {address} - {item[replace_id]} шт ')
            result.append((replace_id, address, item[replace_id]))
    if result != []:
        print(f'Всего {sum_id} штук')


def find():
    find_id = input('Введите артикул для поиска: ')
    result = []
    sum_id = 0
    for address, item in addresses.items():
        if find_id in item.keys():
            sum_id += item[find_id]
            print(f'Артикул {find_id} - {address} - {item[find_id]} шт ')
            result.append((find_id, address, item[find_id]))
    if result != []:
        print(f'Всего {sum_id} штук')
    if result == []:
        print('Артикул не найден')
    return result


def delete():
    delete_id = str(find()[0][0])
    print(delete_id)
    flag_exit = True
    while flag_exit:
        print('1 - удалить все')
        print('2 - удалить с адреса')
        print('x - выйти')
        answer = input('Как хотите удалить?')
        if answer == '1':
            for temp in addresses.values():
                # print(temp)
                if delete_id in temp.keys():
                    temp.pop(delete_id)
            flag_exit = False
        if answer == '2':
            sum_id = 0
            delete_adress = input('С какого адреса удалить: ')
            for adress, item in addresses.items():
                if adress == delete_adress:
                    del item[delete_id]
            for adress, item in addresses.items():
                if delete_id in item.keys():
                    sum_id += item[delete_id]
                    print(
                        f'Артикул {delete_id} - {adress} - {item[delete_id]} шт ')
                    # result.append((delete_id,address,item[delete_id]))
        if answer == 'x':
            flag_exit = False

    print(addresses)


def main():

    flag_exit = True
    while flag_exit:
        print("1 - добавить артикул")
        print("2 - найти артикул")
        print("3 - удалить с адреса")
        print("4 - переместить артикул")
        answer = input("Введите номер команды или 'x' для выхода:  ")
        if answer == "1":
            add()
        if answer == "2":
            find()
        if answer == "3":
            delete()
        if answer == "4":
            replace_()

        elif answer == "x":
            flag_exit = False


if __name__ == '__main__':
    main()
    load_json()
    save_json()
