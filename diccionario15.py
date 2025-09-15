#Contar palabras en una frase
frase = "hola hola mundo mundo mundo python"
contador = {}
for palabra in frase.split():
    contador[palabra] = contador.get(palabra, 0) + 1
print(contador)

