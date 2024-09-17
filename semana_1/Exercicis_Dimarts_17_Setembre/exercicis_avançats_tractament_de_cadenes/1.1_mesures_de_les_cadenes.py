'''
Entrada: 'Python és increïble' 
Sortida esperada: 
La paraula més llarga és: increïble 
La paraula més curta és: és 
El caràcter amb el valor ASCII més alt és: y 
El caràcter amb el valor ASCII més baix és: (espai)
'''
import time

entrada = input()
print(f"La entrada es {entrada}")
paraules = entrada.split(' ')
print(f"Despues del split queda asi {paraules}")

paraula_maxima = ''
paraula_minima = entrada
for paraula in paraules:
    print(f"La paraula actual és esta: {paraula}")
    print(paraula_maxima)
    time.sleep(3)
    if len(paraula) > len(paraula_maxima):
        paraula_maxima = paraula
        print(f"y la maxima de momento és: {paraula_maxima}")
    
    if len(paraula) < len(paraula_minima):
        paraula_minima = paraula
        print(f"y la minima de momento és: {paraula_minima}")

print(f"La paraula maxima es {paraula_maxima}")
print(f"La paraula minima es {paraula_minima}")