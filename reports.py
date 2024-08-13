from print import print_report
from main import load_json,save_json

article_database = {'10073940':'Штукатурка Ротбанд 30 кг', '10072745':'ГСП 12,5 мм влаг.','15163427':'Пескобетон Axton 30 кг','18478820':'Пескобетон 40 кг',
'10072681':'ГСП 12,5 мм стандарт','10072630':'ГСП 9,5 мм влаг.', '12757510':'Грунтовка Ceresit 10/17', '12756884':'Грунтовка Кнауф 10 л'}

addresses = {'1-1L': {'10073940': 40}, '1-1R': {'10072745': 52}, '1-2L': {'10073940': 30}, '1-2R': {'10072630': 68}, '1-3L': {'15163427': 56}, '1-3R': {},
             '1-4L': {}, '1-4R': {}, '1-5L': {'10072745': 52}, '1-5R': {'15163427': 56}, '2-1L': {'10073940': 40}, '2-1R': {}, '2-2L': {'10073940': 40}, '2-2R': {},
             '2-3L': {}, '2-3R': {'10072745': 52}, '2-4L': {}, '2-4R': {}, '2-5L': {}, '2-5R': {}}

warehouse = {'10073940':4000, '10072745':520,
             '15163427':560,'18478820':240,
            '10072681':520,'10072630':340,
            '12757510':360, '12756884':115,
            '123':12}

stock = {'10073940':440, '10072745':520,
             '15163427':560,'18478820':240,
            '10072681':520,'10072630':340,
            '12757510':420, '12756884':148}

def anomaly_of_stock():
    # article_database = load_json('article_database.json')
    # warehouse = load_json('warehouse.json')
    # stock = load_json('stock.json')
    anomaly = {}
    for id in warehouse.keys():
        if id in stock.keys() and warehouse.get(id)>stock.get(id):
            anomaly[id]= warehouse.get(id) - stock.get(id)
        elif id not in stock.keys():
            anomaly[id] = warehouse.get(id)
    print_report(anomaly,'Аномалия')

# Неучтенный товар
def unaccounted_goods():
    unaccounted_goods = {}
    for id in stock.keys():
        find_id = id
        sum_id = 0
        for  item in addresses.values():
            if find_id in item.keys():
                sum_id += item[find_id]
        if (stock.setdefault(id,0)-warehouse.setdefault(id,0)-int(sum_id))>0:
            # unaccounted_goods[id] = (stock.get(id) - warehouse.get(id) - int(sum_id))
            unaccounted_goods[id] = abs(sum_id - (stock.get(id) - warehouse.get(id)))
    # print(unaccounted_goods)
    print_report(unaccounted_goods, 'Неучтенный товар')
    
# Пополнение
def replenishment():
    # fullness = int(input('Введите процент наполнености: '))
    fullness = 50
    replenishment_goods = {}
    for id in stock.keys():
        find_id = id
        sum_id = 0
        for item in addresses.values():
            if find_id in item.keys():
                sum_id += item[find_id]
        if (stock.setdefault(id,0) - warehouse.setdefault(id,0)) < sum_id*(fullness/100):
            replenishment_goods[id] = sum_id - (stock.get(id) - warehouse.get(id))
    # print(replenishment_goods)
    print_report(replenishment_goods, 'Количество для пополнения')




anomaly_of_stock()
# replenishment()
# unaccounted_goods()
