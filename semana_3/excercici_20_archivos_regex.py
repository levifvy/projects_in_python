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
scorealt  = 0
indexalt = 0
scoreover = 0
indexover = 0

scorebaix_ = 0
indexbaix_ = 0
scoremig_  = 0
indexmig_ = 0
scorealt_  = 0
indexalt_ = 0
scoreover_ = 0
indexover_ = 0

for pos in range(len(hores_estudiades)):
    
    if 0 <= hores_estudiades[pos] < 4:

        scorebaix += scores[pos]
        indexbaix   += 1

    elif  4 <= hores_estudiades[pos] < 6:

        scorebaix_ += scores[pos]
        indexbaix_   += 1

    elif 6 <= hores_estudiades[pos] < 8:

        scoremig += scores[pos]
        indexmig   += 1

    elif  8 <= hores_estudiades[pos] < 9:

        scorealt += scores[pos]
        indexalt   += 1
         
    else:
        scoreover += scores[pos]
        indexover += 1
        
print(scorebaix_/indexbaix_, scoremig/indexmig, scorealt/indexalt,scoreover/indexover)

