#Calcular promedio hasta que usuario escriba -1
suma = 0
count = 0
num = int(input("Número (-1 para terminar): "))
while num != -1:
    suma += num
    count += 1
    num = int(input("Número (-1 para terminar): "))
if count > 0:
    print("Promedio:", suma/count)

