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