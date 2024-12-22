import random


# Variables globales para los tiempos y otros cálculos
t_0 = []  # Tiempo de llegada
t = []  # Tiempo de proceso
t_i = []  # Tiempo inicial
t_f = []  # Tiempo final
T = []  # Tiempo de servicio
E = []  # Tiempo de espera
I = []  # Índice de servicio
prioridad = []  # Prioridades de los procesos (para algoritmo de Prioridad)
memoria_total = 10000  # Memoria total en unidades
memoria_libre = memoria_total  # Memoria libre disponible
bloques = 10  # Número de bloques en la memoria
fragmentacion_externa = 0  # Fragmentación externa

# Función para agregar un proceso
def agregar(a, b, p=None):
    t_0.append(a)
    t.append(b)
    if p is not None:
        prioridad.append(p)
    completar()

def completar():
    t_i.append("")
    t_f.append("")
    T.append("")
    E.append("")
    I.append("")

def generarTEI_Prom():
    global T, E, I
    for i in range(len(t_0)):
        tt = t[i]
        TT = t_f[i] - t_0[i]
        T[i] = TT
        EE = TT - tt
        if EE < 0:
            EE = 0
        E[i] = EE
        II = round(tt / TT, 2) if TT != 0 else 0
        I[i] = II

def imprimir_resultados2(algoritmo):
    print(f"\nResultados de {algoritmo}:")
    for i in range(len(t_0)):
        # Imprimir la prioridad junto con los demás resultados
        print(f"t_0: {t_0[i]}\t t: {t[i]}\t Prioridad: {prioridad[i]}\t t_i: {t_i[i]}\t t_f: {t_f[i]}\t T: {T[i]}\t E: {E[i]}\t I: {I[i]}")
    
    # Cálculo de promedios
    promedio_t = sum(t) / len(t)
    promedio_T = sum(T) / len(T)
    promedio_E = sum(E) / len(E)
    promedio_I = sum(I) / len(I)

    print(f"\nPromedios de {algoritmo}:")
    print(f" t: {promedio_t:.2f} \t T: {promedio_T:.2f} \t E: {promedio_E:.2f} \t I: {promedio_I:.2f}")

# Función para imprimir resultados
def imprimir_resultados(algoritmo):
    print(f"\nResultados de {algoritmo}:")
    for i in range(len(t_0)):
        print(f"t_0: {t_0[i]}\t t: {t[i]}\t t_i: {t_i[i]}\t t_f: {t_f[i]}\t T: {T[i]}\t E: {E[i]}\t I: {I[i]}")
    
    promedio_t = sum(t) / len(t)
    promedio_T = sum(T) / len(T)
    promedio_E = sum(E) / len(E)
    promedio_I = sum(I) / len(I)

    print(f"\nPromedios de {algoritmo}:")
    print(f" t: {promedio_t:.2f} \t T: {promedio_T:.2f} \t E: {promedio_E:.2f} \t I: {promedio_I:.2f}")

# Algoritmos de Planificación de Procesos

# FIFO: Primer llegado, primer servido
def FIFO():
    global t_0, t, t_i, t_f, T, E, I
    reloj = 1
    fila = 0
    poc = 0
    r = []
    while len(r) < len(t_0):
        t_aux = reloj
        while poc < len(t_0):
            if poc not in r and t_0[poc] <= reloj:
                minimo = t_0[poc]
                fila = poc
                for i in range(poc, len(t_0)):
                    if t_0[i] <= reloj and t_0[i] < minimo and i not in r:
                        minimo = t_0[i]
                        fila = i
                tt_i = reloj
                tt = t[fila]
                tt_f = reloj + tt - 1
                reloj += tt
                t_i[fila] = tt_i
                t_f[fila] = tt_f
                r.append(fila)
                poc = 0
            else:
                poc += 1
        if reloj == t_aux:
            reloj += 1
            poc = 0
    generarTEI_Prom()
    imprimir_resultados("FIFO")

# SJN: Shortest Job Next (El trabajo más corto es ejecutado primero)
def SJN():
    global t_0, t, t_i, t_f, T, E, I
    reloj = 0  # Reloj inicial
    r = []  # Procesos ejecutados

    while len(r) < len(t_0):
        # Buscar el proceso con menor duración que haya llegado
        candidatos = [i for i in range(len(t_0)) if i not in r and t_0[i] <= reloj]
        if candidatos:
            # Elegir el proceso con menor duración
            fila = min(candidatos, key=lambda x: t[x])

            # Calcular tiempos
            t_i[fila] = reloj
            t_f[fila] = reloj + t[fila]
            reloj += t[fila]

            # Agregar el proceso a los realizados
            r.append(fila)
        else:
            reloj += 1  # Avanzar el reloj si no hay procesos disponibles
    # Generar los tiempos y promedios
    generarTEI_Prom1()
    imprimir_resultados("SJN")
def generarTEI_Prom1():
    global T, E, I
    for i in range(len(t_0)):
        # Turnaround Time (Tiempo de servicio)
        T[i] = t_f[i] - t_0[i]
        
        # Tiempo de espera
        E[i] = T[i] - t[i]
        if E[i] < 0:
            E[i] = 0
        
        # Índice de servicio
        if T[i] != 0:
            I[i] = round(t[i] / T[i], 2)
        else:
            I[i] = 0
