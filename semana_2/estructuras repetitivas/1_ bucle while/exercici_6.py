''' 6. Sumar els múltiples de 2 menors a 100'''
numero = 0
acumulador = 0
while numero < 100:
    acumulador = acumulador + numero
    print(numero, end=" ")
    numero+=2
    
print("")
print(acumulador)