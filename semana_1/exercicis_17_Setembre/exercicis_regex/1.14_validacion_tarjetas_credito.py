''' Exercici 14: Validació de targetes de crèdit
Objectiu: Escriu un regex per validar números de targetes de crèdit amb 16 dígits.
Entrada: 1234 5678 9012 3456, 1111 2222 3333 4444. '''

import re

patro = re.compile(r"(?:\d{4}\s){3}\d{4}")

entrada = input("Ingresa un texto que contenga números de tarjeta de crédito: ")

resultado = patro.findall(entrada)

print("Números de tarjeta de crédito válidos: ", resultado)
