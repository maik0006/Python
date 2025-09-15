#Lista de números hasta que el usuario ponga -1
lista = []
num = int(input("Número (-1 para terminar): "))
while num != -1:
    lista.append(num)
    num = int(input("Número (-1 para terminar): "))
print(lista)

