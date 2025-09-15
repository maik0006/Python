#Juego: adivina palabra
secreta = "python"
palabra = input("Adivina la palabra: ")
while palabra != secreta:
    palabra = input("Incorrecto, intenta otra vez: ")
print("¡Ganaste!")