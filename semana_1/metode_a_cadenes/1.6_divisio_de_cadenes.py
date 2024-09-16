frase = "Hola com estàs jo bé i tu?"
print(frase.split(' ')) # El resultat será una llista
print(frase.split('-')) # No dividira res, perque no hi ha - en la cadena

print(frase.partition(' ')) # El resultat será una tupla i és inmutable
print(frase.rpartition(' '))# El resultat será una tupla i és inmutable