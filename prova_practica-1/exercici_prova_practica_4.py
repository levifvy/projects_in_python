'''Escriu una funció de Python que trobi el màxim de tres números. No es pot utilitzar la funció max.

        def maxim(llista)
        ..................
        ..................
        ..................
        return ...........
    
Per exemple,
print(maxim([7, 3, 8])) imprimirà a la pantalla el número 8, que és el màxim dels tres números.'''

def maxim(lista):
    if int(lista[0]) > int(lista[1]) and int(lista[0]) > int(lista[2]):
        result = int(lista[0])
    elif int(lista[1]) > int(lista[0]) and int(lista[1]) > int(lista[2]):
        result = int(lista[1])
    else:
        result = int(lista[2])
    return result

print(maxim([10,45,23,]))