'''Una clase para representar un automovil'''

class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()
    def read_odometer(self):
        print(f"Este automovil tiene {self.odometer_reading} de kilometraje")
    def update_odometer(self,km):
        if km>=self.odometer_reading:
            self.odometer_reading=km
        else:
            print("El odometro no se puede cambiar")
    def increment_odometer(self,km):
        self.odometer_reading+=km
    def fill_tank(self):
        print("El nivel de bencina es bajo, llena el tanque")


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




    
    
