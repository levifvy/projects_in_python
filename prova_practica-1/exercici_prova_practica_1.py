'''1. Implementar un programa que sol·liciti números a l'usuari –entrats un per un- fins que ingressi el zero. Després d’introduir cada número es mostrarà el seu factorial. Al finalitzar es mostrarà la quantitat total de números llegits. Utilitzar una o més funcions, segons sigui necessari.'''

def solicitar_numeros():
    llista_numeros = []
    while True:
        try:
            entrada = int(input('Ingresa un número o ingresa 0 para terminar: ')) 
            if entrada == 0:
                break
            llista_numeros.append(entrada)
        except ValueError:
            print('Ingresa un número válido.')
    return llista_numeros

def factorial(numero):
    result = 1
    for i in range(2, numero + 1):
        result *= i
    return result

def mostrar_factorials(numeros):
    for numero in numeros:
        print(f"{numero} → {factorial(numero)}")
    print(f"Cantidad de números leídos: {len(numeros)}")

numeros = solicitar_numeros()
mostrar_factorials(numeros)
