'''4. Contar el número de palabras en una cadena'''

def contar_palabras(cadena):
    return len(cadena.split())

cadena = 'Python is a dynamic object-oriented programming language'
palabras_contadas = contar_palabras(cadena)
print(palabras_contadas)
