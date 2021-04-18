rating = int(input('Введите номер рейтинга: '))
number_list = [7, 4, 3, 2]
a = number_list.count(rating)
for element in number_list:
    if a > 0:
        i = number_list.index(rating)
        number_list.insert(i+a, rating)
        break
    else:
        if rating > element:
            b = number_list.index(element)
            number_list.insert(b, rating)
            break
        elif rating < number_list[len(number_list) - 1]:
            number_list.append(rating)
print(number_list)