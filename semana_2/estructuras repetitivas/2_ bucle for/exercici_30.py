'''30.Fer un programa que llegeixi un nombre sencer positiu i escrigui la suma de les seves xifres.'''

def sum_of_digits(number):
    return sum(int(digit) for digit in number)

number = input("Introduce un número entero positivo: ")

print(f"La suma de las cifras de {number} es {sum_of_digits(number)}.")
