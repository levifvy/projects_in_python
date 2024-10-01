# llista = [[2,5,10],[6,7,9],[4,5,10],[20,30,40]]

# resultat = []
# for sublista in llista:
#     subresultat = []
#     for element in sublista:
#         element +=1
#         subresultat.append(element)
#     resultat.append(subresultat)


# print(resultat)

#------------------------
# versio 1
'''matriu = [[2,5,10],[6,7,9],[4,5,10],[20,30,40]]

def incremento(llista):
    resultado = []
    for element in llista:
        resultado.append(element + 1)
    return resultado

resultat = []

for fila in matriu:
   resultat.append(incremento(fila))

print(resultat)'''

#------------------------
# versio 2
'''matriu = [[2,5,10],[6,7,9],[4,5,10],[20,30,40]]

for fila in matriu:
    for pos in range(len(fila)):
        fila[pos] += 1
print(matriu)'''

#------------------------
# versio 3
'''matriu = [[2,5,10],[6,7,9],[4,5,10],[20,30,40]]

def incremento(llista):
    resultado = [element + 1 for element in llista]
    return resultado
    

resultat = []

resultat = [incremento(fila) for fila in matriu]
print(resultat)'''

#------------------------
# versio 4:
# 1000 numeroas aleatorios 0,1000en una lista

