'''27. Fes un programa que calculi el màxim comú divisor (mcd) de dos sencers positius. El mcd es el número més gran que divideix exactament ambdós números.'''

def greatest_common_divisor(a, b):
    
    for element in iter(int, 1):  
        if b == 0:
            break
        a, b = b, a % b
    return a


a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))

print(f"El MCD de {a} y {b} es {greatest_common_divisor(a, b)}")
