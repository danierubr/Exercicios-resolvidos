lista = list()

for x in range(0, 100):
    y = int(input())
    lista.append(y)

print(lista)
print(max(lista))
print(lista.index(max(lista)) + 1)
