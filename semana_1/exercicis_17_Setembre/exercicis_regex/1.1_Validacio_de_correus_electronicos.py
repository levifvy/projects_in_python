# '''Exercici 1: Validació de correus electrònics
# Objectiu: Escriu una expressió regular per validar correus electrònics simples.
# Entrada: hola@test.com, josep.puigdemont@company.cat, marta123@xyz.org, persona@.
# '''
# (?<=^|\s) ... (?=$|\s)
# regex101.com

import re

#patro = re.compile(r"(?<=^|\s|,)[a-z0-9]+\.?[a-z0-9]+@[a-z0-9]+\.[a-z0-9]+(?=$|\s|,|.)")

patro = re.compile(r"(?:^|\s|,)[a-z0-9]+\.?[a-z0-9]+@[a-z0-9]+\.[a-z]{2,}(?=$|\s|,|\.)")

entrada = input("Ingrese un texto: ")

resultado = patro.findall(entrada)
resultado = [correo.strip(", ") for correo in resultado]

for cadena in resultado:   
    print(cadena)





