'''8. Escriu una funció de Python per comprovar si una cadena és un pangrama o no.
Nota: Els pangrames són paraules o frases que contenen cada lletra de l' alfabet
almenys una vegada.
Per exemple la frase en anglès : "The quick brown fox jumps over the lazy dog"
és un pangrama.


def pangrama(cadena):
    ..................
    ..................
    return ...........

Per exemple,
print(pangrama("The quick brown fox jumps over the lazy dog")) imprimirà a la
pantalla True ja que la cadena és un pangrama.
print(pangrama("Aquesta no es pangrama")) imprimirà a la pantalla False ja
que la cadena no és un pangrama.
NOTA. Les cadenes entrades seran sense accents per facilitar la feina.'''

 
import string

def pangrama(cadena):
    cadena = cadena.lower().replace(" ", "")
    alfabet = set(string.ascii_lowercase)
    return alfabet.issubset(set(cadena))

print(pangrama("The quick brown fox jumps over the lazy dog"))  
print(pangrama("Aquesta no es pangrama"))  

