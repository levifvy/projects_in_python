''' 3- Resoldre la lletra del DNI:
La última letra del DNI puede calcularse a partir de sus números. Para ello sólo tienes que dividir el número por 23 y quedarte con el resto. El resto es un número entre 0 y 22. La letra que corresponde a cada número la tienes en esta tabla:
--------------------------------------------------------------
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
T R W A G M Y F P D X B N J Z S Q V H L C K E
--------------------------------------------------------------
Diseña un programa que reciba por parámetro un número de DNI y muestre en pantalla la letra que le corresponde.
(Nota: una implementación basada en tomar una decisiónn con if -elif conduce a un programa muy largo. Si usas el operador de indexación de cadenas de forma inteligente, el programa apenas ocupa 3 líneas , piensa como)'''

caracteres = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]


dni = (int)(input("Ingresa el DNI: "))
indice = dni%23
print(caracteres[indice])

