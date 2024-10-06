''' 14.Calcular la taula de multiplicar d'un número entre 1 i 9 '''

def multiplication_table(number):
    if 1 <= number <= 9:
        for i in range(1, 11):
            print(f"{number} x {i} = {number * i}")
    else:
        print("Número fuera de rango. Introduce un número entre 1 y 9.")

multiplication_table(5)
