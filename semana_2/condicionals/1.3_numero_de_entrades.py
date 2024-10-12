while True:
    try:
        numero = int(input("Diguem un número: "))
        break  
    except ValueError:
        print("Això no és un número vàlid, torna a intentar-ho.")

for i in range(numero):
    print("paraula")
#---------------------------------------------------------------------
cantidad = int(input("¿Cuántas palabras deseas ingresar? "))

palabras = []
for i in range(cantidad):
    palabra = input(f"Ingresa la palabra {i+1}: ")
    palabras.append(palabra)

print("\nLas palabras que ingresaste son:")
for palabra in palabras:
    print(palabra, end=" ")
