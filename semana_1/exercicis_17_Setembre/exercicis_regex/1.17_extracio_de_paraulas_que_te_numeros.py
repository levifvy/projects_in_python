''' Exercici 17: Extracció de paraules que contenen números
Objectiu: Escriu un regex per extreure paraules que continguin números.
Entrada: He comprat 3pomes i 5plàtans. '''
# pataton2, pata2ton, 2patatton, 2pata43cafssf

# [A-Za-záéíóúàèòÁÉÍÓÚÀÈÒñÑ]*[0-9]+[A-Za-záéíóúàèòÁÉÍÓÚÀÈÒñÑ]*

import re

patro = re.compile(r"\b\w*\d+\w*\b")

entrada = input("Ingresa una frase: ")

resultado = patro.findall(entrada)

print("Palabras con números: ", resultado)
