'''2- Dissenya un programa que rebi per paràmetre una cadena i tregui per pantalla totes les subcadenes de longitud 3.
Per exemple la cadena "planes" treu per pantalla:
pla 
lan 
ane 
nes'''

def quitar_subcadenas(cadena):
    subcadenas = [cadena[i:i + 3] for i in range(len(cadena) - 2)]
    return subcadenas

cadena2 = "planes"
llista_subcadenes = quitar_subcadenas(cadena2)

for subcadena in llista_subcadenes:
    print(subcadena)