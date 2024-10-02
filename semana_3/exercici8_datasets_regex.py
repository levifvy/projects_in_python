import io
import re

patro = re.compile("[A-Za-z0-9 \\-_]+")

arxiu = io.open("C:\\Users\\Alumne_mati1\\Downloads\\user_behavior_dataset.csv","r",encoding='utf-8')

llistedecadenes = arxiu.readlines()

matriz = []
sublongituds = []
longituds = []
subcadena = ''

for cadena in llistedecadenes:
    matriz.append(patro.findall(cadena))
    #if len(patro.findall(cadena)) != 20:
    #longituds.append(patro.findall(cadena))
    for element in cadena:
        subcadena = element.replace(' ','')
        print(subcadena, end='')
        #element.split(',')
    #sublongituds.append()
        #print(element.split(','),end='')

        

print(type(subcadena))

# print(type(sublongituds))

# print(sublongituds)
#print(longituds)
