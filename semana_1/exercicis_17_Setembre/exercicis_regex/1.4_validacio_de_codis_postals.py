'''Exercici 4: Validació de codis postals 
Objectiu: Escriu un regex per validar codis postals de 5 dígits espanyols. 
Entrada: 08001, 08080, 12345, abcd5, 5678. '''

import re

patro = re.compile(r"(?:^|\s|,)\b[0-9]{5}(?=$|\s|,|\.)")

entrada = input("Ingresa un texto con codigos postales: ")

resultado = patro.findall(entrada)
resultado = [print(codi_postal.strip(" ")) for codi_postal in resultado]