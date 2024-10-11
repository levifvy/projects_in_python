'''3. Escriure una funció que, donada una cadena (string), retorni la longitud de l'última paraula. Es considera que les paraules estan separades per un o més espais. També hi podria haver espais al principi o al final de la cadena.

def ultimalen(cadena)
..................
..................
..................
return ...........

Per exemple,
print(ultimalen(“ Tinc tanta son que a les cinc tinc son ”)) imprimirà a la pantalla el número 3, ja que 3 és la longitud de l'última paraula "son".'''

def ultimalen(cadena):
    cadena = cadena.strip()
    paraules = cadena.split()
    return len(paraules[-1]) if paraules else 0  

print(ultimalen("     Tinc tanta        son que a les cinc tinc son   "))  

print(ultimalen("     Estic   cansat   de fer el mateix, miillo   farè un programa         "))  