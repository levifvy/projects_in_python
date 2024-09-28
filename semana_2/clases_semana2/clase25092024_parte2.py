'''comptadors = [0,0,0,0,0]

for element in comptadors:
    element +=1   
print(comptadors)'''

'''for posicio in range(len(comptadors)):
    comptadors[posicio] += 1
    
print(comptadors)'''

# comptador[posicio] es el valor de comptadors en la posicio posicio


'''comptadors = [0,0,0,0,0]

resultat = []

for valor in comptadors:
    valor +=1   
    resultat.append(valor)
    print(id(valor))
    print(id(comptadors[0]))
print(resultat)
print(comptadors)'''

# codeskulptor3: https://py3.codeskulptor.org/#user309_aEiDfmGmx7_0.py

#__________________________________

'''cadena = "murder"

resultat = " "
for car in cadena:
    resultat += 'a'
print(resultat)

for pos in range(len(cadena)):
    # cadena[pos] += "a"
    resultat += cadena[pos]
print(resultat)'''

#____________________________
'''
comptadors = [0,0,0,0,0]

print(comptadors)
print(id(comptadors))
print("")
for posicio in range(len(comptadors)):
    comptadors[posicio] += 10
print(comptadors)
print(id(comptadors))

print("")
for posicio in range(len(comptadors)):
    comptadors[posicio] = 1

print(comptadors)
print(id(comptadors))'''

#---------------------------------------------------
'''comptadors = [1,2,3,4,5]

print(comptadors[0:3])
print(type(comptadors[0:3]))
print(comptadors[3:])
print(comptadors[:3])
print(comptadors[0:len(comptadors)])
print(comptadors[:])
print(comptadors)'''

#----------------------------------------------
'''a = ['hola','pollo']
b = a[:]
a.append('saltarin')

print(a)
print(b)
print(a,id(a))
print(b,id(b))

print('****************')
sa = 'hola'
sb = sa
sa = 'saltarin'
print(sa,id(sa))
print(sb,id(sb))
print("")'''

#------------------------------------------------
'''llista = [1,2,3,4,5]
print("id: ",id(llista))
llista.append(5)
print("id: ",id(llista))

# llista = llista.append(5) esta linea dara none (en numero, es mejor trabajar solo con la linea anterior)

print(llista)'''

cadena = ' ho la'

print("id: ",id(cadena))

cadena.replace(" ","")

print(cadena)
print("id: ",id(cadena))
print("id cadena.replace(" ",""): ",id(cadena.replace(" ","")))
cadena = cadena.replace(" ","")

print("id: ",id(cadena))

print(cadena)
