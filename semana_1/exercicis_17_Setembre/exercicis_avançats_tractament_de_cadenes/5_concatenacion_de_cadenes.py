''' 5. Concatenació de cadenes (''.join()):
Escriu un programa que demani a l'usuari una llista de paraules separades per comes i un símbol escollit per l'usuari per unir-les. 
Entrada: 'poma,plàtan,taronja', '@' 
Sortida esperada: 
poma@plàtan@taronja
'''
entrada = input("Ingresa un llista de paraules y un simbol separades por comes: ")

recortando = entrada.split(',')
paraulas = recortando[0:len(recortando)-1]
simbol = recortando[len(recortando)-1]
print(simbol.join(paraulas))