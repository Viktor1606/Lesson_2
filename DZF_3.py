def my_func(x,y,z):
    seq = [x,y,z]
    total = []
    max_1 = max(seq)
    total.append(max_1)
    seq.remove(max_1)
    max_2 = max(seq)
    total.append(max_2)
    print(sum(total))
my_func(int(input("Введите значение x: ")), int(input("Введите значение y: ")), int(input("Введите значение z: ")))