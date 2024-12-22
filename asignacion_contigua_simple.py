import random

# MENÚ INTERACTIVO
def menu():
    print("===== MENÚ DE GESTIÓN DE MEMORIA =====")
    print("1. Generar 1000 procesos y bloques de memoria aleatorios y ejecutar los algoritmos")
    print("2. Ingresar procesos y bloques de memoria manualmente y ejecutar los algoritmos")
    print("5. Salir")
    
    while True:
        try:
            opcion = int(input("Selecciona una opción (1-5): "))
            if opcion == 1:
                generar_datos_aleatorios_y_ejecutar_algoritmos()
            elif opcion == 2:
                ingresar_datos_y_ejecutar_algoritmos()
            elif opcion == 5:
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Función para generar datos aleatorios
def generar_datos_aleatorios_y_ejecutar_algoritmos():
    global procesos, memoria, procesosA, ocupado
    ##
    ##
    ##EN ESTE PONEMOS LOS 1000 
    ##
    ##
    procesos = [10000, 10, 10, 10, 1000]
    memoria = [50, 100, 180, 250, 100]
    
    inicializar_variables_auxiliares()
    seleccionar_algoritmo()

# Función para ingresar datos manualmente
def ingresar_datos_y_ejecutar_algoritmos():
    global procesos, memoria, procesosA, ocupado
    num_procesos = int(input("Ingresa el número de procesos: "))
    num_bloques = int(input("Ingresa el número de bloques de memoria: "))
    
    procesos = [int(input(f"Ingresa el tamaño del proceso {i+1} (MB): ")) for i in range(num_procesos)]
    memoria = [int(input(f"Ingresa el tamaño del bloque {i+1} (MB): ")) for i in range(num_bloques)]
    
    print("\nProcesos ingresados:", procesos)
    print("Memoria ingresada:", memoria)
    
    inicializar_variables_auxiliares()
    seleccionar_algoritmo()

# Inicializar variables auxiliares para los algoritmos
def inicializar_variables_auxiliares():
    global procesosA, ocupado
    procesosA = ["S/A"] * len(memoria)  # Inicialmente, ningún proceso está asignado
    ocupado = [False] * len(memoria)    # Inicialmente, ningún bloque está ocupado

# Selección de algoritmo
def seleccionar_algoritmo():
    print("\nSelecciona el algoritmo que deseas ejecutar:")
    print("1. Asignación contigua simple")
    while True:
        try:
            opcion_algoritmo = int(input("Selecciona el algoritmo (1): "))
            if opcion_algoritmo == 1:
                asignacion_contigua_simple()
            else:
                print("Opción no válida. Intenta de nuevo.")
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Funciones de los algoritmos
def asignacion_contigua_simple():
    print("\n======================= Asignación Contigua Simple =======================")
    memoria_total = sum(memoria)
    espacio_usado = 0
    trabajos_postergados = 0

    for peticion in procesos:
        if espacio_usado + peticion <= memoria_total:
            espacio_usado += peticion
        else:
            trabajos_postergados += 1

    fragmentacion_externa = memoria_total - espacio_usado
    porcentaje_uso = (espacio_usado / memoria_total) * 100
    nivel_multiprogramacion = len(procesos) - trabajos_postergados

    print(f"Fragmentación externa: {fragmentacion_externa}MB")
    print(f"Porcentaje de uso de memoria: {porcentaje_uso:.2f}%")
    print(f"Nivel de multiprogramación: {nivel_multiprogramacion}")
    print(f"Trabajos postergados: {trabajos_postergados}")
# Llamada al menú principal
menu()
