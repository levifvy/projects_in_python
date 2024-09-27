'''20. Funció que pren com a paràmetre una llista de cadenes i retorna una altra
llista amb les mateixes cadenes invertides.'''

'''def remoult(llista):

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

print(remoult(llista))'''
#-----------------------------------
# en la consola python luego dir(str)

# def inversio(l):
  
#     invertida = []
#     for element in l:
#         temp = ""
#         for char in element:
#             element = char + element
#         invertida.append(element)
#     return invertida

# original = ['hola','com', 'estàs', 'pink floyd']

# resultado = inversio(original)
# #print(f"La lista original es {original} i la modificada es {resultado}")
# print(resultado)
# cadena = 'murder'
# invertida = ''
# for element in cadena:
#     invertida = element + invertida
# print(invertida)

#------------------
def inversion_cadena(c):
    resultat = ''
    for char in c:
        resultat = char + resultat
    return resultat

def inversio(l):
    invertida = []
    for element in l:
        invertida.append(inversion_cadena(element))
    return invertida

original = ['hola','com', 'estàs','pink floyd']
print(inversio(original))