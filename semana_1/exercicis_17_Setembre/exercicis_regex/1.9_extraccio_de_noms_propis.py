'''
Exercici 9: Extracció de noms propis 
Objectiu: Escriu un regex per extreure noms propis d'una frase (inicien amb majúscula). 
Entrada: Maria va anar a Barcelona amb Josep i Anna. 
'''

# tentando
# [A-Z]{1}[^\s()\/\\"@0-9:]+