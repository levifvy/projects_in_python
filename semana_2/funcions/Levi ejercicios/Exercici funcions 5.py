'''5. Funció que pren com a paràmetre una llista de números i retorna el seu valor mínim'''

# def minimo(llista):

#     resultat = llista[:]

#     return min(resultat)

# llista = [4,3,2,1,8]

# print(minimo(llista))

#-------------------------------

def minimo(llista):
    resultat = llista[:]
    minim = resultat[0]
    for num in resultat[1:]:
        if num < minim:
            minim = num

    return minim

llista = [4,3,2,1,8]

print(minimo(llista))