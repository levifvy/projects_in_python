''' 3. Cerca de caràcters (count, index, find):
Escriu un programa que demani una cadena i un caràcter. El programa ha de mostrar quantes vegades apareix el caràcter en la cadena, la seva primera aparició i la seva última aparició. 

Entrada:'supercalifragilistico', 'i' 

Sortida esperada: 
El caràcter 'i' apareix 3 vegades. 
La seva primera aparició és a la posició 7. 
La seva última aparició és a la posició 17. 
'''
entrada = input("Ingresa una cadena y un caracter separados por una coma: ")
extraccion = entrada.split(',')

cadena = extraccion[0]
caracter = extraccion[1]
print("")

conteo = cadena.count(caracter)
print(f"El caràcter {caracter} apareix {conteo} vegades.")

primera_posicio = cadena.find(caracter)
print(f"La seva primera aparició és a la posició {primera_posicio}.")

ultima_posicio = cadena.rfind(caracter)
print(f"La seva última aparició és a la posició {ultima_posicio}.")

print("")