def Prioridad():
    global t_0, t, t_i, t_f, T, E, I, prioridad
    reloj = 0  # El reloj empieza en 0
    r = []  # Lista de procesos ya ejecutados

    while len(r) < len(t_0):  # Hasta que todos los procesos sean ejecutados
        t_aux = reloj
        fila = -1
        min_prioridad = float('inf')

        # Buscar los procesos que ya han llegado al tiempo actual del reloj
        disponibles = [i for i in range(len(t_0)) if i not in r and t_0[i] <= reloj]

        if disponibles:
            # Mientras haya procesos disponibles, elige el de menor prioridad
            for i in disponibles:
                # Buscar el proceso con menor prioridad entre los disponibles
                if prioridad[i] < min_prioridad:
                    min_prioridad = prioridad[i]
                    fila = i

            # Ejecutar el proceso con la menor prioridad
            if fila != -1:
                tt_i = reloj  # Tiempo de inicio del proceso
                tt = t[fila]  # Tiempo de ejecución del proceso
                tt_f = reloj + tt  # Tiempo de finalización del proceso (no es necesario restar 1)
                reloj += tt  # Avanzar el reloj con el tiempo de ejecución

                t_i[fila] = tt_i
                t_f[fila] = tt_f
                T[fila] = tt_f - t_0[fila]  # Tiempo total de ejecución
                E[fila] = tt_i - t_0[fila]  # Tiempo de espera
                I[fila] = round(tt / T[fila], 2) if T[fila] != 0 else 0  # Índice de eficiencia

                r.append(fila)  # Agregar el proceso a la lista de ejecutados
        else:
            # Si no hay procesos disponibles, avanza el reloj
            reloj += 1

    generarTEI_Prom()  # Función para generar el promedio de T, E, I
    imprimir_resultados2("Prioridad")  # Imprimir los resultados


# Función para leer los procesos
def leer_procesos(entrada_usuario=False, algoritmo="FIFO"):
    print("Generando procesos de prueba...")
    if entrada_usuario:
        num_procesos = int(input("¿Cuántos procesos deseas ingresar? "))
        for i in range(num_procesos):
            print("ti.")
            a = int(input())
            print("tiempo de cpu")
            b = int(input())
            if algoritmo == "Prioridad":
                print("prioridad")
                p = int(input())
                agregar(a, b, p)
            else:
                agregar(a, b)
    else:
        tiempo_llegada = [0,0,1,1,2]
        tiempos_cpu = [2,1,3,2,1]  
        prioridades = [4,4,4,4,4]# Opcional: prioridades predefinidas


        #tiempo_llegada = [21, 38, 98, 26, 39, 7, 34, 29, 50, 74, 28, 30, 37, 46, 100, 3, 44, 72, 93, 1, 23, 63, 80, 50, 32, 44, 60, 95, 77, 51, 45, 63, 19, 48, 54, 88, 64, 11, 87, 11, 62, 29, 24, 54, 98, 64, 21, 7, 91, 17, 55, 87, 95, 57, 28, 14, 45, 0, 11, 8, 8, 22, 93, 95, 28, 93, 91, 39, 88, 58, 61, 89, 33, 31, 37, 22, 95, 88, 68, 63, 54, 72, 1, 75, 10, 80, 38, 32, 66, 30, 43, 39, 15, 60, 66, 95, 98, 40, 51, 51]
        #tiempos_cpu = [8, 13, 3, 17, 13, 19, 10, 20, 12, 6, 17, 11, 20, 7, 13, 5, 9, 5, 13, 1, 6, 20, 6, 2, 10, 13, 14, 8, 1, 9, 4, 8, 17, 12, 18, 7, 6, 5, 3, 10, 1, 6, 15, 2, 4, 14, 16, 20, 15, 4, 20, 7, 3, 20, 7, 8, 7, 3, 1, 17, 6, 20, 17, 16, 3, 2, 4, 11, 19, 13, 9, 9, 9, 20, 15, 9, 2, 16, 3, 15, 11, 13, 2, 12, 10, 1, 15, 13, 13, 2, 5, 14, 4, 20, 3, 7, 7, 20, 12, 6]
        # Opcional: prioridades predefinidas
        #prioridades = [5, 9, 8, 1, 4, 4, 2, 7, 1, 9, 4, 5, 9, 2, 7, 2, 7, 1, 10, 8, 9, 2, 5, 8, 9, 6, 2, 7, 5, 2, 4, 1, 4, 4, 10, 6, 4, 5, 6, 9, 9, 2, 2, 9, 9, 10, 6, 10, 9, 7, 9, 2, 2, 8, 5, 3, 6, 5, 10, 7, 7, 3, 1, 5, 9, 10, 3, 2, 2, 4, 1, 4, 9, 9, 4, 9, 10, 9, 5, 3, 4, 2, 9, 3, 1, 9, 5, 6, 2, 5, 5, 9, 4, 9, 6, 4, 1, 1, 4, 3]
        algoritmo = "Prioridad"  # Cambiar según el algoritmo que uses

        # Usar las listas predefinidas
        for i in range(len(tiempo_llegada)):  # Iterar según la longitud de las listas
            a = tiempo_llegada[i]
            b = tiempos_cpu[i]
    
            if algoritmo == "Prioridad":
                p = prioridades[i]  # Usar prioridad correspondiente
                agregar(a, b, p)
            else:
                agregar(a, b)

# Ejecución
def ejecutar_simulacion():
    algoritmo = input("Elija el algoritmo a ejecutar (FIFO, SJN, Prioridad): ").strip()
    entrada_usuario = input("¿Quieres ingresar los datos manualmente? (s/n): ").strip().lower() == "s"

    leer_procesos(entrada_usuario, algoritmo)

    if algoritmo == "1":
        FIFO()
    elif algoritmo == "2":
        SJN()
    elif algoritmo == "3":
        Prioridad()
    else:
        print("Algoritmo no válido. Intente nuevamente.")



# Ejecutar la simulación
ejecutar_simulacion()
