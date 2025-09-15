# Suma de números del 1 al 100
#Maikoll Daniel Torres Fandiño
suma_total = 0 
numero_actual = 1
limite = 100

print("Sumando números del 1 al", limite, "...")
while numero_actual <= limite:
    suma_total = suma_total + numero_actual # Acumulamos la suma
    print("Sumando", numero_actual, "- Total hasta ahora:", suma_total)
    numero_actual = numero_actual + 1

print("\nResultado final:")
print("La suma de todos los números del 1 al", limite, "es:", suma_total)