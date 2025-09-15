# Organizador de lista
numeros = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42]

print("Lista original:", numeros)
print("Cantidad de elementos:", len(numeros))

numeros_ascendente = numeros.copy()
numeros_descendente = numeros.copy()

numeros_ascendente.sort() 
print("\nOrdenada ascendente:", numeros_ascendente)

numeros_descendente.sort(reverse=True) 
print("Ordenada descendente:", numeros_descendente)

import random 
numeros_mezclados = numeros.copy()
random.shuffle(numeros_mezclados) 
print("Lista mezclada:", numeros_mezclados)

numeros_invertidos = numeros.copy()
numeros_invertidos.reverse() 
print("Orden invertido:", numeros_invertidos)
print("\nLista original (sin cambios):", numeros)