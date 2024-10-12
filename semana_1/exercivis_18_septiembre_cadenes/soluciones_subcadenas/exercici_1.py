'''1- Dissenya un programa que tregui tots els prefixes d'una cadena que rebem per paràmetre. Per exemple la cadena "Fedora" treu per pantalla: 

F 
Fe 
Fed 
Fedo 
Fedor 
Fedora 
'''

def quitar_prefijos(cadena):
    prefijos = []
    for i in range(1, len(cadena) + 1):
        prefijos.append(cadena[:i])
    return prefijos

cadena = "Fedora"
llista_prefixs = quitar_prefijos(cadena)

for prefix in llista_prefixs:
    print(prefix)
    