cadena = input("Entra en la cadena")

print(cadena)
print(type(cadena))

print(cadena[0])
print(cadena[-1])

print(cadena[len(cadena)-1])
print(cadena[-len(cadena)])

print(cadena[-3])

#          range(start, stop, step)
for num in range(10,0,-2):
    print(num)

# start incluido
# stop no incluido