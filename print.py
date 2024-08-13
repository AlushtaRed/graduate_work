def print_report(report, name):
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
            

    print(f'Артикул   Наименование{(max_len- 11)*" "} {name}    Общий запас   На Складе')
    for id,quantity in report.items():
        print(f'{id}  {article_database.get(id)}{((max_len+1)-len(article_database.get(id)))*" "} {quantity}{(len(name)+(len_report-len(str(report.get(id)))))*" "}{stock.get(id)}{(10 +(len_stock-len(str(stock.get(id)))))*" "}{warehouse.get(id)} ')
