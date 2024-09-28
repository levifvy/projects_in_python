'''2. Funció que pren com a paràmetre una llista de números i retorna la suma dels seus
elements.'''
# def suma(llista):

#     resultat = llista[:]
#     sumatorio = 0

#     for element in resultat:
#         sumatorio = sumatorio + element

#     return sumatorio

# llista = [5,4,3,2,1]

# print(suma(llista))

def suma(llista):

    resultat = llista[:]
    sumatorio = 0

    for element in resultat:
        sumatorio = sumatorio + element

    return sumatorio

llista = [5,4,3,2,1]

print(suma(llista))
