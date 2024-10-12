import re
import io

patro = re.compile(r"[A-Za-z0-9-':\/\_\.!$?]+|\"[^\"]*\"")

arxiu = io.open(r"C:\\Users\\Alumne_mati1\\Downloads\\StudentPerformanceFactors.csv","r",encoding = 'utf-8')

#llistadecadenes = arxiu.readlines()

llistadecadenes = [cadena.replace(",,",",ND,") for cadena in arxiu.readlines()]

matriu = []

for cadena in llistadecadenes:
    matriu.append(patro.findall(cadena))

longituds = [len(element) for element in matriu]

print(set(longituds))