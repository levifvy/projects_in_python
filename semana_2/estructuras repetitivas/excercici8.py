'''Calcular la mitjana dels números positius llegits'''
acumulador = 0
contador = 0
while True:    
    try:
        numero = int(input("Ingresa un número ó ingresa \"-1\" para terminar: "))
        if numero == -1:
            break
        acumulador = acumulador + numero
        contador +=1
    except ValueError:
        print("Això no és un número vàlid, torna a intentar-ho.")

print("acumulador: ",acumulador)
print("contador: ",contador)
calculo = int(acumulador/contador)
print("Respuesta: ", calculo)
        