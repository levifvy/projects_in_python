'''7. Ordenació de cadenes (sorted):
Escriu un programa que demani a l'usuari una frase i mostri els caràcters ordenats de manera ascendent i descendent.
Entrada:'zebra'
Sortida esperada:
Caràcters ordenats (ascendent): aebrz
Caràcters ordenats (descendent): zrbca '''

entrada = input('ingresar un cadena: ')

treure_espais = entrada.replace(' ', '')
ascendent = "".join(sorted(treure_espais))
descendent = "".join(sorted(treure_espais,reverse=True))

print(f'Caràcters ordenats (ascendent): {ascendent}')
print("")
print(f'Caràcters ordenats (descendent): {descendent}')

