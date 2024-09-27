
'''15. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb les
mateixes cadenes ordenades en ordre alfabètic.'''
'''def ordenacio(llista):

    cadenes = sorted(llista)
    print(cadenes)

llista = ['hola','com','estàs']

ordenacio(llista)'''
#--------------------
'''no se recomineda hacer una funcion sin return'''
# def ordenacio(llista):

#    llista.sort()

# llista = ['hola','com','estàs']
# replica = llista[:]
# ordenacio(replica)
# print(replica)
#-------------------------------------------
def ordenaciocadenas(llistacadenas):
    replica = llistacadenas[:]
    replica.sort()
    return replica

llista = ['hola','com','estàs']

resultado = ordenaciocadenas(llista)
print(f"La lista original es {llista}")
print(resultado)
