'''3. Resolver la letra del DNI'''

def letra_dni(numero_dni):
    letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
    return letras[numero_dni % 23]

dni = 12345678
buscar_letra = letra_dni(dni)
print(buscar_letra)
