my_f = open('test.txt', 'w')
line = input('Введите текст \n')
while line:
    my_f.writelines(line)
    line = input('Введите число \n')
    if not line:
        break
    my_f.close()
    my_f = open('test.txt', 'r')
    content = my_f.readline()
    print(content)
    my_f.close()