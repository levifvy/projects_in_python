'''6. Divisió de cadenes (split, partition):
Escriu un programa que demani a l'usuari una frase llarga i una paraula de divisió. 
El programa ha de dividir la frase utilitzant 'partition' i després mostrar la llista de paraules utilitzant 'split'. 
Entrada: 'A mi m'agrada la pizza, i també la pasta', 'pizza' 
Sortida esperada: 
Partició de la frase: ('A mi m'agrada la ', 'pizza', ', i també la pasta') 
Llista de paraules: ['A', 'mi', "m'agrada", 'la', 'pizza,', 'i', 'també', 'la', 'pasta'] 
'''

entrada = input("ingresa una frase y despues de una coma una palabra de esta frase: ")

frase, separador, palabra = entrada.rpartition(',')
# recorte = entrada.rpartition(',')
# frase = recorte[0]
# palabra = recorte[2]

resultado = frase.partition(palabra)
llista_paraulas = frase.split(' ')
print(f'Partició de la frase: {resultado}')
print(f'Llista de paraules: {llista_paraulas}')