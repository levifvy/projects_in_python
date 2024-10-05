''' Exercici 3: Identificació de paraules amb accents 
Objectiu: Extrau totes les paraules que contenen accents en una frase. 
Entrada: Hola, com estàs? Avui és un dia solejat i l'hora és les 10:30 del matí. '''

import re

patro = re.compile(r"\b\w*[àèìòùáéíóúÁÉÍÓÚÀÈÌÒ]+\w*\b")

entrada = input("Ingresa un texto: ")

resultado = set(patro.findall(entrada))
resultado = [print(paraula.strip(" ")) for paraula in resultado]

