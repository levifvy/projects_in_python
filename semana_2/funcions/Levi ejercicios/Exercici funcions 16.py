'''16. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb
les cadenes que es troben en posició parell.'''

# def posparell(llista):

#     resultat = llista[:]
#     posicionsparells = []
#     posicio = 0

#     while posicio < len(resultat):
#         if posicio % 2 == 0:
#             posicionsparells.append(resultat[posicio])
#         posicio += 1

#     return posicionsparells

# llista = ['hola','com', 'estàs']

# print(posparell(llista))
#-----------------------------------

# def parelles(x):
#     resultat = []
#     for posicio in range(len(original)):
#         if posicio % 2 == 0:
#             resultat.append(original[posicio])
#     return resultat

# original = ['hola','com', 'estàs', 'pink floyd']

# resultado = parelles(original)
# #print(f"La lista original es {original} i la modificada es {resultado}")
# print(resultado)
#-----------
# def parelles(x):
#     resultat = []
#     for posicio in range(0,len(original),2):
#         resultat.append(original[posicio])
#     return resultat

def cadenes_posicio_parelles(llista):
    resultat = []
    for posicio in range(0,len(llista),2):
        resultat.append(llista[posicio])
    return resultat

original = ['hola','com', 'estàs', 'pink floyd']

resultado = cadenes_posicio_parelles(original)
#print(f"La lista original es {original} i la modificada es {resultado}")
print(resultado)