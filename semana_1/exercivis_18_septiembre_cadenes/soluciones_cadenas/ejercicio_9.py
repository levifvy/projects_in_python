'''Reescribir con longitud de cada palabra'''
def reescribir_con_longitud(cadena):
    palabras = cadena.split()
    return ''.join([f"{palabra}{len(palabra)}\n" for palabra in palabras])

cadena = 'esta es una prueba'
print(reescribir_con_longitud(cadena))
