# Реализовать класс Road(дорога).
# определить атрибуты: length(длина), width(ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв.метра дороги асфальтом, толщиной в
# 1 см * число см толщины полотна;
# проверить работу метода.
#
# Например: 20
# м * 5000
# м * 25
# кг * 5
# см = 12500т.

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._weight = 43
        self._thickness = 7


    def mass_calculation(self):
        mass = self._length * self._width * self._weight * self._thickness
        print(mass, 'кг')


mass_road = Road(20, 100)
mass_road.mass_calculation()

