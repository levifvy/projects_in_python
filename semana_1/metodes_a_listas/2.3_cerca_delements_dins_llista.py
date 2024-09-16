llista1=[1,2,3,4,5]

print(llista1.count(5))

print(llista1.index(5))

try:
    print(llista1.index(6))
except:
    print("L'element no es troba a la llista")

print(4 in llista1)