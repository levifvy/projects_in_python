'''def remoult(llista):

    resultat = llista[:]
    posicio = 0
    final = []

    while posicio < len(resultat):
        ultcar = resultat[posicio].strip(resultat[posicio][0])
        final.append(ultcar)
        posicio += 1

    return final

llista = ['hola','com', 'estàs']

print(remoult(llista))'''
#----------------------
def nofirst(l):
    resultat = []
    for element in l:
        resultat.append(element[1:len(element)])
    return resultat

original = ['hola','com', 'estàs', 'pink floyd']

resultado = nofirst(original)
#print(f"La lista original es {original} i la modificada es {resultado}")
print(resultado)