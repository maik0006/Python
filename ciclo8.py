#Adivinar número secreto
secreto = 7
num = int(input("Adivina el número: "))
while num != secreto:
    num = int(input("Intenta de nuevo: "))
print("¡Correcto!")

