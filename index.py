import random

N = int(input("Tamaño del tablero N (recomendamos usar como maximo 10): "))
cantidad_barcos = int(input("Cantidad de barcos: "))
cantidad_disparos = int(input("Cantidad de disparos: "))

# Generar posiciones de barcos aleatorias
posiciones_posibles = [(fila_tablero, columna_tablero) for fila_tablero in range(N) for columna_tablero in range(N)]
barcos = random.sample(posiciones_posibles, cantidad_barcos)

tablero = [["~"] * N for _ in range(N)]

def mostrar_tablero():
    print("  " + " ".join(str(numero_columna) for numero_columna in range(N)))
    for numero_fila in range(N):
        print(numero_fila, " ".join(tablero[numero_fila]))
    print()

for turno_actual in range(1, cantidad_disparos + 1):
    print("Disparo", turno_actual, "/", cantidad_disparos)
    mostrar_tablero()
    fila_disparo = int(input("Fila: "))
    columna_disparo = int(input("Columna: "))

    if fila_disparo < 0 or fila_disparo >= N or columna_disparo < 0 or columna_disparo >= N:
        print("Posicion no valida")
    elif tablero[fila_disparo][columna_disparo] != "~":
        print("Ya disparate aca")
    else:
        if (fila_disparo, columna_disparo) in barcos:
            tablero[fila_disparo][columna_disparo] = "X"
            barcos.remove((fila_disparo, columna_disparo))
            print("Tocado")
            if len(barcos) == 0:
                print("Ganaste!")
                break
        else:
            tablero[fila_disparo][columna_disparo] = "O"
            print("Agua")

# Tablero final
mostrar_tablero()
