class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._weidtht = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self._weidtht * self.height / 1000
        print(f'Для покрытия дороги необходимо {round(asphalt_mass)} т. массы асфальта')
r = Road(5000, 20)
r.asphalt_mass()