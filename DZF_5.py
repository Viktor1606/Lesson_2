import sys
res = 0
while True:
    line = input("Введите число или специальный символ & для завершения операции: ")
    tokens = line.split(" ")
    for token in tokens:
        try:
            num = float(token)
            res += num
        except:
            if token == '&':
                print(f"Вы складываете {res}. Программа завершает работу")
                exit(0)
            else:
                print(f"Вы складываете{res}. Ошибка", file=sys.stderr)
                exit(1)
