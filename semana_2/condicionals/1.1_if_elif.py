'''
Dos casos
opcion A:
if caso1:
if caso2:

opcion B: Los casos no se excluyen <----- pueden ser verda lols dos a la vez
if caso1:
if caso2:

opcion c: los casos se excluyen <--- no pueden ser verdad los dos a la vez
if caso1:
else:

Tres casos o mas (casos excluyentes)

lf caso1:
elif caso2:
elif caso3:
else:

if caso1:
if caso2:
if caso3:
if caso4:
if caso5:
if caso resto:

'''
# a = 3

# b = 5
# if (a ==3):
    
#     print("a vale 3")
    
# elif (b == 5):
    
#     print("b vale 5")
    
# else:
#     print("Hola")
'''

# numero = int(input(" INtroduce un numero: "))

# if numero > 0:

#     print(f"El numero {numero} es positivo")

# if numero % 2 == 0:

#     print(f"El numero {numero} es par")
'''

'''# Escriu un programa que, donat un nombre enter, 
# mostri un missatge que indiqui si el nombre és:
numero = int(input(" INtroduce un numero: "))
if (numero > 0):
    
    print(f"El numero {numero} es positiu.")
    
elif (numero < 0):
    
    print(f"El numero {numero} es negatiu.")
    
else:
    print(f"El numero {numero} es zero.")'''

import re

patro = re.compile(r"(?<!\S)-?[0-9]+(?!\S)")

entrada = (input("Escriu un número: "))

print(patro.findall(entrada))

while len(patro.findall(entrada)) != 1:
    entrada = (input("Escriu un número: "))

numero = patro.findall(entrada)[0]

if numero == "0":

    print(f" el número que has escrit és {numero} i té un valor de 0")

elif numero.isdigit():

    print(f" El nombre {numero} és positiu")

elif "-" in numero:

    print(f"El nombre {numero} és negatiu")

    # https://chatgpt.com/share/66f13424-2578-800d-8990-8105f8f3b823