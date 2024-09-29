''' 8. Modificació de cadenes (replace, strip, lstrip, rstrip):
Escriu un programa que demani una frase amb espais al principi i al final, i un caràcter o paraula a substituir. Utilitza 'strip', 'replace', 'lstrip' i 'rstrip' per modificar la cadena i mostrar les versions.
Entrada: ' Hola, Python és genial! ', 'Python'
Sortida esperada:
Frase sense espais: 'Hola, Python és genial!'
Frase sense espais inicials: 'Hola, Python és genial! '
Frase sense espais finals: ' Hola, Python és genial!'
Frase modificada: 'Hola, [substituït] és genial!'  '''

entrada = input("Ingresa una cadena con un espacio tanto al inicio como al final: ")

paraula_o_caracter = input("Ingresa una paraula o un caracter: ")

sense_espais = entrada.strip(" ")
sense_espais_inicials = entrada.lstrip(" ")
sense_espais_finals = entrada.rstrip(" ")
frase_modificada = entrada.replace(paraula_o_caracter, 'substituït')

print(f"Frase sense espais: {sense_espais}")
print(f"Frase sense espais inicials: {sense_espais_inicials}")
print(f"Frase sense espais finals: {sense_espais_finals}")
print(f"Frase modificada: {frase_modificada}")