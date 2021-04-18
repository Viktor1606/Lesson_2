a = 50
b= 55.5
c = (complex(13 + 17))
d = "проста строка"
e = list('просто список')
f = tuple('Просто кортеж')
j = set('изменяемое множество')
h = frozenset('неизменяемое множество')
i = dict(zero = 'zero', apple = 'juise')
k = bool(20), bool(0)
l = bytes(16)
m = type(None)

all_values = [a,b,c,d,e,f,j,h,i,k,l,m]
for i in all_values:
    print(f'{i} is {type(i)}')

