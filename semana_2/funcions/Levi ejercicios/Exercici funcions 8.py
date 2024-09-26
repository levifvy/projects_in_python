'''8. Funció que pren com a paràmetre una llista de números i retorna una altra llista
amb els elements en posició parell.'''

# def posparell(llista):

#     resultat = llista[:]
#     posicionsparells = []
#     posicio = 0

#     while posicio < len(resultat):
#         if posicio % 2 == 0:
#             posicionsparells.append(resultat[posicio])
#         posicio += 1

#     return posicionsparells

# llista = [5,4,3,2,1]

# print(posparell(llista))

#-------------------------

'''def posparell(llista):

    resultat = llista[:]
    posicionsparells = []

    for posicio in range(len(resultat)):
        if posicio % 2 == 0:
            posicionsparells.append(resultat[posicio])

    return posicionsparells

llista = [5,4,3,2,1]

print(posparell(llista))'''
#_______________________________

def posparell(llista):

    resultat = llista[:]
    posicionsparells = []

    for posicio in range(0,len(resultat),2):
        posicionsparells.append(resultat[posicio])

    return posicionsparells

llista = [5,4,3,2,1]

print(posparell(llista))