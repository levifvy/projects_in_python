'''
Exercici 5: Extracció de preus en format decimal
Objectiu: Escriu un regex per trobar preus amb decimals en una cadena de text.
Entrada: Els preus dels productes són 10.99€, 20€, 100.50€, i 300.00€
'''

# [0-9]*\.[0-9]*€


# [0-9]*[\.,]{1}[0-9]*€

# \s[0-9]*[\.,]{1}[0-9]*€