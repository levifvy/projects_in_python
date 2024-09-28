
def odernada(llista):
    #1. toma una lista de numero y retorna otra lista ordenada
    resultat = llista[:]
    resultat.sort()
    return resultat

def suma(llista):
    # 2. suma los valores dentro de la lista
    resultat = llista[:]
    sumatorio = 0
    for element in resultat:
        sumatorio = sumatorio + element
    return sumatorio


def suma_cuadrados(llista):
    # 3. suma los cuadrados de los elementos de la lista
    resultat = llista[:]
    sumatorio = 0
    for element in resultat:
        sumatorio += (element**2)
    return sumatorio


def suma_cubos(llista):
    # 4. suma los cubos de los elementos de la lista
    resultat = llista[:]
    sumatorio = 0
    for element in resultat:
        sumatorio = sumatorio + (element**3)
    return sumatorio


def minimo(llista):
    # 5. retorna el valor minimo de la lista
    resultat = llista[:]
    minim = resultat[0]
    for num in resultat[1:]:
        if num < minim:
            minim = num
    return minim


def maximo(llista):
    # 6. retorna el valor maximo de la lista
    resultat = llista[:]
    maxim = resultat[0]
    for num in resultat[1:]:
        if num > maxim:
            maxim = num
    return maxim


def revertir(llista):
    # 7. retorna la lista en orden invertido
    resultat = llista[:]
    resultat.reverse()
    return resultat


def posicio_parell(llista):
    # 8. retorna una lista con los elementos en posicio par de la lista
    resultat = llista[:]
    posicionsparells = []
    for posicio in range(0,len(resultat),2):
        posicionsparells.append(resultat[posicio])
    return posicionsparells


def posicio_senars(llista):
    # 9. retorna una lista con los elementos en posicio impar 
    # de la lista
    resultat = llista[:]
    posicionsparells = []
    for posicio in range(len(resultat)):
        if posicio % 2 == 1:
            posicionsparells.append(resultat[posicio])
    return posicionsparells


def cantidad_digits(llista):
    # 10. recibe como parametro una lista de numeros,
    #  retorna otra lista indicando cuantos digitos tiene cada elemento
    resultat = llista[:]
    numdigits = []
    for num in resultat:
        num =str(num).replace("-","")
        numdigits.append(len(num))
    return numdigits


def cantidad_caracters(llista):
    # 11. recibe por parametro una lista de cadenas 
    # y retorna otra lista con la cantidad de caracteres de cada cadena
    longituds = []
    for i in llista:
        longituds.append(len(i))
    return(longituds)


def convertir_minuscules(llista):
    # 12. recibe una lista de cadenas y 
    # retorna otra lista con las cadenas en minusculas
    longituds = []
    for i in llista:
        longituds.append(i.lower())
    return(longituds)

def convertir_majuscules(llista):
    # 13. recibe una lista de cadenas 
    # y retorna otra lista con las cadenas en mayuscaulas
    longituds = []
    for i in llista:
        longituds.append(i.upper())
    return(longituds)

def concatenacio_caracteres(llista):
    # 14. recibe una lista y retorna una unica cadena 
    # - con todos los caracteres concatenados
    resultado = ""
    for cadena in llista:
        resultado += cadena
    return resultado

def ordenacio_cadenas_alfabeticamente(llista_cadenes):
    # 15. recibe una lista de cadenas 
    # y retorna otra lista con las cadenas ordenadas alfabeticamente
    replica = llista_cadenes[:]
    replica.sort()
    return replica

def cadenes_posicio_parelles(llista):
    # 16. recibe una lista por parametro
    # - y retorna otra lista con las cadenas en posicio parell
    resultat = []
    for posicio in range(0,len(llista),2):
        resultat.append(llista[posicio])
    return resultat


def cadenes_posicio_senars(llista):
    # 17. recibe una lista por parametro
    # - y retorna otra lista con las cadenas en posicio parell
    resultat = []
    for posicio in range(1,len(llista),2):
        resultat.append(llista[posicio])
    return resultat

def no_last_caracter(llista_cadenes):
    # 18. recibe una lista de cadenas
    #- y deveulve otra lista de las mismas cedenas sin el ultimo caracter
    resultat = []
    for element in llista_cadenes:
        resultat.append(element[0:len(element)-1])
    return resultat

def no_first_caracter(llista_cadenes):
    # 19. recibe una lista de cadenas
    #- y deveulve otra lista de cedenas sin el primer caracter
    resultat = []
    for element in llista_cadenes:
        resultat.append(element[1:len(element)])
    return resultat

def inversion_cadena(cadena):
    # 20.1 recibe una cadena por parametro
    # y devuelve otra cadena con sus caracteres invertidos
    resultat = ''
    for char in cadena:
        resultat = char + resultat
    return resultat

def inversio(llista_cadenes):
    # 20.2 recibe una lista de cadenas
    #- y en cada posicion invierte el orden de los
    #- caracteres de cada cadena con la funcion inversion_cadena
    invertida = []
    for element in llista_cadenes:
        invertida.append(inversion_cadena(element))
    return invertida