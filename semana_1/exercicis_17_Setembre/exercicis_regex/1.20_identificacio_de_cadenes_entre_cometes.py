''' Exercici 20: Identificació de cadenes entre cometes
Objectiu: Escriu un regex per extreure cadenes entre cometes dobles d'un text.
Entrada: "Hola", "Bon dia", 'Això no val'. '''

import re

patro = re.compile(r'["\'](.*?)["\']')

entrada = input("Ingresa un texto con cadenas entre comillas dobles: ")

resultado = patro.findall(entrada)

print("Cadenas entre comillas dobles:", resultado)
