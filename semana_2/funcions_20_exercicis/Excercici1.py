
'''1. Funció que pren com a paràmetre una llista de números i retorna una altra llista
ordenada. '''
def odernada(llista):
    resultat = llista[:]
    resultat.sort()
    return resultat
llista = [5,4,3,2,1]

print(odernada(llista))