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
        
        return datetime.today().year -self.ano
    
    
    def ITV(self):
        
        if   self.antiguedad() > 10:
            
            return 1
        
        else:
            
            return 2
       
        
    def consumo(self):
        
        return self.potencia
    
    def __str__(self):
        
        return f"Es un {self.tipo} marca {self.marca} modelo {self.modelo} del ano {self.ano} y color {self.color} con matricula {self.matricula}"
     
    
        
vehicle1 = vehiculo( 'coche', 'rojo', 2021, 'BMW', 'Predator', '200','ASDLJLSFD')

print(vehicle1.antiguedad())

print(vehicle1.consumo())

print(vehicle1)

print(vehicle1.ITV())

print(vehicle1.color)

print(vehicle1.matricula)