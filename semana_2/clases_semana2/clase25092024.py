

'''def ordenada(llista):
    resultado = llista[:]
    resultado.sort()
    return resultado

conjunto = [8,6,5,3,2,9,4,21,17]

print(ordenada(conjunto))
print(conjunto)'''

#------------------------------------------
'''#A) 
def ordenar(l):
    l.sort()
   
llista = [8,6,5,3,2,9,4,21,17]

llista2 =ordenar(llista) # (No tiene return!!! ---- "None")
print("A", llista2)
print("A", llista)'''

#B)

def ordenar(llista):
    resultat = llista[:]
    resultat.sort()
    return resultat
llista = [8,6,5,3,2,9,4,21,17]
ordenada = ordenar(llista)

print("B original: ", llista)
print("B ordenada: ", ordenada)

