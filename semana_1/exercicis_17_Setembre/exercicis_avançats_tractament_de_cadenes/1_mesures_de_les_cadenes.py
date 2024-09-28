''' Entrada: 'Python és increïble' 
Sortida esperada: 
    La paraula més llarga és: increïble 
    La paraula més curta és: és 
    El caràcter amb el valor ASCII més alt és: y 
    El caràcter amb el valor ASCII més baix és: (espai)'''

entrada = input("Ingresa una cadena: ")
print("")
paraules = entrada.split(' ')

paraula_maxima = ''
paraula_minima = entrada
for paraula in paraules:
    if len(paraula) > len(paraula_maxima):
        paraula_maxima = paraula
    
    if len(paraula) < len(paraula_minima):
        paraula_minima = paraula

mes_grand = entrada[0]
mes_petit = entrada[0]
contador = 0

for i in entrada:
    print(f"{i} es {ord(i)}")
    if ord(i) > ord(mes_grand):
        mes_grand = i
    if ord(i) < ord(mes_petit):
        mes_petit = i
    contador += 1

if mes_petit == ' ':
    mes_petit = "espai"

print(f"La paraula més llarga és: {paraula_maxima}")
print(f"La paraula més curta és: {paraula_minima}")
print("")
print(f"El caràcter amb el valor ASCII més alt és: {mes_grand}")
print(f"El caràcter amb el valor ASCII més baix és: {mes_petit}")



