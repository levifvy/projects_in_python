'''12. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb les
mateixes cadenes en minúscules.'''
def minuscules(llista):

    longituds = []

    for i in llista:
        longituds.append(i.lower())
    print(longituds)

llista = ['HOLA','COM','ESTÀS']

minuscules(llista)

#