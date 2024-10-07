'''21. Realitza un programa que proporcioni el desglossament en bitllets i monedes d'una quantitat sencera d'euros. Recorda que hi ha bitllets de 500, 200, 100, 50, 20, 10 i 5 e y monedas de 2 y 1 e. Has de “recórrer” els valors de bitllet i moneda disponibles amb un o més bucles for-in.'''

def currency_breakdown(euros):
    bills = [500, 200, 100, 50, 20, 10, 5]
    coins = [2, 1]
    result = {}
    
    for bill in bills:
        if euros >= bill:
            result[bill] = euros // bill
            euros %= bill
            
    for coin in coins:
        if euros >= coin:
            result[coin] = euros // coin
            euros %= coin
    
    return result


euros = int(input("Introduce la cantidad en euros: "))

desglose = currency_breakdown(euros)

for denom, count in desglose.items():
    print(f"{count} billetes/monedas de {denom}€")
