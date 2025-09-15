#Validar contraseña
clave = "1234"
ingreso = input("Contraseña: ")
while ingreso != clave:
    ingreso = input("Incorrecta. Intenta otra vez: ")
print("Acceso permitido")

