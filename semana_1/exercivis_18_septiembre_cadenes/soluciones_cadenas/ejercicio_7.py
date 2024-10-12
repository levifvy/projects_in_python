'''7. Contar vocales en una frase y determinar la mas y menos abundante'''

def contar_vocales(cadena):
    vocales = 'aeiou'
    
    cuenta_vocales = {vocal: cadena.lower().count(vocal) for vocal in vocales}
    
    mas_abundante = max(cuenta_vocales, key=cuenta_vocales.get)
    
    menos_abundante = min(cuenta_vocales, key=cuenta_vocales.get)
    
    return mas_abundante, cuenta_vocales[mas_abundante], menos_abundante, cuenta_vocales[menos_abundante]

cadena = input("Introduce una frase: ")

abundante, cantidad_abundante, escaso, cantidad_escaso = contar_vocales(cadena.strip())


print(f"La {abundante} es la vocal más abundante con {cantidad_abundante} {'coincidencia' if cantidad_escaso == 1 else 'coincidencias'}.")
print(f"La {escaso} es la vocal que se repite menos veces con {cantidad_escaso} {'coincidencia' if cantidad_escaso == 1 else 'coincidencias'}.")
