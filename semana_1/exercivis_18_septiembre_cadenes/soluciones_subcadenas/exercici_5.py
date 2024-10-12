'''5- Llegir un verb en infinitiu i dir quina és la seva conjugació, per exemple:
Entrada -->  Sortida 
cantar 1 'cantar' 
caure 2 'caure' 
saber 2 'saber' 
tenir 3 'tenir' 
cantava 'cantava' no té conjugació
'''
def identificar_conjugacio(verb):
    if verb.endswith("ar"):
        return f"{verb} 1 '{verb}'"
    elif verb.endswith("er") or verb.endswith("re"):
        return f"{verb} 2 '{verb}'"
    elif verb.endswith("ir"):
        return f"{verb} 3 '{verb}'"
    else:
        return f"'{verb}' no té conjugació"


verbs = ["cantar", "caure", "saber", "tenir", "cantava"]
for verb in verbs:
    print(identificar_conjugacio(verb))

