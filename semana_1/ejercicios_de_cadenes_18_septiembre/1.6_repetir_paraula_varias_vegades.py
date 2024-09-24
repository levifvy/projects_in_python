''' 6-Dissenya un programa que demani una paraula i l'escrigui per pantalla tantes vegades com la seva longitud: 
exemple: user-bash$ python repeteix.py hal 
hal 
hal 
hal
'''

cadena = input("Ingresa una paraula: ")
print("")
numero = len(cadena)
print((cadena + "\n")*numero)
