class Transport(object):
    name = ''
    max_speed = 0
    mileage = 0

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def get_information(self):
        print(f"Название автомобиля: {self.name}. Скорость: {self.max_speed}. Пробег: {self.mileage}")

class Autobus(Transport):
    seat_capacity = 50

    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    def seating_capacity (self):
        return f"Вместимость одного автобуса {self.name} {self.seat_capacity} пассажиров"
    

reno_bus = Autobus("Renaul Logan", 180, 12)
print(reno_bus.seating_capacity())
