
'''6. Funció que pren com a paràmetre una llista de números i retorna el seu valor màxim'''
# def maximo(llista):

#     resultat = llista[:]

#     return max(resultat)

# llista = [4,3,2,1,8]

# print(maximo(llista))

#--------------------------------
def maximo(llista):
    resultat = llista[:]
    maxim = resultat[0]
    for num in resultat[1:]:
        if num > maxim:
            maxim = num

    return maxim

llista = [-11,13,1,25]

print(maximo(llista))