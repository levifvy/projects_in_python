def remoult(llista):

    resultat = llista[:]
    posicio = 0
    final = []

    while posicio < len(resultat):
        ultcar = resultat[posicio].rstrip(resultat[posicio][-1])
        final.append(ultcar)
        posicio += 1

    return final

llista = ['hola','com', 'estàs']

print(remoult(llista))