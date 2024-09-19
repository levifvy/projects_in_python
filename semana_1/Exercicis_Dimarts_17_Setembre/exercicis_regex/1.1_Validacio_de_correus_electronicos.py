# regex101.com
'''
Exercici 1: Validació de correus electrònics
Objectiu: Escriu una expressió regular per validar correus electrònics simples.
Entrada: hola@test.com, josep.puigdemont@company.cat, marta123@xyz.org, persona@.
'''



# (?<=^|\s|,)[a-z0-9]+\.?[a-z0-9]+@[a-z0-9]+\.[a-z0-9]+(?=$|\s|,|.)

# Exercici 1: Validació de correus electrònics
# Objectiu: Escriu una expressió regular per validar correus electrònics simples.
# Entrada: hola@test.com, josep.puigdemont@company.cat, marta123@xyz.org, persona@.

# (?<=^|\s) ... (?=$|\s)

# josep.puigdemont@company.cat

# genaro.12321@hlkj.cat

# vadsfga1313.asfg@gmail.com

# vadsfgaAD1313.asfg@gmail.com

# genaro12321@hlkj.cat