month = int(input('Введите номер месяца: '))
if month <= 12 and month >= 1:
    number = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь", 7: "Июль", 8: "Август",
              9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
    number_list = list(number.values())
    for i, el in enumerate(number_list):
        if i == month-1:
            print(f"Ваш месяц:{number_list[i]} ")
else:
    print("вы ошиблись")
