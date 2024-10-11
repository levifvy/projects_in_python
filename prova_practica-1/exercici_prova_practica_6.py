'''6. Escriu una funció de Python que accepti una cadena i calculi el número de majúscules i minúscules que apareixen a la cadena. La funció retornarà una llista amb dos elements: el número de majúscules i el número de minúscules.

def aparicions(cadena):
..................
..................
..................
return ...........
    
Per exemple,
print(aparicions(“Hola Caracola, a tu bola”)) imprimirà a la pantalla la llista [2, 17] perquè a la cadena hi ha 2 majúscules i 17 minúscules.

NOTA: Els espais o altres caràcters no es consideren majúscules o minúscules.'''

def aparicions(cadena):
    majuscules = 0
    minuscules = 0

    for char in cadena:
        if char.isupper():
            majuscules += 1
        elif char.islower():
            minuscules += 1

    return [majuscules, minuscules]

print(aparicions("Hola Caracola, a tu bola"))  