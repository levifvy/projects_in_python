'''3- Amb la funció strftime del mòdul time pots construir una cadena amb la data i l'hora actual amb el següent format, "dd/mm/yyyy hh:mm:ss"

NOTA: pots cercar informació a la web de http://www.python.org , ves a "Documentation --> Search the online docs" aquí cerca per time i enllaça amb "time — Time access and conversions" aquí veuras totes les funcions del mòdul time que podràs fer servir si fas un import d'aquest mòdul.

Crea una cadena amb la data i l'hora actual amb el format especificat anteriorment i extrau d'aquesta cadena els següents valors per escriure per pantalla el següent:

El dia : dd 
El mes : mm 
L'any : yyyy 
L'hora : hh:mm:ss
'''

import time

def extraer_fecha_hora():
    
    fecha_hora_actual = time.strftime("%d/%m/%Y %H:%M:%S")
    
    fecha, hora = fecha_hora_actual.split()  
    
    dia, mes, año = fecha.split('/')  
    
    return dia, mes, año, hora

dia, mes, año, hora = extraer_fecha_hora()

print(f"El dia : {dia}")
print(f"El mes : {mes}")
print(f"L'any : {año}")
print(f"L'hora : {hora}")
