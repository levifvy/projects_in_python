'''23. Escriu un programa que mostri els números parells positius entre 2 i un número qualsevol que introdueixi l'usuari per teclat.'''

def show_even_numbers_up_to():
    
    n = int(input("Introduce un número: "))
    
    for i in range(2, n+1, 2):
        print(i, end=" ")


show_even_numbers_up_to()
