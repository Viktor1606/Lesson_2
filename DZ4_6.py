from  itertools import count
from itertools import cycle

def count_f (start_num, stop_num):
    for el in count(start_num):
        if el > stop_num:
            break
        else:
            print(el)
def cycle_f (my_list, iteration):
    i = 0
    it = cycle(my_list,)
    while i < iteration:
        print(next(it))
        i += 1
count_f(start_num= int(input("Введите число: ")), stop_num= int(input("Введите число: ")))
cycle_f(my_list=[1,2], iteration= int(input("Введите итерацию: ")))