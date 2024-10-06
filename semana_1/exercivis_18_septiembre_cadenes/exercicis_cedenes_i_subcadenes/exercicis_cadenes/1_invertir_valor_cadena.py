'''
1- Invertir el valor d'una cadena:
a)Assignar a una variable una cadena de text qualsevol, després crear una altra variable de text
buida on haurem de fer el procés per passar els valors de e l'anterior cadena però invertida.
b) Mostrar els caràcters d'una cadena en ordre invers
'''

cadena = "El valor de la puntualidad"

# print(cadena[0])
# print(cadena[len(cadena)-1])

# contador = len(cadena)-1
# print("")
# while contador >= 0:
#     print(cadena[contador], end="")
#     contador-=1
# print("")
# print("")

escritor = 'Fyodor Mikhailovich Dostoevsky'
cadenaInvertida = escritor[::-1]
print(cadenaInvertida)