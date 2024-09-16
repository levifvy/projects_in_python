#Troballa de cadenas dins de cadenes

#Comptar els caracters d'una cadena

# Metodo Count
cadena = "Quants caracteres tincs?"
# print(cadena.count('a'))
# print(cadena.count('A'))

# # Metode Index: 
# # #troba la posiciò on trobem un caracter
# #tenint en compta que la primera posicio es la zero
# #aquest metode no compta totes les caracters, sino nomes la primera ocurreça
# #cuando no trobe el caracter dona error
# print(cadena.index('a'))
# #reverse index: la primera aparicio desde el final
# print(cadena.rindex('a'))

#  # Metode Find: 
#  # si no encuentra el caracter donara -1
# print(cadena.find('a'))
# print(cadena.find('A'))
# # reverse find: la primera aparicio desde el final
# print(cadena.rfind('a'))

for posicio in cadena:
    print(posicio.index('a'))