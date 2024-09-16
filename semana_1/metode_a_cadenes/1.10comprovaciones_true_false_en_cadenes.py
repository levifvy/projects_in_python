# cadena = "la farola de laredo"

# print('La cadena és: {}\n\n\n'.format(cadena))

# print("El caracter i és troba dins de cadena")
# print('i' in cadena)

# print("El caracter i no és troba dins de cadena")
# print('i' not in cadena)

# print("La cadena esta formada NOMÉS per números")
# print(cadena.isdigit())

# print("La cadena esta formada NOMÉS per lletres")
# print(cadena.isalpha()) # els espais no son lletres

# print("La cadena esta formada NOMÉS per números i lletres")
# print(cadena.isalnum())

# print("La cadena esta formada NOMÉS per espais")
# print(cadena.isspace())

# print("La cadena esta escrita en minúscules")
# print(cadena.islower()) # els espais no comptan para aquest criteri

# print("La cadena esta escrita en majúscules")
# print(cadena.isupper())

# print("La cadena comença per l")
# print(cadena.startswith('l'))

# print("La cadena acaba en o")
# print(cadena.endswith('o'))
import math

nom = input("entre el nom: ")

while nom.isalpha() == False:
    nom = input("Entra be el nom sisplau: ")
print("El teu no és " + nom)

cadena = input("Entra el num: ")

def esdecimal(cadena):
    if cadena.count('.') == 1:
        cadena = cadena.replace('.','')
        if essencer(cadena):
            return True
    return False

print(esdecimal())