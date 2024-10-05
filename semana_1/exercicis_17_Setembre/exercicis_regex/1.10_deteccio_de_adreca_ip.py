''' Exercici 10: Detecció d'adreces IP
Objectiu: Escriu un regex per validar adreces IP en format IPv4.
Entrada: 192.168.1.1, 255.255.255.0, 999.999.999.999, 0.0.0.0. '''

import re

patro = re.compile(r"(?:^|\s|,)(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?=$|\s|,|\.)")

entrada = input("Ingresa un texto con  direcciones IPv4: ")

resultado = patro.findall(entrada)
resultado = [".".join(ip) for ip in resultado]

print("Adreces IP vàlides: ", resultado)
