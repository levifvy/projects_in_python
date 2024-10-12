import time

inicial = time.time()
print("Current UTC Time in seconds:", inicial)

fmt = time.localtime(inicial)
print("Current Formatted Local Time:", fmt)

strf = time.strftime("%D %T", fmt)
print("Current Formatted Local Time:",strf)

final = time.time()

resultat = final - inicial

