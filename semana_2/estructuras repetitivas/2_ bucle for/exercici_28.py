'''28.Fes un programa que llegeixi els minuts i els segons i realitzi un compte enrere.'''

import time

def countdown(minutes, seconds):
    total_seconds = minutes * 60 + seconds
    
    for total_seconds in range(total_seconds, 0, -1):
        mins, secs = divmod(total_seconds, 60)
        print(f"{mins:02}:{secs:02}")
        time.sleep(1)
    
    print("¡Tiempo finalizado!")

moment = input("Introduce los minutos y segundos(mm:ss): ")

result = moment.split(':')

minutes = int(result[0])
seconds = int(result[1])

countdown(minutes, seconds)

