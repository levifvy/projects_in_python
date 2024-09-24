'''
2-Comptar lletres:
Comptar el número de vegades que surt la lletra 'a' dins d'una cadena de text
'''

cadena = "La vaca es buena, porque da leche blanca"
# print(cadena.count('a'))

contador = 0

for letra in cadena:
    for i in letra:
        if i == ('b'):
            contador += 1
print (contador)