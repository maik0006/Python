#Confirmar contraseña
#Maikoll Daniel Torres Fandiño
contraseña = "Maco12392"
longitud_minima = 8

print("Contraseña a validar: ",contraseña)
print("Longitud de contraseña: ",len (contraseña ))

if len(contraseña) >= longitud_minima:
  print("7 La contraseña tiene la longitud correcta")

if contraseña.islower():
 print(" La contraseña debe contener al menos una letra mayúscula")