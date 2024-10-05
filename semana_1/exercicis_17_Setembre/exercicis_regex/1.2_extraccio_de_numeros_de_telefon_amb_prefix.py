'''Exercici 2: Extracció de números de telèfon amb prefix
Objectiu: Escriu una expressió regular per extreure els números de telèfon espanyols amb prefix "(93)".
Entrada: (93)2541700, (952)253228, (93)2177017, (958)233517, (93), (93)4561233.
'''
import re

#patro = re.compile("?<=^|\s|,)\([0-9]+\)[0-9]{5,}(?=$|\s|,|\.")
patro = re.compile(r"(?:^|\s|,)\(93\)[0-9]{5,}(?=$|\s|,|\.)")

entrada = input("Ingrese un texto con numeros telefonicos: ")

resultado = patro.findall(entrada)
resultado = [telefono.strip(", ") for telefono in resultado]

for telefono in resultado:
    print(telefono)