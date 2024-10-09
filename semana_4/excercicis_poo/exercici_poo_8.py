'''Ejercicio 8

Crear una clase Cálculos con un constructor por defecto (sin parámetros) que permita realizar varios cálculos sobre números enteros.
Crear un método llamado factorial() que permita calcular el factorial de un entero.
Crear un método llamado suma() que permita calcular la suma de los primeros n enteros 1 + 2 + 3 + .. + n.
Crear un método llamado testPrimo() en la clase Cálculo para comprobar si un número es primo. El resultado será True o False.
Crear un método llamado testPrimos() que permita comprobar si dos números son primos entre sí.
Crear un método tablaMult() que cree y muestre la tabla de multiplicación de un número entero dado. A continuación, crear un método allTablesMult() para mostrar todas las tablas de multiplicación de enteros 1, 2, 3, ..., 9.
Crear un método listDiv() que obtenga todos los divisores de un entero dado en una nueva lista llamada Ldiv.'''


class Calculos:
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)

    def suma(self, n):
        return sum(range(1, n+1))

    def test_primo(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def test_primos(self, a, b):
        return self.test_primo(a) and self.test_primo(b)

    def tabla_mult(self, num):
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")

    def all_tables_mult(self):
        for i in range(1, 10):
            self.tabla_mult(i)

    def list_div(self, num):
        return [i for i in range(1, num+1) if num % i == 0]


calculos = Calculos()
print("Factorial de 5:", calculos.factorial(5))
print("Suma de los primeros 5 números:", calculos.suma(5))
print("¿Es primo 7?", calculos.test_primo(7))
print("¿Son primos 7 y 11?", calculos.test_primos(7, 11))
calculos.tabla_mult(5)
calculos.all_tables_mult()
print("Divisores de 12:", calculos.list_div(12))
