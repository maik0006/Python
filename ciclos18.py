#Contar letras "a" en cadena
texto = "programacion"
i = 0
contador = 0
while i < len(texto):
    if texto[i] == "a":
        contador += 1
    i += 1
print("Cantidad de 'a':", contador)

