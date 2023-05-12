'''
Ejercicio del uso de clase randint del módulo random
'''
from random import randint

class Die:
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        print(f"Un numero aleatorio entre 1 y {self.sides} es: "+str(randint(1,self.sides)))

dado=Die()
for i in range(0,10):
    dado.roll_die()
print("----------------")
dado=Die(10)
for i in range(0,10):
    dado.roll_die()
    print("----------------")
dado=Die(20)
for i in range(0,10):
    dado.roll_die()