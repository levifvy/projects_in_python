'''19. Volem fer un programa que calculi el factorial d'un número sencer positiu. El factorial d'n es denota amb n!. Sabent que n! = 1 · 2 · 3 · . . . · (n − 1) · n y que 0! = 1, fes un programa que demani el valor de n i mostri per pantalla el resultat de calcular n!.'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

n = int(input("Introduce un número para calcular su factorial: "))
print(f"El factorial de {n} es {factorial(n)}.")
