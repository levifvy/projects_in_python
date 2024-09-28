'''7. Funció que pren com a paràmetre una llista de números i retorna la llista en ordre
invertit.'''
# def revertir(llista):
#     resultat = llista[:]
#     resultat.sort(reverse=True)
#     return resultat
# llista = [6,4,8,9,10]
# print(revertir(llista))

#------------------------
def revertir(llista):
    resultat = llista[:]
    resultat.reverse()
    return resultat

llista = [6,4,8,9,10]

print(revertir(llista))