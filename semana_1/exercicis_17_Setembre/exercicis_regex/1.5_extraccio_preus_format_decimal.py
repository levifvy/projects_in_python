'''Exercici 5: Extracció de preus en format decimal
Objectiu: Escriu un regex per trobar preus amb decimals en una cadena de text.
Entrada: Els preus dels productes són 10.99€, 20€, 100.50€, i 300.00€, 50,25€
'''
import re

patro = re.compile(r"(?:^|\s|,)[0-9]*[\.,]{1}[0-9]*€(?=$|\s|,|\.)")

entrada = input("Ingresa un texto con precios de productos: ")

resultado = patro.findall(entrada)
resultado = [print(preu.strip(" ")) for preu in resultado]