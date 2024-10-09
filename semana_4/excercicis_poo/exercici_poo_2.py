''' Ejercicio 2
Escribir una clase en Python llamada rectangulo que contenga una base y una altura, y que contenga un método que devuelva el área del rectángulo. '''

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

rectangulo = Rectangulo(10, 5)
print("Área del rectángulo:", rectangulo.area())
