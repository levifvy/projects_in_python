'''Exercici 13: Extracció d'enllaços sense protocol 
Objectiu: Escriu un regex per extreure enllaços web que no incloguin el protocol (ex: www). 

Entrada: Visita www.example.com per més informació. www.google.com.es, www.google.co.uk '''

import re

patro = re.compile(r"(www\.[a-zA-Z0-9\-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?)")

entrada = input("Ingresa un texto que contenga enlaces: ")

resultado = patro.findall(entrada)

print("Enlaces: ", resultado)
