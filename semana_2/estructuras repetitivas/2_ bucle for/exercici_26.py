'''26.Fes un programa que llegeixi un número i ens mostri els números primers menors que ell (amb bucles for in)'''

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def primes_less_than_n():
    n = int(input("Introduce un número: "))
    for i in range(2, n):
        if is_prime(i):
            print(i, end=" ")


primes_less_than_n()
