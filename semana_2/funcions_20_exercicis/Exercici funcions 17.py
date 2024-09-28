'''17. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb
les cadenes que es troben en posició senar'''
'''def possenar(llista):

    resultat = llista[:]
    posicionsparells = []
    posicio = 0

    while posicio < len(resultat):
        if posicio % 2 != 0:
            posicionsparells.append(resultat[posicio])
        posicio += 1

    return posicionsparells

llista = ['hola','com', 'estàs']

print(possenar(llista))'''

#-----------
def senars(x):
    resultat = []
    for posicio in range(1,len(x),2):
        resultat.append(x[posicio])
    return resultat

original = ['hola','com', 'estàs', 'pink floyd','llila','montanya']

resultado = senars(original)
#print(f"La lista original es {original} i la modificada es {resultado}")
print(resultado)