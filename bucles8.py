#Contar vocales
palabra = "programacion"
contador = 0
for c in palabra:
    if c in "aeiou":
        contador += 1
print("Vocales:", contador)

