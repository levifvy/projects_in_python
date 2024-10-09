'''Ejercicio 6
Escribe una clase de Python, y define dos métodos que devuelvan el área del cuadrado y el perímetro.'''

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return 4 * self.lado

cuadrado = Cuadrado(4)
print("Área del cuadrado:", cuadrado.area())
print("Perímetro del cuadrado:", cuadrado.perimetro())
