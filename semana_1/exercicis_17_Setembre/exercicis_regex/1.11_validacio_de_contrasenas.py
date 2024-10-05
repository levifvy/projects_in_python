'''Exercici 11: Validació de contrasenyes 
Objectiu: Escriu un regex per validar contrasenyes que tinguin entre 8 i 16 caràcters, almenys una majúscula, una minúscula, i un número. 
Entrada: Contraseña1, pass, PASSWORD123, loker123456, PROTEGIENDO2098, 502545562615, cuidadorInt123. '''

import re

patro = re.compile(r"(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$")

entrada = input("Ingresa un texto que contenga contraseñas: ")

posibles_contrasenyes = [contrasenya.strip() for contrasenya in entrada.split(",")]

contrasenyes_valides = [contrasenya for contrasenya in posibles_contrasenyes if patro.match(contrasenya)]

print("Contrasenyes vàlides: ", contrasenyes_valides)

