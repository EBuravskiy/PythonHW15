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

autobus = Transport("Renaul Logan", 180, 12)
autobus.get_information()