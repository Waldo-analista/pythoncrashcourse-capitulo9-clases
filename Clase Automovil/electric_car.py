'''Set de clases que pueden representar un automovil electrico'''
from car_separate import Car


class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()

    def fill_tank(self):
        print("Este automovil no necesita bencina")

class Battery:
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def get_range(self):
        if self.battery_size==70:
            self.range=240
        elif self.battery_size==85:
            self.range=270
        print(f"Este automovil puede recorrer {self.range} con la bateria completa de {self.battery_size}")
    def upgrade_battery(self):
        if self.battery_size!=85:
            self.battery_size=85
    def describe_battery(self):
        print(f"Este automovil tiene una bateria de tamaño {self.battery_size}")



