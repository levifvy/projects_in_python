import random
import string

# Función para generar una palabra aleatoria
def generar_palabra_aleatoria(longitud):
    letras = string.ascii_lowercase # Letras del alfabeto en minúscula
    return ''.join(random.choice(letras) for _ in range(longitud))

# Solicitar al usuario cuántas palabras desea generar
cantidad = int(input("¿Cuántas palabras aleatorias deseas generar? "))

# Generar y mostrar las palabras aleatorias
palabras = [generar_palabra_aleatoria(random.randint(3, 10)) for _ in range(cantidad)]

print("\nLas palabras generadas son:")
for palabra in palabras:
    print(palabra)