'''10. Funció que pren com a paràmetre una llista de números i retorna una altra llista amb
el número de dígits de cada element.'''

def digits(llista):

    resultat = llista[:]
    numdigits = []
    posicio = 0

    while posicio < len(resultat):
        numdigits.append(len(str(resultat[posicio])))
        posicio += 1

    return numdigits

llista = [105,40,312,2224,1112]

print(digits(llista))

#---------------

# def digits(llista):

#     resultat = llista[:]
#     numdigits = []

#     for num in resultat:
    
#         num =str(num).replace("-","")
#         numdigits.append(len(num))
        

#     return numdigits

# llista = [105,40,312,2224,1112]

# print(digits(llista))