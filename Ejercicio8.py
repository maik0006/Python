#Criterio de una nota
#Maikoll Daniel Torres Fandiño
nota = float(input("Ingrese su nota definitiva de 1 a 10: "))

if nota >= 9.0:
    criterio = "Excelente"
    mensaje = "Felicidades"
elif nota >= 7.0:
    criterio = "Buena"
    mensaje = "Buen trabajo , pero puedes mejorar"
else:
    criterio = "Insuficiente"
    mensaje = "Estudia para la próxima"

print("Tu nota es: ", nota)
print("Tu criterio es: ", criterio)
print("Comentario: ", mensaje)
