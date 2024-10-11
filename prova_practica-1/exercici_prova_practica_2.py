'''2. Implementar un programa que sol·liciti números a l'usuari –entrats un per un- fins que ingressi el zero. Al final el programa mostrarà cada número i al costat la suma dels seus dígits. El zero no cal presentar-lo. (El programa contindrà una funció que realitzarà i retornarà la suma dels dígits d’un número). '''

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

def suma_digitos_numero(numero):
    result = 0
    for digito in str(numero):
        result += int(digito)
    return result

numeros = solicitar_numeros()
for numero in numeros:
    suma_obtenida = suma_digitos_numero(int(numero))
    print(f"{numero} → {suma_obtenida}")

