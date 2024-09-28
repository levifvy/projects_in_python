import archivo_ayuda

llista_de_prueba = ["las", "clases","de","python","son","geniales"]
lista_numeros = [1,2,3,4,5,6,7,8,9]
lista_majuscules = ["MONTANYA","GERONIMO","UNIVERSO","LIDER"]
cadena = "madrito"

resultat = archivo_ayuda.inversio(llista_de_prueba)
resultat2 = archivo_ayuda.revertir(lista_numeros)
resultat3 = archivo_ayuda.revertir(llista_de_prueba)
resultat4 = archivo_ayuda.convertir_minuscules(lista_majuscules)
resultat5 = archivo_ayuda.concatenacio_caracteres(llista_de_prueba)


print(resultat5)
print(llista_de_prueba)
print(cadena[len(cadena)-1])
print(cadena[0:len(cadena)-2])