'''14. Funció que pren com a paràmetre una llista de cadenes i retorna una única cadena amb
tots els elements concatenats (Suma d'strings o cadenes).'''

# def ordenacio(llista):

#     cadenes = "".join(llista)
#     return cadenes

# llista = ['hola','com','estàs']

# print(ordenacio(llista))

#-------------
def ordenacio(llista):
    resultado = ""
    for cadena in llista:

        resultado += cadena

    return resultado

llista = ['hola','com','estàs']

print(ordenacio(llista))