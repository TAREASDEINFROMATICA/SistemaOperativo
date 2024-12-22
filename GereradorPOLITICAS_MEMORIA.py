import random

# Generar 1000 procesos aleatorios
num_procesos = 1000
procesos = [random.randint(10, 90) for _ in range(num_procesos)]

# Generar 1000 bloques de memoria
num_bloques = 1000
memoria = [random.randint(100, 400) for _ in range(num_bloques)]

procesosA = ["S/A"] * num_bloques
ocupado = [False] * num_bloques

# Imprimir todos los procesos y bloques de memoria en una sola línea
print("procesos:",procesos)
print("memoria:",memoria)
