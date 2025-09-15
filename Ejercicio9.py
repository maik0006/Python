#Juego de adivinanza
#Maikoll Daniel Torres Fandiño
numero_secreto = 9
print("Intenta adivinar el número secreto del 1 al 10")
adivinanza = int(input("Escribe un número: "))

if adivinanza == numero_secreto:
        print("!Felicidades¡ Has adivinado el número secreto: " , numero_secreto)

elif adivinanza < numero_secreto:
        print("Tu número es menor. Intente uno más grande")
else:
        print("Tu número es mayor. Intente uno más pequeño")