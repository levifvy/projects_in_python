''' Exercici 8: Validació de números de telèfon mòbils espanyols
Objectiu: Escriu un regex per validar números de telèfon mòbil que comencin amb 6 o 7 i tinguin 9 dígits.
Entrada: 612345678, 711234567, 812345678. '''

import re

patro = re.compile(r"(?:^|\s|,)[6|7]{1}[0-9]{8}(?=$|\s|,|\.)")

entrada = input("Ingresa un texto con numeros telefonicos: ")

resultado = patro.findall(entrada)
resultado = [print((telefonos).strip(' ')) for telefonos in resultado]