goods = []
while input('Хотите ввести товар? Введите да/нет: ') == 'да':
    number = int(input('Укажите номер товара: '))
    specifications = {}
    while input('Хотите ввести характеристики продукта? да/нет: ') == 'да':
        specifications_key = input('Введите характеристику товара: ')
        specifications_features = input('Введите особенности товара: ')
        specifications[specifications_key] = specifications_features
    goods.append(tuple([number, specifications]))
print(goods)
analitics = {}
for good in goods:
    for specifications_key, specifications_features in good[1].items():
        if specifications_key in analitics:
            analitics[specifications_key].append(specifications_features)
        else:
            analitics[specifications_key] = [specifications_features]
print(analitics)

