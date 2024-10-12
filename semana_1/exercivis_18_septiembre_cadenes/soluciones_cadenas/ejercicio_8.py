'''Reescribir frase añadiendo 'BONICA PARAULA' despues de cada palabra'''
def reescribir_frase_bonica(cadena):
    palabras = cadena.split()
    return ' '.join([palabra + ' BONICA PARAULA' for palabra in palabras])

entrada = input("Ingresa una frase: ")
cadena = reescribir_frase_bonica(entrada).strip()
print(cadena)
