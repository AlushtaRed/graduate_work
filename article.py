import json

from main import load_json,save_json

# article_database = {'10073940':'Штукатурка Ротбанд 30 кг', '10072745':'ГСП 12,5 мм влаг.','15163427':'Пескобетон Axton 30 кг','18478820':'Пескобетон 40 кг',
# '10072681':'ГСП 12,5 мм стандарт','10072630':'ГСП 9,5 мм влаг.', '12757510':'Грунтовка Ceresit 10/17', '12756884':'Грунтовка Кнауф 10 л'}


def find_article():
    find_id = input('Введите артикул: ')
    article_database = load_json('article_database.json')
    warehouse = load_json('warehouse.json')
    addresses = load_json('addresses.json')
    stock = load_json('stock.json')
    if article_database.get(find_id):
        print(f'{find_id} - {article_database[find_id]}')
        if stock.get(find_id):
            print(f'Доступный запас - {stock[find_id]}')
        else:
            print('Нет в наличии')
        if warehouse.get(find_id):
            print(f'На складе - {warehouse[find_id]}')
        result = []
        sum_id = 0
        for address, item in addresses.items():
            if find_id in item.keys():
                sum_id += item[find_id]
                print(f'{address} - {item[find_id]} шт ')
                result.append((find_id, address, item[find_id]))
        # if result != []:
        #     print(f'Всего {sum_id} штук')
        return find_id,article_database[find_id]
    else:
        print(f'Артикул {find_id} не найден')
    


def add_to_adrdress(id):
    addresses = load_json('addresses.json')
    print(addresses)
    temp_meaning = input('Введите адрес: ')
    temp_id = id
    temp_capacity = int(input('Введите вместимость: '))
    if addresses.get(temp_meaning).setdefault(temp_id):
        answer = input('На этом адресе уже есть данный артикул, изменить вместимость? y/n: ')
        if answer == 'y':
            addresses.get(temp_meaning)[temp_id] = temp_capacity
    else:
        addresses.get(temp_meaning)[temp_id] = temp_capacity

    print(addresses)
    save_json('addresses.json', addresses)
    
# find_article()
add_to_adrdress('10072745')
# save_article_database(article_database)
# article_database = load_article_database()
# print(article_database)
