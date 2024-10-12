llista = ["2 , 3, hola,24,34.000, hola2 \n", "3,4,hola ,24,   54.000, hola3 \n","3,4,  hola, 24,34.000, hola4 \n","3,4,   hola,  24,34.000,  hola5 \n"]

reemplazo = llista[:]    
resultat = []
for cadena in reemplazo:
    cadena = cadena.replace(" ","")
    linia = ""
    for element in cadena:
        element = element.replace('.','')
        element = element.replace('\n','')
        linia += element
    resultat.append(linia)
#print (resultat) 

resultat_final = []
for cadena in resultat:
    paraula = cadena.split(',')
    resultat_final.append(paraula)
print (resultat_final) 

    
'''
    frase_limpia = ""
    subresultat = []
    for paraula in cadena:
        frase_limpia += paraula
        #frase_limpia = frase_limpia.replace(',','')
    subresultat.append(frase_limpia)
    resultat_final.append(subresultat)
'''
#print (resultat_final) 

        
        

