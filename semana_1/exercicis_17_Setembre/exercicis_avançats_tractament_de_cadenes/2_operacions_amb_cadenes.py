''' 2. Operacions amb cadenes (+, *, \n):
Escriu un programa que demani a l'usuari una frase i un número. El programa ha de concatenar la frase amb una versió repetida de la mateixa frase el número de vegades indicat, amb cada repetició en una línia nova. 
Entrada: 'Hola, món!', 3 
Sortida esperada: 
Hola, món!
Hola, món!
Hola, món!
'''
# frase = input("Ingresa una frase: ")
# numero = input("Ahora ingresa un numero: ")
# print("")

# numero_valido = (int) (numero)

# concatenado = ''.join([frase,", ",numero])
# print("Entrada: ", concatenado)
# print("")

# contador = 0
# while contador < numero_valido:
#     contador+=1
#     print(frase)

# print("")


'''# Una altre manera'''

entrada = input('Ingresa una frase y un número, separados por una coma: ')

lista = entrada.split(',')
cadena_repetida = lista[0] + "\n"
repeticiones = int(lista[1])
print(cadena_repetida * repeticiones)


