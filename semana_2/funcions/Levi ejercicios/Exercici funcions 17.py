def possenar(llista):

    resultat = llista[:]
    posicionsparells = []
    posicio = 0

    while posicio < len(resultat):
        if posicio % 2 != 0:
            posicionsparells.append(resultat[posicio])
        posicio += 1

    return posicionsparells

llista = ['hola','com', 'estàs']

print(possenar(llista))