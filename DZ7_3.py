class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Результат отрицательный')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cell_in_row):
        row = ''
        for i in range(int(self.quantity / cell_in_row)):
            row += f'{"*" * cell_in_row} \\n'
        row += f'{"*" * (self.quantity % cell_in_row)}'
        return row

cells_1 = Cell(12)
cells_2 = Cell(3)
print(cells_1)
print(cells_1 + cells_2)
print(cells_2 - cells_1)
print(cells_2.make_order(12))
print(cells_1.make_order(3))
print(cells_1 / cells_2)