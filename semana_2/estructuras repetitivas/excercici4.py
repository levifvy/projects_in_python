'''Escriure els n primers múltiples de m'''

# n = int(input("Ingresa un numero: "))
# m = int(input("Ingresa un numero de multiplos: "))

# numero = 0
# multiplos = 1

# while multiplos <= m:
#     print(numero, end=" ")
#     numero+=n
#     multiplos+=1

'''n = int(input("Ingresa un número: "))
m = int(input("Ingresa el número de múltiplos: "))

for i in range(m):
    print(i * n, end=" ")'''
    
n = int(input("Ingresa un número: "))
m = int(input("Ingresa el número de múltiplos: "))

numero = 0    
while m > 0:
    print(numero, end=" ")
    numero += n
    m -= 1