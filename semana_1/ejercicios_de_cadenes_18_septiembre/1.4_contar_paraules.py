'''4-Comptar paraules:
Compta el número de paraules que hi ha dins d'una cadena de text que li passeu per paràmetre (les paraules sempre estan separades per un o més espais en blanc)
Nota: Exemple de com passar un paràmetre amb espais user-bash$ python comptaparaules.py 'Python is a dynamic object-oriented programming language' '''

cadena = 'Python is a dynamic object-oriented programming language'

paraules = cadena.split(" ")

print(len(paraules))


