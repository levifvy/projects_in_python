'''
3. Cerca de caràcters (count, index, find):
Escriu un programa que demani una cadena i un caràcter. El programa ha de mostrar 
quantes vegades apareix el caràcter en la cadena, la seva primera aparició i la seva última 
aparició. 
Entrada:'supercalifragilistico', 'i' 
Sortida esperada: 
El caràcter 'i' apareix 3 vegades. 
La seva primera aparició és a la posició 7. 
La seva última aparició és a la posició 17. 
'''
cadena = input("Ingresa una cadena: ")
caracter = input("Ahora ingresa un caracter: ")
print("")

concatenado = ''.join([cadena,", ",caracter])
print("Entrada: ", concatenado)
print("")

conteo = cadena.count(caracter)
print(f"El caràcter {caracter} apareix {conteo} vegades.")

primera_posicio = cadena.find(caracter)
print(f"La seva primera aparició és a la posició {primera_posicio}.")

ultima_posicio = cadena.rfind(caracter)
print(f"La seva última aparició és a la posició {ultima_posicio}.")

print("")