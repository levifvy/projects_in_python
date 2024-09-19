'''
Exercici 19: Validació d'horaris
Objectiu: Escriu un regex per validar horaris en format HH:MM (de 24 hores).
Entrada: 14:30, 02:59, 25:00.
'''
# Respuestas:
# (?<=^|\s)([0-1][0-9]|2[0-3]):[0-5][0-9](?=$|\s)
# (?<=^|\s|,)([0-1][0-9]|2[0-3]):[0-5][0-9](?=$|\s|,) → al lado de comas

# Exercici 19: Validació d'horaris
# Objectiu: Escriu un regex per validar horaris en format HH:MM (de 24 hores).


# Entrada: 
# 14:30 , 
# 02:59 , 
# 25:00 .
# 74:25
# 13:26
# 13:36
# 13:66
# 09:26,22:51

# lookbehind i lookahead regex

# (?<=^|\s) ... (?=$|\s)