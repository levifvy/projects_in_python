'''5. Comparar la longitud de dos cadenas y mostrar la mas larga, la cantidad de palabras y la cantidad de letras'''

def comparar_cadenas(cadena1, cadena2):
    cadena_larga = cadena1 if len(cadena1) > len(cadena2) else cadena2
    n_paraulas = len(cadena_larga.split())
    n_letras = sum(len(paraula) for paraula in cadena_larga.split())
    return cadena_larga,n_paraulas,n_letras


cadena1 = "El país fue ocupado inmediatamente y desmembrado."
cadena2 = "Los intentos del nuevo gobierno, de apaciguar, al canciller alemán resultaron vanos."

cadena_gran, numero_paraulas, numero_letras = comparar_cadenas(cadena1,cadena2)

print(f"{cadena_gran} → {numero_paraulas} paraulas, {numero_letras} letras.")