'''
Exercici 7: Detecció de URLs 
Objectiu: Escriu un regex per extreure URLs d'una cadena de text. 
Entrada: Visita https://www.example.com per més informació o http://test.org. També 
pots anar a www.google.com
'''

# https:\/\/w{3}\.[a-z]+.[a-z]+|http:\/\/[a-z]+\.[a-z]+|w{3}\.[a-z]+\.[a-z]+

# h?t?t?p?s?:?\/?\/?[a-z]+\.[a-z]+\.

# h?t?t?p?s?:?\/?\/?[a-z]+\.[a-z]*\.

# [htpsw]+[:\/.]+[a-z]+[:\/.]+[a-z]+.?[a-z]+

# (http[s]?:\/\/|(w{3})){1}[a-zA-Z\.]*[\.]?[a-z]+