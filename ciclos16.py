#Contar dígitos de un número
num = 12345
contador = 0
while num > 0:
    num //= 10
    contador += 1
print("Dígitos:", contador)


