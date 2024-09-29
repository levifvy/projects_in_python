'''  10. Comprovacions True/False (isdigit, isalpha, islower, startswith,
endswith):
Escriu un programa que demani una cadena a l'usuari i comprovi si només conté dígits, lletres, espais, i si comença o acaba amb un caràcter específic.
Entrada: 'Python123'
Sortida esperada:
La cadena només conté dígits: False
La cadena només conté lletres: False
La cadena només conté espais: False
La cadena comença amb 'P': True  '''

entrada = input("Ingresa una cadena: ")

nomes_digits = entrada.isdigit()
print(f"La cadena només conté dígits: {nomes_digits}")

nomes_lletres = entrada.isalpha()
print(f"La cadena només conté lletres: {nomes_lletres}")

nomes_espais = entrada.isspace()
print(f"La cadena només conté espais: {nomes_espais}")

start_with = entrada.startswith('P')
print(f"La cadena comença amb 'P': {start_with}")