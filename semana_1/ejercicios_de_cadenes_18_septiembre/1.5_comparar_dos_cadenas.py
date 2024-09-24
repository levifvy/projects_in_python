''' 5-Passar a un programa 2 cadenes de text i dir quina cadena de text és la més llarga
(quina té len major)i quin número de lletres (comptem com a lletra qualsevol 
caràcter entre la 'A' i la 'Z' i la 'a' i la 'z') té.
'''
cadena1 = "El país fue ocupado inmediatamente y desmembrado."
cadena2 = "Los intentos del nuevo gobierno de apaciguar al canciller alemán resultaron vanos."
paraules1 = cadena1.split(" ")
paraules2 = cadena2.split(" ")

contador1 = 0
for palabras1 in paraules1:
    for letras in palabras1:
        contador1 += 1
print(contador1)

contador2 = 0
for palabras2 in paraules2:
    for letras in palabras2:
        contador2 += 1
print(contador2)

if len(paraules1) > len(paraules2):
    print("Cadena 1 es mayor que cadena 2")
    print("Cadena 1 tiene ",len(paraules1), " paraulas y ",contador1," lletres.")
    print("Cadena 2 tiene ",len(paraules2), " paraulas y ",contador2," lletres.")
else:
    print("Cadena 2 es mayor que cadena 1")
    print("Cadena 1 tiene ",len(paraules1), " paraulas y ",contador1," lletres.")
    print("Cadena 2 tiene ",len(paraules2), " paraulas y ",contador2," lletres.")