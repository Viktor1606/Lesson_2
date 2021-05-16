class StoreMashines:

    def __init__(self, name, prise, quantity, number_of_lists, *args):
        self.name = name
        self.prise = prise
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.prise, 'Колличество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.prise} колличество{self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование: ')
            unit_p = int(input(f'Введите цену за ед: '))
            unit_q = int(input('Введите колличество:'))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Колличество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - E, продолжение - R')
        q = input(f'-->')
        if q == 'E' or q == 'e':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход:'
        else:
            return StoreMashines.reception(self)

class Printer(StoreMashines):
    def to_print(self):
        return f'to print smth {self.numb} times'

class Scanner(StoreMashines):
    def to_scan(self):
        return f'to scan smth {self.numb} times'

class Copier(StoreMashines):
    def to_copier(self):
        return f'to copier smth {self.numb} times'

unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())