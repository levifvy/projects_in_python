'''11. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb la
longitud de cadascuna de les cadenes que formen la llista.
'''

def caracters(llista):

    longituds = []

    for i in llista:
        longituds.append(len(i))
    return(longituds)

llista = ['hola','com','estàs']

print(caracters(llista))

#----------------------
# def caracters(llista):

#     longituds = []

#     for posicio in range(len(llista)):
#         longituds.append(llista(len[posicio]))
#     print(longituds)

# llista = ['hola','com','estàs']

# caracters(llista)