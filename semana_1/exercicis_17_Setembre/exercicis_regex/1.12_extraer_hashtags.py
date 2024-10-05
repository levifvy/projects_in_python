'''Exercici 12: Identificació de hashtags
Objectiu: Escriu un regex per extreure hashtags d'un text.
Entrada: Avui és un bon dia #sunny #felicitat #dia.'''

import re

patro = re.compile(r"(?:^|\s|,)#[A-Za-záéíóúàèòÁÉÍÓÚÀÈÒñÑ]+(?=$|\s|,|\.)")

entrada = input("Ingresa un texto que contenga hashtags: ")

resultado = patro.findall(entrada)
resultado = [hashtag.strip(' ') for hashtag in resultado]

print("Hashtags: ", resultado)