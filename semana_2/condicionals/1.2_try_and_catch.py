
while True:
    try:
        numero = int(input("Diguem un número: "))
        break  # Si l'entrada és correcta, surt del bucle
    except ValueError:
        print("Això no és un número vàlid, torna a intentar-ho.")

# Un cop tenim un número vàlid, fem les comprovacions
if numero == 0:
    print("El número és 0.")
elif numero > 0:
    print(f"{numero} és positiu.")
else:
    print(f"{numero} és negatiu.")