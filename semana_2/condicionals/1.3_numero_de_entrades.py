# while True:
#     try:
#         numero = int(input("Diguem un número: "))
#         break  # Si l'entrada és correcta, surt del bucle
#     except ValueError:
#         print("Això no és un número vàlid, torna a intentar-ho.")

# # Un cop tenim un número vàlid, fem les comprovacions
# for i in range(numero):
#     print("paraula")


# # Solicitar al usuario cuántas palabras quiere ingresar
# cantidad = int(input("¿Cuántas palabras deseas ingresar? "))

# # Inicializar una lista para almacenar las palabras
# palabras = []

# # Utilizar un bucle para ingresar las palabras
# for i in range(cantidad):
#     palabra = input(f"Ingresa la palabra {i+1}: ")
#     palabras.append(palabra)

# # Imprimir las palabras ingresadas
# print("\nLas palabras que ingresaste son:")
# for palabra in palabras:
#     print(palabra)

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