from main import load_json,save_json
import json
addresses = {'1-1L': {'10073940': 40,'10072745': 52}, '1-1R': {'10072745': 52}, '1-2L': {'10073940': 30}, '1-2R': {'10072630': 68}, '1-3L': {'15163427': 56}, '1-3R': {},
             '1-4L': {}, '1-4R': {}, '1-5L': {'10072745': 52}, '1-5R': {'15163427': 56}, '2-1L': {'10073940': 40}, '2-1R': {}, '2-2L': {'10073940': 40}, '2-2R': {},
             '2-3L': {}, '2-3R': {'10072745': 52}, '2-4L': {}, '2-4R': {}, '2-5L': {}, '2-5R': {}}

article_database = {'10073940':'Штукатурка Ротбанд 30 кг', '10072745':'ГСП 12,5 мм влаг.',
                    '15163427':'Пескобетон Axton 30 кг','18478820':'Пескобетон 40 кг',
                    '10072681':'ГСП 12,5 мм стандарт','10072630':'ГСП 9,5 мм влаг.', '12757510':'Грунтовка Ceresit 10/17',
                    '12756884':'Грунтовка Кнауф 10 л', '123':'Тест'}

warehouse = {'10073940':4000, '10072745':520,
             '15163427':560,'18478820':240,
            '10072681':520,'10072630':340,
            '12757510':360, '12756884':115,
            '123':12}

stock = {'10073940':440, '10072745':520,
             '15163427':560,'18478820':240,
            '10072681':520,'10072630':340,
            '12757510':420, '12756884':148}
def print_report(report, name):
    # article_database = load_json('article_database.json')
    # warehouse = load_json('warehouse.json')
    # stock = load_json('stock.json')
    len_stock = 0
    len_warehouse = 0
    len_report = 0
    max_len = 0

    for id in report.keys():
        if len(str(report.get(id)))> len_report:
            len_report = len(str(report.get(id)))
    
    for id in report.keys():
        if len(article_database.get(id)) > max_len:
            max_len = len(article_database.get(id))
    for id in report.keys():
        if len(str(stock.get(id)))> len_stock:
            len_stock = len(str(stock.get(id)))        
            

    print(f'Артикул   Наименование{(max_len- 11)*" "} {name}   Общий запас  На Складе')
    for id,quantity in report.items():
        print(f'{id}  {article_database.get(id)}{((max_len+1)-
        len(article_database.get(id)))*" "} {quantity}{(len(name)+(len_report-
        len(str(report.get(id)))))*" "}{stock.get(id)}{(10 +(len_stock-
        len(str(stock.get(id)))))*" "}{warehouse.get(id)} ')
