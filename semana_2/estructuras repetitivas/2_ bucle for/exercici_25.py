'''25. Fes un programa que ens digui si un número sencer és primer o no (amb un bucle for in)'''

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

number = int(input("Introduce un número: "))

print(f"El número {number} {'es primo' if is_prime(number) else 'no es primo'}.")
