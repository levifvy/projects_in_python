
llista = [5,4,5,3,2,6,4,7,8,2,9,7,7,4,4,4]
# resposta = set(llista)
# print(resposta)
# print(list(resposta))
resultat = []
for element in llista:
    if element not in resultat:
        resultat.append(element)

print(resultat)