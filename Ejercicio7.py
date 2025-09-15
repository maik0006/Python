#Descuento en una compra
#Maikoll Daniel Torres Fandiño
precio = int(input("Ingrese el precio de la compra(Sin puntos): "))
descuento = 0

if precio > 100000:
    descuento = precio * 0.10
    precio_total = precio - descuento
    print("Por el valor de su compra obtuvo un descuento del 10 %", "Vuelva pronto.")

else:
    precio_total = precio
    print("No obtuvo descuento, por favor vuelva pronto.")

print("El precio original de su compra es: ", precio)
print("El precio total es:", precio_total)

