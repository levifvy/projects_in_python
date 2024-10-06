'''9. Dir si un número és primer o no'''
while True:
    try:
        entrada = input('Ingresa un numero o marca "y" para terminar: ')
        
        if entrada.lower() == 'y':
            print("Gracias.")
            break
        
        numero = int(entrada)

        if numero <= 1:
            print(f"El numero {numero} no es primo")
        elif numero == 2:
            print(f"El numero {numero} es primo")
        else:
            es_primo = True
            for i in range(2, int(numero ** 0.5) + 1): 
                if numero % i == 0:
                    es_primo = False
                    break

            if es_primo:
                print(f"El numero {numero} es primo")
            else:
                print(f"El numero {numero} no es primo")
    except ValueError:
        print("Ingresa un número válido, sius plau: ")
