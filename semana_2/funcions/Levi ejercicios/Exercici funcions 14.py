def ordenacio(llista):

    cadenes = "".join(llista)
    return cadenes

llista = ['hola','com','estàs']

print(ordenacio(llista))

#-------------
def ordenacio(llista):
    resultado = ""
    for cadena in llista:

        resultado += cadena

    return resultado

llista = ['hola','com','estàs']

print(ordenacio(llista))