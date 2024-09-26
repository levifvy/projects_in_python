'''9. Funció que pren com a paràmetre una llista de números i retorna una altra llista amb
els elements en posició senar.
'''
'''def possenar(llista):

    resultat = llista[:]
    posicionsparells = []
    posicio = 0

    while posicio < len(resultat):
        if posicio % 2 != 0:
            posicionsparells.append(resultat[posicio])
        posicio += 1

    return posicionsparells

llista = [5,4,3,2,1]

print(possenar(llista))'''

#-----------------------

'''def possenar(llista):

    resultat = llista[:]
    posicionsinparells = []

    for posicio in range(1,len(resultat),2):
        posicionsinparells.append(resultat[posicio])

    return posicionsinparells

llista = [5,4,3,2,1]

print(possenar(llista))'''

#-------------------------
def posparell(llista):

    resultat = llista[:]
    posicionsparells = []

    for posicio in range(len(resultat)):
        if posicio % 2 == 1:
            posicionsparells.append(resultat[posicio])

    return posicionsparells

llista = [5,4,3,2,1]

print(posparell(llista))
