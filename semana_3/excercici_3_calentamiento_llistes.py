'''   haz un algoritmo que convierta la lista original quitarle'''
#llista = [['hola','pepe','com'],['farola','tierra'],['barcelona','madrid']]

# def no_first_caracter(llista_cadenes):
#     resultat = []
#     for element in llista_cadenes:
#         resultat.append(element[1:len(element)])
#     return resultat

# resultado = []
# for sublista in llista:
#     sub_cadenas = no_first_caracter(sublista)
#     resultado.append(sub_cadenas)

# print(resultado)

#---------------------------------------------------

''' llista_de_llistes = [['hola','pepe','com'],['farola','tierra'],['barcelona','madrid']]

for llista in llista_de_llistes:
    for pos in range(len(llista)):
        llista[pos] = llista[pos][1:]
print(llista_de_llistes)'''

#-----------------

'''llista_de_llistes = [['hola','pepe','com'],['farola','tierra'],['barcelona','madrid']]

for lista in llista_de_llistes:
    for pos in range(len(lista)):
        lista[pos] = lista[pos][1:]
print(llista_de_llistes)'''

#-------------------------
llistadellistesdecadenes = [['hola','pepe','com','estas'],['la','farola','de','laredo']]

resultantllistadellistesdecadenes = []

for llista in llistadellistesdecadenes:
    resultat1 = []
    for cadena in llista:
        #resultat2 = []
        #resultat2.append(cadena[1:])
        resultat1.append(cadena[1:])
    resultantllistadellistesdecadenes.append(resultat1)
    
print(resultantllistadellistesdecadenes)
print(llistadellistesdecadenes)

                         
    
def nofirst(llistadellistesdecadenes):
    resultat = []
    for llista in llistadellistesdecadenes:
        resultat1 = []
        for cadena in llista:
            resultat1.append(cadena[1:])
        resultat.append(resultat1)
    return resultat
    
    
llistadellistesdecadenes = [['hola','pepe','com','estas'],['la','farola','de','laredo']]
print(nofirst(llistadellistesdecadenes))
print(llistadellistesdecadenes)


def quitarprimeraletra(l):
    return [[element[1:] for element in subllista] for subllista in l]

print(quitarprimeraletra(llistadellistesdecadenes))
print(llistadellistesdecadenes)