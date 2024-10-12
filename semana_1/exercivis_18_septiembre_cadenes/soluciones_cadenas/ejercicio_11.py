'''11. Determinar si un número es entero, real o incorrecto'''

def validar_numero(cadena):
    try:
        numero = int(cadena)
        return f"El {numero} es un número entero."
    except ValueError:
        try:
            numero = float(cadena)
            return f"El {numero} es un número real."
        except ValueError:
            return f"{cadena} no es un número correcto."


entrada = input("Ingrese un numero: ")
numero = entrada.strip()
print(validar_numero(numero))
