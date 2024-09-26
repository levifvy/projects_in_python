def suma(llista):

    resultat = llista[:]
    sumatorio = 0

    for element in resultat:
        sumatorio += (element**2)

    return sumatorio

llista = [11,13,1,25]

print(suma(llista))