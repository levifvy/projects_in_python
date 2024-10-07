'''29.Fer un programa que llegeixi un nombre sencer i escrigui el nombre de xifres que té.'''

def count_digits(number):
    count = 0

    for digit in str(abs(number)):
        count += 1 
    return count

number = int(input("Introduce un número entero: "))
print(f"El número {number} tiene {count_digits(number)} cifras.")

