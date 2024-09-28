'''18. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb
les mateixes cadenes sense l'últim caràcter.'''

'''def remoult(llista):

    resultat = llista[:]
    posicio = 0
    final = []

    while posicio < len(resultat):
        ultcar = resultat[posicio].rstrip(resultat[posicio][-1])
        final.append(ultcar)
        posicio += 1

    return final

llista = ['hola','com', 'estàs']

print(remoult(llista))'''

#-----------------------
def nolast(l):
    resultat = []
    for element in l:
        resultat.append(element[0:len(element)-1])
    return resultat

original = ['hola','com', 'estàs', 'pink floyd']

resultado = nolast(original)
#print(f"La lista original es {original} i la modificada es {resultado}")
print(resultado)