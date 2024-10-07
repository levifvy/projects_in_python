'''24. Fes un programa que demani el valor de dos sencers n i m i que mostri per pantalla el valor de la suma dels seus quadrats. Has d'utilitzar un bucle for in pel càlcul del sumatori.'''

def sum_of_squares(n, m):
    sum = [n,m]
    result = 0
    for element in sum:
        result += element**2
    return result


n = int(input("Introduce el valor de n: "))
m = int(input("Introduce el valor de m: "))
print(f"La suma de los cuadrados es: {sum_of_squares(n, m)}")
