'''
xercici 2: Extracció de números de telèfon amb prefix
Objectiu: Escriu una expressió regular per extreure els números de telèfon espanyols amb 
prefix "(93)".
Entrada: (93)2541700, (952)253228, (93)2177017, (958)233517.
'''


# (?<=^|\s|,)\([0-9]+\)[0-9]{5,}(?=$|\s|,|\.)

# Exercici 2: Extracció de números de telèfon amb prefix
# Objectiu: Escriu una expressió regular per extreure els números de telèfon espanyols amb 
# prefix "(93)".
# Entrada: (93)2541700, (952)253228, (93)2177017, (958)233517.
# (93)2541700
# (93)