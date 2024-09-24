'''5. Llegeix els quatre nombres que conformen una adreça IP, valida si és una IP
correcta i ho escriu.'''
adreca = input("Ingresa una IPv4: ").strip()
validando = adreca.split('.')
counter = 0
enunciado  = False

while counter < len(validando):
    if int(validando[counter]) in range(0,256):
        enunciado = True
    else:
        enunciado = False
        break
    counter += 1

if enunciado:
    print(f"La IP {adreca} es valida")
else:
    print(f"La IP {adreca} no es valida")     
        
