'''6- El nom d'un fitxer és una cadena que pot tenir el que denominem com una extensió. La extensió son els caràcters que succeeixen al últim punt d'una cadena, volem fer un programa que rebi per paràmetre un nom de fitxer i ens digui la seva extensió, per exemple:
Entrada -->     Sortida 
exercici1.py    'exercici1.py' extensió 'py' 
arxiu.de.text.txt   'arxiu.de.text.txt' extensió 'txt' 
arxiusenseext   'arxiusenseext' no té extensió '''

def obtener_extension(nombre_archivo):
    
    if '.' in nombre_archivo:
        
        return nombre_archivo.split('.')[-1]

    return "no té extensió"

archivo = "arxiusenseext"
extension = obtener_extension(archivo)

if extension == "no té extensió":
    print(f"\'{archivo}\' {extension}")
else:
    print(f"\'{archivo}\' extensió \'{extension}\'")