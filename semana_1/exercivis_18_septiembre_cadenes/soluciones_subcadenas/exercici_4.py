'''4- Dissenya un programa que llegeixi 2 cadenes a i b i ens digui si a es un prefixe de b.
Per exemple si introdueixen les següents cadenes 'sub' i 'subcadena' el resultat és:
Entrada -->  Sortida 
'sub' 'subcadena' 'sub' es un prefixe de 'subcadena' 
'es' 'camins' 'es' NO és un prefixe de 'camins'
'''

def es_prefijo(a, b):

    return a == b[:len(a)]

cadena_a = 'sub'
cadena_b = 'subcadena'
print(f"{cadena_a} {'es'if es_prefijo(cadena_a, cadena_b) else 'No és' } un prefixe de {cadena_b}")