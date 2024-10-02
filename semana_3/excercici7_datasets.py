import io
import re

patro = re.compile("[A-Za-z0-9 \\-_]+")

arxiu = io.open("C:\\Users\\Alumne_mati1\\Downloads\\work.csv","r",encoding='utf-8')

llistedecadenes = arxiu.readlines()

matriz = []
longituds = []

for cadena in llistedecadenes:
    matriz.append(patro.findall(cadena))
    if len(patro.findall(cadena)) != 20:
        longituds.append(patro.findall(cadena))


print(matriz[1])
