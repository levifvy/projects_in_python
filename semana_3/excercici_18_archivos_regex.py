import re
import io

patro = re.compile(r"[A-Za-z0-9-':\/\_\.!$?]+|\"[^\"]*\"")

arxiu = io.open(r"C:\\Users\\Alumne_mati1\\Documents\\python_cifo_septiembre_2024\\semana_3\\PRIMER_ESTUDI\\StudentPerformanceFactors.csv","r",encoding = 'utf-8')

#llistadecadenes = arxiu.readlines()

llistadecadenes = [cadena.replace(",,",",ND,") for cadena in arxiu.readlines()]

matriu = []

for cadena in llistadecadenes:
    matriu.append(patro.findall(cadena))

longituds = [len(element) for element in matriu]

#print(set(longituds))

#print(matriu[0])
hores_estudiades = []
score = []
for llista in matriu[1:]:
    hores_estudiades.append(int(llista[0]))
    score.append(int(llista[-1]))

#print(hores_estudiades)
'''print(min(hores_estudiades))
print(max(hores_estudiades))
#print(score)

print(min(score))
print(max(score))
'''
# 0 --- 10 h/week -----> poc estudi
# 10 --- 20 h/week -----> mitja
# 20 --- 30 h/week -----> bon
# +30 h/week -----> overload

scorebaix  = 0
indexbaix = 0

scoremig  = 0
indexmig = 0

scorealt  = 0
indexalt = 0

scoreover  = 0
indexover = 0

scorebaix_  = 0
indexbaix_ = 0

scoremig_  = 0
indexmig_ = 0

scorealt_  = 0
indexalt_ = 0

scoreover_  = 0
indexover_ = 0

for pos in range(len(hores_estudiades)):

    if 0 <= hores_estudiades < 5:

        scorebaix += score[0]
        indexbaix += 1
    
    elif 5 <= hores_estudiades < 10:

        scoremig_ += score[0]
        indexmig_ += 1

    elif 10<= hores_estudiades < 15:

        scoremig += score[0]
        indexmig += 1

    elif 15 <= hores_estudiades < 20:

        scoremig_ += score[0]
        indexmig_ += 1

    elif 20<= hores_estudiades < 25:

        scorealt += score[0]
        indexalt += 1
    else:
        scoreover += score[0]
        indexover += 1



    
