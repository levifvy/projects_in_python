'''16.Mostrar els números primers menors a 100'''

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def primes_less_than_100():
    primes = []
    for num in range(2, 100):
        if is_prime(num):
            primes.append(num)
    print(primes)

primes_less_than_100()
