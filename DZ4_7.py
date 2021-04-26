def f_g(num):
    count = 1
    while count <= num:
        yield count
        count += 1
i = 1
my_fif = []
for el in f_g(5):
    if i > 15:
        break
    else:
        my_fif.append(el)
        i += 1
print(my_fif)
