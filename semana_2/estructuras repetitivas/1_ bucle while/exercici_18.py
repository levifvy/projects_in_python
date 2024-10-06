'''18. Escriure un programa que demani N números i en digui quin és el més gran i quin és el més petit i la posició en què van ser llegits cadascun.'''

def find_max_min_positions():
    n = int(input("¿Cuántos números vas a ingresar?: "))
    numbers = []
    
    for i in range(n):
        number = int(input(f"Ingresa el número {i+1}: "))
        numbers.append(number)
    
    max_num = max(numbers)
    min_num = min(numbers)
    
    print(f"El número más grande es {max_num}, ingresado en la posición {numbers.index(max_num) + 1}.")
    print(f"El número más pequeño es {min_num}, ingresado en la posición {numbers.index(min_num) + 1}.")


find_max_min_positions()
