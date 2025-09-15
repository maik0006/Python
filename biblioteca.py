from datetime import date


libros = []
usuarios = []
prestamos = []


def registrar_libro(titulo, autor):
    libro = {"id": len(libros)+1, "titulo": titulo, "autor": autor, "disponible": True}
    libros.append(libro)
    print(f"Libro registrado: {titulo}")

def registrar_usuario(nombre):
    usuario = {"id": len(usuarios)+1, "nombre": nombre}
    usuarios.append(usuario)
    print(f" Usuario registrado: {nombre}")

def prestar_libro(id_libro, id_usuario):
    for libro in libros:
        if libro["id"] == id_libro and libro["disponible"]:
            libro["disponible"] = False
            prestamo = {
                "libro": libro["titulo"],
                "usuario": next(u["nombre"] for u in usuarios if u["id"] == id_usuario),
                "fecha": str(date.today())
            }
            prestamos.append(prestamo)
            print(f"Prestamo registrado: {prestamo}")
            return
    print("❌ Libro no disponible o no encontrado.")


registrar_libro("Cien Años de Soledad", "Gabriel García Márquez")
registrar_libro("Don Quijote", "Miguel de Cervantes")

registrar_usuario("Ana")
registrar_usuario("Luis")

prestar_libro(1, 1)
prestar_libro(2, 2)

print("\n Prestamos realizados:")
for p in prestamos:
    print(p)
