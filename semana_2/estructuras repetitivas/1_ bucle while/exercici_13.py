''' 13.Multiplicar dos sencers en base a sumes successives '''

def multiply_by_addition(a, b):
    result = 0
    for _ in range(abs(b)):  
        result += a
    return result if b >= 0 else -result 


print(multiply_by_addition(5, 3)) 