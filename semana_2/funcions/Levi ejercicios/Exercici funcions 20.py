def remoult(llista):

    resultat = llista[:]
    posicio = 0
    final = []
  
    while posicio < len(resultat): 
        cadena_invertida = ""
        contador = len(resultat[posicio]) -1
        
        while contador >= 0:
            cadena_invertida += resultat[posicio][contador]
            contador -= 1
        
        final.append(cadena_invertida)
        posicio += 1
    
    return final

#llista = ['hola','com', 'estàs']

llista = input("Ingresa, una lista : ")

print(remoult(llista))