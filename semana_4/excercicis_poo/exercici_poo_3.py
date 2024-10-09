'''Ejercicio 3
Escribir una clase en Python llamada circulo que contenga un radio, con un método que devuelva el área y otro que devuelva el perímetro del círculo.'''

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio

circulo = Circulo(7)
print("Área del círculo:", circulo.area())
print("Perímetro del círculo:", circulo.perimetro())
