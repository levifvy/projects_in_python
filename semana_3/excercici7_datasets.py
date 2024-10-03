import io
import re

patro = re.compile("[A-Za-z0-9 \\-_]+")

arxiu = io.open("C:\\Users\\Usuario\\Downloads\\user_behavior_dataset.csv","r",encoding='utf-8')

llistedecadenes = arxiu.readlines()

matriz = []
longituds = []

for cadena in llistedecadenes:
    matriz.append(patro.findall(cadena))
    if len(patro.findall(cadena)) != 20:
        longituds.append(patro.findall(cadena))


print(matriz)
