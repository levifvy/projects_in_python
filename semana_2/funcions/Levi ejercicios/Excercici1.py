def odernada(llista):

    resultat = llista[:]
    
    resultat.sort()

    return resultat

llista = [5,4,3,2,1]

print(odernada(llista))