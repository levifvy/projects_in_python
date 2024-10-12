'''14.-Escriu un programa que donada una cadena ens digui si és un palíndrom o no. Una frase o cadena és palíndroma si es pot llegir en ordre o a l'inrevés obtenint la mateixa frase, per exemple: 
"dabale arroz a la zorra el abad", és palíndroma. 
Determinar si una cadena es un palíndromo'''

def es_palindromo(cadena):
    cadena_sin_espacios = cadena.replace(' ', '').lower()
    return 'Es palídromo.' if cadena_sin_espacios == cadena_sin_espacios[::-1] else 'No es palíndromo.'


entrada = input("Ingresa una cadena: ")
cadena = entrada.strip()
resultado = es_palindromo(cadena)

print(f"{cadena}, {resultado}")


#anilina