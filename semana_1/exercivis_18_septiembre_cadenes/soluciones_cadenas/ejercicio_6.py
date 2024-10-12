'''6. Repetir una palabra tantas veces como su longitud'''

def repetir_palabra(palabra):
    return (palabra + '\n') * len(palabra)

entrada = input("Ingrese una paraula: ")

palabra = entrada.strip()
repetir = repetir_palabra(palabra)
print(repetir)