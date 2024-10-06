'''15.Jugar a endevinar un número'''
import random

def guess_number():
    target = random.randint(1, 100)
    guess = None
    attempts = 0
    
    while guess != target:
        guess = int(input("Adivina un número entre 1 y 100: "))
        attempts += 1
        if guess < target:
            print("Demasiado bajo!")
        elif guess > target:
            print("Demasiado alto!")
    
    print(f"Correcto! Lo adivinaste en {attempts} intentos.")


guess_number()
