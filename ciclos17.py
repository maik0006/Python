#Buscar mínimo en una lista
lista = [7, 2, 9, 4, 1]
i = 1
minimo = lista[0]
while i < len(lista):
    if lista[i] < minimo:
        minimo = lista[i]
    i += 1
print("Mínimo:", minimo)

