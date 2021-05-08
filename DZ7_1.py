class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
       for i in range(len(self.my_list)):
           for i_2 in range(len(other.my_list[i])):
               self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
       return Matrix.__str__(self)

m = Matrix([
    [2, 3, -5],
    [2, 5, 2],
    [6, -1, 1],
    [2, 8, -1]
    ])
new_m = Matrix([
    [5, -7, 8],
    [2, 3, -9],
    [1, 1, 1],
    [6, -4, 7]
    ])


print(m.__add__(new_m))