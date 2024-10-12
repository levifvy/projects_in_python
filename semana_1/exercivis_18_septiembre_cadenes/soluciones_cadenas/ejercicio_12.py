'''12- Escriu un programa que rebi 2 cadenes i ens digui si la primera cadena està dins de l'altra. 
user-bash$ python 11trobarcadena.py 'el' 'la casa no estaba'    --> Treu per pantalla: La cadena 'el' NO està dins de 'la casa no estaba' 

user-bash$ python 11trobarcadena.py 'el' 'la casa del campo'    --> Treu per pantalla: La cadena 'el' SI està dins de 'la casa del campo'

Verificar si una cadena está contenida en otra'''

def cadena_en_otra(cadena1, cadena2):
    return f"La cadena '{cadena1}' {'SI' if cadena1 in cadena2 else 'NO'} está dentro de '{cadena2}'"

print(cadena_en_otra('campo', 'la casa de campo'))
