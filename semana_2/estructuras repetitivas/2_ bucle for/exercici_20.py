'''20.Fes un programa que mostri la taula de multiplicar d'un nú́mero introduït per teclat per l'usuari. Aquí tens un exemple de com s'ha de comportar el
programa:
Dóna'm un número: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50'''

def multiplication_table_user_input():
    number = int(input("Dóna'm un número: "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


multiplication_table_user_input()
