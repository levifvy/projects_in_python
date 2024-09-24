'''Sumar les potències de 2 menors a 100'''
potencia = 0
numero = 0
acumulador = 0
while potencia < 100:
    acumulador += potencia
    potencia = (2 ** numero)
    # print(potencia, end=" ") 
    numero +=1 
print("")
print(acumulador)
