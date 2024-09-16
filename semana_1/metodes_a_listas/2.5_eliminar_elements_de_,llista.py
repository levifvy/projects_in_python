llista = [1,2,3]
llista.clear()
print(llista)

llista = [1,2,1,3,1,4]
llista.remove(1)
print(llista)

llista.remove(1)
print(llista)

llista.remove(1)
print(llista)

try:
    llista.remove(1)
except ValueError:
    pass
print(llista)

llista.pop(1)
print(llista)

llista.pop(1)
print(llista)

try:
    llista.pop(1)
except  IndexError:
    pass
print(llista)