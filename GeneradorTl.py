import random
m=1000 #con este decidmos cuantos podemos generar#
num_procesos = 1000  # Numero de procesos a generar
rango_llegada = (0, 100)  # Rango para los tiempos de llegada
rango_servicio = (1, 20)  # Rango para los tiempos de CPU
prioti=(1,10) #valor de prioirdad 

# Generación de datos en vectores
tiempos_llegada = [random.randint(*rango_llegada) for _ in range(num_procesos)]
tiempos_servicio = [random.randint(*rango_servicio) for _ in range(num_procesos)]
prioridad = [random.randint(*prioti) for _ in range(num_procesos)]

num_procesos = m
procesos = [random.randint(10, 90) for _ in range(num_procesos)]
# Generar 1000 bloques de memoria
num_bloques = m
memoria = [random.randint(100, 200) for _ in range(num_bloques)]
procesosA = ["S/A"] * num_bloques
ocupado = [False] * num_bloques
# Mostrar los primeros 10 elementos de cada vector como ejemplo
print("t_legadoa= ", tiempos_llegada[:m])
print("t_cpu = ", tiempos_servicio[:m])
print("t_priodidad = ", prioridad[:m])
# Imprimir todos los procesos y bloques de memoria en una sola línea
print("procesos:",procesos)
print("memoria:",memoria)