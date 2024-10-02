from datetime import *

class vehiculo:

    def __init__(self, tipo, color, ano, marca, modelo, potencia, matricula):

        self.tipo = tipo
        self.color = color
        self.ano = ano
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.matricula = matricula
    
    def antiguedad(self):

        return datetime.today().year - self.ano
    
    def ITV(self):
        
        if self.antiguedad() > 10:
            return 1
        else:
            return 2
    
    def consumo(self):
        return self.potencia
    
    def __str__(self):
        return f"Es un {self.tipo} marca {self.marca} modelo {self.modelo} ano {self.ano} y color {self.color} con la matricula {self.matricula}"
    

vehiculo1 = vehiculo('coche', 'rojo', 2021, 'BMW', 'Predator', '200', 'ASDLJLSFD')

print(vehiculo1.antiguedad)
print(vehiculo1.consumo)
print(vehiculo1)
print(vehiculo1.ITV())
print(vehiculo1.color)
print(vehiculo1.matricula)
