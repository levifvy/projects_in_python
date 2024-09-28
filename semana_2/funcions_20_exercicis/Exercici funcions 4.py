'''4. Funció que pren com a paràmetre una llista de números i retorna la suma dels cubs
dels seus elements.'''

def sumacubos(llista):

    resultat = llista[:]
    sumatorio = 0

    for element in resultat:
        sumatorio = sumatorio + (element**3)

    return sumatorio

llista = [11,13,1,25]

print(sumacubos(llista))