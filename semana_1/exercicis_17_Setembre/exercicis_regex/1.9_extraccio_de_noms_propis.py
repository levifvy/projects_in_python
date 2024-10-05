'''Exercici 9: Extracció de noms propis 
Objectiu: Escriu un regex per extreure noms propis d'una frase (inicien amb ajúscula). 
Entrada: Maria va anar a Barcelona amb Josep i Anna. '''

import re

patro = re.compile(r"(?:^|\s|,)[A-ZÁÉÍÓÚÀÈÒÑ][a-záéíóúàèòñ]*(?=$|\s|,|\.)")

entrada = input("Ingresa un texto que contenga palabras que inicien con mayusculas: ")

resultado = patro.findall(entrada)
resultado = [print(nou.strip(' ')) for nou in resultado]