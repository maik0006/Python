#Calcular potencia (base^exponente) con multiplicaciones
base, exp = 2, 5
resultado = 1
i = 0
while i < exp:
    resultado *= base
    i += 1
print("Potencia:", resultado)

