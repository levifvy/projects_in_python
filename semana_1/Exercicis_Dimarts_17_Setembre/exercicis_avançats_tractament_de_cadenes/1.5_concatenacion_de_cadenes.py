'''
5. Concatenació de cadenes (''.join()):
Escriu un programa que demani a l'usuari una llista de paraules separades per comes i un 
símbol escollit per l'usuari per unir-les. 
Entrada: 'poma,plàtan,taronja', '@' 
Sortida esperada: 
poma@plàtan@taronja
'''
lista = input("Ingresa un llista de paraules separades per comes: ")
simbol = input("Ingresa un simbol: ")

print("")

paraules = lista.split(",")

print(simbol.join(paraules))

print("")








# otra manera
# llista_entrada = []
# entrada = ""

# while entrada != 'y':
#     entrada = input("Ingresa un llista de paraules pressione y per terminar: ")
#     llista_entrada.append(entrada)
#     if entrada == 'y':
#         llista_entrada.remove("y")
# for valor in llista_entrada:
#     print(valor)
# print("")

# simbol = input("Ingresa un simbol: ")

# print("")

# print("Entrada: ")
# print("")