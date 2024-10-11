'''Escriu una funció de Python que comprovi si un número cau en un rang donat.

def dinsrang(numero, rang1, rang2):
..................
..................
..................
return ...........

Per exemple,
print(dinsrang(3, 2, 5)) imprimirà True, ja que 3 es troba entre els números 2 i 5.
print(dinsrang(5, 2, 3)) imprimirà False, ja que 5 no es troba entre els números 2 i 3.'''

def dinsrang(numero, rang1, rang2):
    return min(rang1, rang2) <= numero <= max(rang1, rang2)

print(dinsrang(3,2,5))
print(dinsrang(5, 2, 3))
print(dinsrang(1, 2, 5))