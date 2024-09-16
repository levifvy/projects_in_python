cadena = "Hola"

print(cadena)

print(cadena.center(20,'*')) # centrada amb el caracter * i longitud 20

print(cadena.center(20,' '))

print(cadena.ljust(20,'*')) # justifició a l'esquera amb longitud 20
print(cadena.rjust(20,'*')) # justifició a la dreta amb longitud 20

password = "La clave esta en Rebeca"

cadenas= input("Entra el password")

if cadenas.lower == password.lower:
    print("Obre el programe")
else:
    print("el password no es el mismo")
