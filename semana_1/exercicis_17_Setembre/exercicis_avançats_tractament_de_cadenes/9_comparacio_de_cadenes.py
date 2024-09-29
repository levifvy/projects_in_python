'''' 9. Comparació de cadenes (<, >, ==, !=):
Escriu un programa que demani dues cadenes a l'usuari i compari quina és més gran segons l'ordre alfabètic. Mostra si són iguals o diferents.
Entrada: 'gat', 'gos'
Sortida esperada:
La cadena 'gos' és major que 'gat'. '''

entrada = input("Ingresa dos cadenas separades per coma: ")

revision = entrada.replace(" ","")
llista = revision.split(',')

paraula1 = llista[0]
paraula2 = llista[1]

if paraula1 == paraula2:
    print(f"La cadena {paraula1} es igual que {paraula2}") 
elif paraula1 > paraula2:
    print(f"La cadena {paraula1} es major que {paraula2}")
else:    
    print(f"La cadena {paraula2} es major que {paraula1}")

