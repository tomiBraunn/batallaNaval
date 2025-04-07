import random

disparos = 10
barcos = 3


tamaño = int(input("¿De qué tamaño querés el tablero?: "))

tablero_oculto = []
tablero_jugador = []

for fila_num in range(tamaño):
    fila_barcos = []
    fila_visible = []

    for columna_num in range(tamaño):
        fila_barcos += [False]
        fila_visible += [" "]

    tablero_oculto += [fila_barcos]
    tablero_jugador += [fila_visible]

barcos_colocados = 0
while barcos_colocados < barcos:
    fila_azar = random.randint(0, tamaño - 1)
    columna_azar = random.randint(0, tamaño - 1)
    if tablero_oculto[fila_azar][columna_azar] == False:
        tablero_oculto[fila_azar][columna_azar] = True
        barcos_colocados += 1

while disparos > 0:
    for fila in tablero_jugador:
        print(fila)

    fila_disparo = int(input("fila: "))
    columna_disparo = int(input("columna: "))

    if 0 <= fila_disparo < tamaño and 0 <= columna_disparo < tamaño:
        if tablero_oculto[fila_disparo][columna_disparo] == True:
            tablero_oculto[fila_disparo][columna_disparo] = False
            tablero_jugador[fila_disparo][columna_disparo] = "X"
            barcos -= 1
            if barcos == 0:
                print("Hundiste todos los barcos.")
                break
        else:
            tablero_jugador[fila_disparo][columna_disparo] = "O"
        disparos -= 1
        print("Te quedan", disparos, "disparos.")

if barcos > 0:
    print("No hundiste todos los barcos")

print("Tablero final:")
for fila in tablero_jugador:
    print(fila)
