'''Ejercicio 1 Escribir una clase en python con 2 métodos: get_string y print_string. get_string acepta una cadena ingresada por el usuario y print_string imprime la cadena en mayúsculas.'''

class Cadena:
    def get_string(self):
        self.cadena = input("Introduce una cadena: ")
    
    def print_string(self):
        print(self.cadena.upper())

cadena = Cadena()
cadena.get_string()
cadena.print_string()
