'''Escriure tots els divisors d'un número en ordre ascendent'''

while True:
    try:
        entrada = input('Ingresa un numero o marca "y" para terminar: ')
        
        if entrada.lower() == 'y':
            print("Gracias.")
            break
       
        numero = int(entrada)
        i = 1
        while i in range(1,numero+1):
            if numero % i == 0:
                print(i,end=" ")
            i +=1
        print("")

    except ValueError:
        print("Ingresa un valor valido. Torna a intentarlo")

