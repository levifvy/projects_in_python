import re

llista = ["2 , 3, hola,24,34.000, hola2 \n", "3,4,hola ,24,   54.000, hola3 \n","3,4,  hola, 24,34.000, hola4 \n","3,4,   hola,  24,34.000,  hola5 \n"]

patro = re.compile("[a-z0-9\\.]+")
resultat = []
subresultat = []
sublista = []
for element in llista:
    
    element = patro.findall(element)
    
    frase = ""
    print(element)
    for paraula in element:
        
        frase = paraula.replace('.','').replace('\n','')
       # print(frase)
    sublista.append(frase)
#print(sublista)
#     resultat.append(sublista)
# print(resultat)