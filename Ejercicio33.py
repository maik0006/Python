#Maikoll Daniel Torres Fandiño
#Juego de la vida de conway-33
import random
import time

def crear_tablero(filas, columnas, densidad=0.3):
    """Crea un tablero inicial con células vivas (1) y muertas (0)."""
    tablero = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            esta_viva = 1 if random.random() < densidad else 0
            fila.append(esta_viva)
        tablero.append(fila)
    return tablero

def contar_vecinos_vivos(tablero, fila, columna):
    """Cuenta cuántos vecinos vivos tiene una célula."""
    filas = len(tablero)
    columnas = len(tablero[0])
    vecinos_vivos = 0
    direcciones = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    for df, dc in direcciones:
        nueva_fila = fila + df
        nueva_columna = columna + dc
        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
            vecinos_vivos += tablero[nueva_fila][nueva_columna]
    return vecinos_vivos

def aplicar_reglas(tablero):
    """Aplica las reglas del Juego de la Vida para generar la siguiente generación."""
    filas = len(tablero)
    columnas = len(tablero[0])
    nuevo_tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
    cambios = []

    for i in range(filas):
        for j in range(columnas):
            vecinos = contar_vecinos_vivos(tablero, i, j)
            celula_actual = tablero[i][j]

            if celula_actual == 1:  # Célula viva
                if vecinos < 2:
                    nuevo_tablero[i][j] = 0
                    cambios.append((i, j, "murió por soledad"))
                elif vecinos > 3:
                    nuevo_tablero[i][j] = 0
                    cambios.append((i, j, "murió por sobrepoblación"))
                else:
                    nuevo_tablero[i][j] = 1  # Sobrevive
            else:  # Célula muerta
                if vecinos == 3:
                    nuevo_tablero[i][j] = 1
                    cambios.append((i, j, "nació"))

    return nuevo_tablero, cambios

def mostrar_tablero(tablero, generacion, mostrar_coordenadas=False):
    """Muestra el tablero en consola."""
    print(f"\nGeneración {generacion}:")
    for i, fila in enumerate(tablero):
        linea = ""
        for j, celula in enumerate(fila):
            if celula == 1:
                linea += "⬛" if not mostrar_coordenadas else f"({i},{j}) "
            else:
                linea += "⬜"
        print(linea)
