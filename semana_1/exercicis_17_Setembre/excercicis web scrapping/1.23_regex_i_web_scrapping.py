

import requests
from bs4 import BeautifulSoup
import re

patro = re.compile("?<=\s|^)[0-9]{4}(?=\s|$")

# URL de la página de Wikipedia que quieres obtener 
url "https://es.wikipedia.org/wiki/Python_(lenguaje_de_programación)"

9 #Realiza la petición a la página

10 response requests.get(url)

#Comprobar que la petición fue exitosa (código 200)

if response.status_code == 200:

#Crear el objeto BeautifulSoup para parsear el HTML

soup BeautifulSoup(response.content, 'html.parser')

Encontrar el contenido principal de la página

content soup.find(id="mr-content-text")


else: 
    print("No se pudo acceder a la página.")