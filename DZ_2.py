n = int(input('Введите числа: '))
number_list = []
for i in range(0, 9):
    ele = int(input())
    number_list.append(ele)
if len(number_list) % 2 == 0:
    i = 0
    while i < len(number_list):
        el = number_list[i]
        number_list[i] = number_list[i + 1]
        number_list[i + 1] = el
        i += 2
else:
    i = 0
    while i < len(number_list) - 1:
        el = number_list[i]
        number_list[i] = number_list[i + 1]
        number_list[i + 1] = el
        i += 2
print(number_list)