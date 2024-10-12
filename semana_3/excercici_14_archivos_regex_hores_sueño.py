import re
import io

patro = re.compile(r"[A-Za-z0-9-':\/\_\.!$?]+|\"[^\"]*\"")

arxiu = io.open(r"C:\\Users\\Alumne_mati1\\Documents\\python_cifo_septiembre_2024\\semana_3\\PRIMER_ESTUDI\\StudentPerformanceFactors.csv","r",encoding = 'utf-8')

#llistadecadenes = arxiu.readlines()

llistadecadenes = [cadena.replace(",,",",ND,") for cadena in arxiu.readlines()]

matriu = []

for cadena in llistadecadenes:
    matriu.append(patro.findall(cadena))

hores_estudiades = []
scores = []

for llista in matriu[1:]:
    
    hores_estudiades.append(int(llista[0]))
    scores.append(int(llista[-1]))
   
scorebaix = 0
indexbaix = 0
scoremig  = 0
indexmig = 0

for pos in range(len(hores_estudiades)):
    
    if hores_estudiades[pos] == 4:

        scorebaix += scores[pos]
        indexbaix += 1

    elif hores_estudiades[pos] == 5:

        scoremig += scores[pos]
        indexmig += 1
        
print(scorebaix/indexbaix, scoremig/indexmig)