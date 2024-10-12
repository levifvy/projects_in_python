'''2. Contar el número de veces que aparece la letra 'a' en una cadena'''

# Primera forma:
# cadena = "La vaca es buena, porque da leche blanca"
# contador = 0
# for letra in cadena:
#     for i in letra:
#         if i == ('a'):
#             contador += 1
# print (contador)
#--------------------------------------------------

def contar_letras_a(cadena):
    return cadena.count('a')

cadena = "La vaca es buena, porque da leche blanca"
cantidad_de_caracteres = contar_letras_a(cadena)
print(cantidad_de_caracteres)
