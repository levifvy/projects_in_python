'''Ejercicio 9
Sigue los pasos:

Crea una clase, Triangulo. Su método __init__() debe tomar como argumentos self, angle1, angle2 y angle3. Asegúrate de establecerlos apropiadamente en el cuerpo del método __init__().
Crea una variable llamada numero_de_lados y ponla igual a 3.
Crea un método llamado comprobar_angulos. La suma de los tres ángulos de un triángulo debe devolver True si la suma de ángulo1, ángulo2 y ángulo3 es igual a 180, y False en caso contrario.
Crea una variable llamada mi_triangulo y hazla igual a una nueva instancia de tu clase Triangulo. Pásale tres ángulos que sumen 180 (por ejemplo, 90, 30, 60).
Imprime mi_triangulo.numero_de_lados e imprime mi_triangulo.comprobar_angulos().'''

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
