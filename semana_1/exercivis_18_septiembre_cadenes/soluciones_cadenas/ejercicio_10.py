'''10. Fes el mateix que el exercici 8 però escriu les paraules en la mateixa línia: 
Exemple: 
user-bash$ python 7reescriulen.py 'la porta contaràs' 
la2 porta5 contaràs8' '''

def reescribir_con_longitud(cadena):
    palabras = cadena.split()
    return ' '.join([f"{palabra}{len(palabra)}" for palabra in palabras])

entrada = input("Ingresa una frase: ")

cadena = entrada.strip()
print(reescribir_con_longitud(cadena))