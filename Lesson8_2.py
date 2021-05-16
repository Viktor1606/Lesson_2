class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_nyll(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f'Нельзя делить на ноль! ')

div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_nyll(10, 0))
print(DivisionByNull.divide_by_nyll(10, 0.1))
print(div.divide_by_nyll(100, 0))