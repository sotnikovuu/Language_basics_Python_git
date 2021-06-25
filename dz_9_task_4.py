#  Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, 'поехал(а)!')

    def stop(self):
        print(self.name, 'остановился(ась)!')

    def turn(self, direction):
        print(self.name, 'повернул(а)', self.direction)

    def show_speed(self):
        print('Текущая скорость:', self.speed)

    def show_name(self):
        print('Марка машины:', self.name)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Осторожно, превышение скорости!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Осторожно, превышение скорости!')


class PoliceCar(Car):
    pass


sport_car = SportCar(1800, 'Синий', 'Лада', False)
town_car = TownCar(80, 'Красный', 'МиниКупер', False)
work_car = WorkCar(70, 'Белый', 'Газель', False)
police_car = PoliceCar(120, 'Серый', 'Автозак', True)

sport_car.show_name()
sport_car.show_speed()
print()
town_car.show_name()
town_car.go()
town_car.show_speed()
town_car.stop()
print()
work_car.show_name()
work_car.go()
work_car.show_speed()
print()
police_car.show_name()
police_car.go()