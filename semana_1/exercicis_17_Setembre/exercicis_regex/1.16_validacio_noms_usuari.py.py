''' Exercici 16: Validació de noms d'usuari
Objectiu: Escriu un regex per validar noms d'usuari que només continguin caràcters alfanumèrics i guions baixos.
Entrada: usuari_123, usuari-abc, usuari.abc. '''

import re

patro = re.compile(r"^[a-zA-Z0-9_]+$")

entrada = input("Ingresa nombres de usuario separados por comas: ")

nombres = entrada.split(", ")

resultado = [nombre for nombre in nombres if patro.match(nombre)]

print("Nombres de usuario válidos: ", resultado)
