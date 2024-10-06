''' Exercici 18: Detecció de codis HTML
Objectiu: Escriu un regex per extreure etiquetes HTML d'un text.
Entrada: <div>Hola</div>, <p>Paràgraf</p> '''

# </\1>: Coincide con la etiqueta de cierre correspondiente, donde \1 se refiere a la primera captura (el nombre de la etiqueta de apertura).

# re.DOTALL: Permite que . coincida con cualquier carácter, incluyendo saltos de línea, lo que permite capturar contenido que puede abarcar múltiples líneas.

import re

patro = re.compile(r"<([\w\s]+)>(.*?)</\1>", re.DOTALL)

entrada = input("Ingresa un texto que contenga etiquetas HTML: ")

resultado = patro.findall(entrada)

resultado_formateado = []

for etiqueta, contenido in resultado:
    etiqueta_formateada = f"<{etiqueta}>{contenido}</{etiqueta}>"
    resultado_formateado.append(etiqueta_formateada)

print("Etiquetas HTML con contenido: ", resultado_formateado)

