'''
4. Majúscules i minúscules (upper, lower, capitalize):
Escriu un programa que demani una frase a l'usuari. El programa ha de mostrar la frase 
en tres versions: totes les paraules en majúscula, en minúscules, i amb només la primera 
lletra en majúscula. 
Entrada: 'el gat menja peix' 
Sortida esperada: 
Frase amb majúscules: EL GAT MENJA PEIX 
Frase en minúscules: el gat menja peix 
Frase capitalitzada: El gat menja peix 
La frase estava originalment en minúscules. 
'''
frase = input("Ingresa una frase: ")
print("")
print("Entrada: ", frase)
print("")

frase_majuscules = frase.upper()
print(f"Frase amb majúscules: {frase_majuscules} ")

frase_minuscules = frase.lower()
print(f"Frase en minúscules: {frase_minuscules} ")

frase_capitalized = frase.capitalize()
print(f"Frase capitalitzada: {frase_capitalized} ")

print("")