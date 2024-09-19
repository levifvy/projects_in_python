'''
Exercici 13: Extracció d'enllaços sense protocol 
Objectiu: Escriu un regex per extreure enllaços web que no incloguin el protocol (ex: www). 
Entrada: Visita www.example.com per més informació. 
'''

# [^\/][w]{3}\.[a-z]+\.[a-z]+


'''
Python regex lookbehind and lookahead

(?<=^|\s)w{3}(\.[a-zA-Z0-9]+)+(?=\s|$)
www.google.com.es

www.google.co.uk

el caracter que hi ha abans
(?<=.....) look behind
(?<=\s|^)    per exemple abans del patró espai


el caracter que hi ha despres
(?=.....)look ahead
(?=\s|$)   per exemple despres del patró 

'''