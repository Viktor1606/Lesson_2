def my_f(a):
    sep = a.split(' ')
    total = []
    for i in sep:
        str_element = str(i)
        first_letter = str_element[:1].upper()
        name = first_letter + str_element[1:]
        total.append(name)
    return total
print(my_f("сергей анатольевич"))