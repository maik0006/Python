# Eliminar duplicados de una lista usando diccionario
lista = [1, 2, 2, 3, 4, 4, 5]
sin_duplicados = list(dict.fromkeys(lista))
print(sin_duplicados)

