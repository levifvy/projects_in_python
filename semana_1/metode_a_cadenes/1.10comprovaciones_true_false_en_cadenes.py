cadena = "la farola de laredo"

print('La cadena és: {}\n\n\n'.format(cadena))

print("El caracter i és troba dins de cadena")
print('i' in cadena)

print("El caracter i no és troba dins de cadena")
print('i' not in cadena)

print("La cadena esta formada NOMÉS per números")
print(cadena.isdigit())

print("La cadena esta formada NOMÉS per lletres")
print(cadena.isalpha()) # els espais no son lletres

print("La cadena esta formada NOMÉS per números i lletres")
print(cadena.isalnum())

print("La cadena esta formada NOMÉS per espais")
print(cadena.isspace())

print("La cadena esta escrita en minúscules")
print(cadena.islower()) # els espais no comptan para aquest criteri

print("La cadena esta escrita en majúscules")
print(cadena.isupper())

print("La cadena comença per l")
print(cadena.startswith('l'))

print("La cadena acaba en o")
print(cadena.endswith('o'))