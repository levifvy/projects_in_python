'''
Exercici 15: Extracció de coordenades geogràfiques 
Objectiu: Escriu un regex per extreure coordenades en format de graus decimals. 
Entrada: 41.40338, 2.17403.

'''



# (?<=^|\s)(\-{0,1}[1-8?][1-9]{1}\.[0-9]{5}|\-{0,1}90),\s-?(180|1[0-7][0-9]\.[0-9]{5}|[1-9]?[0-9]\.[0-9]{5})(?=$|\s)

# -41.45612, 90.48512

# 41.40338, 2.17403