'''Multiplicar dos sencers positius en base a sumes successives'''
n= int(input("Multiplicando: "))
m = int(input("Multiplicador: "))
acumulador = 0
for i in range(m):
    acumulador = acumulador + n
print(acumulador)
