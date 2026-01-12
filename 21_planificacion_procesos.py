# Archivo: 21_planificacion_procesos.py
# Descripción: Algoritmo de planificación de procesos FCFS (First Come First Served)

from operator import itemgetter

try:
    from tabulate import tabulate  # type: ignore[reportMissingModuleSource]
    TABULATE_AVAILABLE = True
except ImportError:
    TABULATE_AVAILABLE = False
    print("Nota: tabulate no está instalado. Usando formato simple para tablas.")

print("=== Planificación de Procesos FCFS ===\n")

# Versión 1: Original (con comentarios)
print("=== Versión 1: Original ===")
def planificacion_original():
    """
    Versión original del código.
    Simula algoritmo FCFS (First Come First Served).
    """
    procesos = [
        {'t-llegada': 0, 'rafaga': 10},
        {'t-llegada': 2, 'rafaga': 12},
        {'t-llegada': 4, 'rafaga': 5},
        {'t-llegada': 3, 'rafaga': 6},
        {'t-llegada': 1, 'rafaga': 24}
    ]
    
    cantidad_procesos = len(procesos)
    
    if cantidad_procesos > 0:
        print('--------- ORDENAMOS LOS PROCESOS SEGÚN SU TIEMPO DE LLEGADA ---------')
        
        procesos_ordenados = sorted(procesos, key=itemgetter('t-llegada'))
        
        tiempoRespuesta = 0
        totalTR = []
        tabla_procesos = []

        for proceso in procesos_ordenados:
            t_llegada = proceso['t-llegada']
            rafaga = proceso['rafaga']
            tiempoRespuesta += rafaga
            tabla_procesos.append([t_llegada, tiempoRespuesta])
            
            totalTR.append(tiempoRespuesta)
        
        # Mostrar resultados en tabla
        if TABULATE_AVAILABLE:
            headers = ["Proceso con tiempo de llegada #", "Tiempo de respuesta"]
            tabla_resultados = tabulate(tabla_procesos, headers=headers, tablefmt="grid")
            print(tabla_resultados)
        else:
            print("Tiempo de llegada | Tiempo de respuesta")
            print("-" * 40)
            for fila in tabla_procesos:
                print(f"{fila[0]:^18} | {fila[1]:^20}")

        contador = 0
        tiempoEspera = []
        
        for te in totalTR:
            contador += 1
            val = te - contador
            tiempoEspera.append(val)
        
        tiempoEspera = tiempoEspera[:-1]
        tiempoEspera.append(0)
        tiempoEspera.sort()
        
        sumatoriaTE = sum(tiempoEspera)
        sumatoriaTR = sum(totalTR)
        
        promedioTE = sumatoriaTE / len(procesos_ordenados)
        promedioTR = sumatoriaTR / len(procesos_ordenados)
        
        print(f'El tiempo de espera {tiempoEspera} promedio es de: {promedioTE} ut.')
        print(f'El tiempo de respuesta {totalTR} promedio es de: {promedioTR} ut.')
    else:
        print('El número de procesos debe ser mayor a 0 (cero) para poder probar el algoritmo.')

# planificacion_original()

# Versión 2: Corregida (Lógica FCFS correcta)
print("=== Versión 2: Corregida (Lógica FCFS Correcta) ===")
def planificacion_fcfs_corregida(procesos):
    """
    Algoritmo FCFS con lógica corregida.
    
    Tiempo de respuesta (TR) = Tiempo de finalización - Tiempo de llegada
    Tiempo de espera (TE) = Tiempo de respuesta - Ráfaga
    """
    if not procesos:
        print('Error: La lista de procesos está vacía')
        return None
    
    # Ordenar por tiempo de llegada
    procesos_ordenados = sorted(procesos, key=itemgetter('t-llegada'))
    
    tiempo_actual = 0
    resultados = []
    
    for proceso in procesos_ordenados:
        t_llegada = proceso['t-llegada']
        rafaga = proceso['rafaga']
        
        # Si el proceso llega después del tiempo actual, actualizar tiempo
        if tiempo_actual < t_llegada:
            tiempo_actual = t_llegada
        
        # Tiempo de inicio
        tiempo_inicio = tiempo_actual
        
        # Tiempo de finalización
        tiempo_finalizacion = tiempo_actual + rafaga
        
        # Tiempo de respuesta = Tiempo de finalización - Tiempo de llegada
        tiempo_respuesta = tiempo_finalizacion - t_llegada
        
        # Tiempo de espera = Tiempo de respuesta - Ráfaga
        tiempo_espera = tiempo_respuesta - rafaga
        
        resultados.append({
            't-llegada': t_llegada,
            'rafaga': rafaga,
            'inicio': tiempo_inicio,
            'finalizacion': tiempo_finalizacion,
            'tiempo-respuesta': tiempo_respuesta,
            'tiempo-espera': tiempo_espera
        })
        
        tiempo_actual = tiempo_finalizacion
    
    return resultados

def mostrar_resultados_fcfs(resultados):
    """
    Muestra los resultados del algoritmo FCFS en formato tabla.
    """
    if not resultados:
        return
    
    # Crear tabla
    tabla_datos = []
    for res in resultados:
        tabla_datos.append([
            res['t-llegada'],
            res['rafaga'],
            res['inicio'],
            res['finalizacion'],
            res['tiempo-respuesta'],
            res['tiempo-espera']
        ])
    
    headers = ["T-Llegada", "Ráfaga", "Inicio", "Finalización", "T-Respuesta", "T-Espera"]
    
    if TABULATE_AVAILABLE:
        print(tabulate(tabla_datos, headers=headers, tablefmt="grid"))
    else:
        # Formato simple sin tabulate
        print(" | ".join(headers))
        print("-" * 70)
        for fila in tabla_datos:
            print(" | ".join(f"{val:^12}" for val in fila))
    
    # Calcular promedios
    promedio_tr = sum(r['tiempo-respuesta'] for r in resultados) / len(resultados)
    promedio_te = sum(r['tiempo-espera'] for r in resultados) / len(resultados)
    
    print(f'\nTiempo de respuesta promedio: {promedio_tr:.2f} ut.')
    print(f'Tiempo de espera promedio: {promedio_te:.2f} ut.')

# Probar versión corregida
procesos_test = [
    {'t-llegada': 0, 'rafaga': 10},
    {'t-llegada': 2, 'rafaga': 12},
    {'t-llegada': 4, 'rafaga': 5},
    {'t-llegada': 3, 'rafaga': 6},
    {'t-llegada': 1, 'rafaga': 24}
]

print("Resultados con algoritmo FCFS corregido:")
resultados = planificacion_fcfs_corregida(procesos_test)
if resultados:
    mostrar_resultados_fcfs(resultados)
print()

# Versión 3: Mejorada con validación
print("=== Versión 3: Mejorada con Validación ===")
def validar_procesos(procesos):
    """
    Valida que los procesos tengan la estructura correcta.
    """
    if not procesos:
        return False, "La lista de procesos está vacía"
    
    t_llegadas = []
    for i, proceso in enumerate(procesos):
        if 't-llegada' not in proceso or 'rafaga' not in proceso:
            return False, f"El proceso {i} no tiene las claves 't-llegada' y 'rafaga'"
        
        t_llegada = proceso['t-llegada']
        rafaga = proceso['rafaga']
        
        if t_llegada < 0:
            return False, f"El proceso {i} tiene tiempo de llegada negativo: {t_llegada}"
        
        if rafaga <= 0:
            return False, f"El proceso {i} tiene ráfaga no positiva: {rafaga}"
        
        if t_llegada in t_llegadas:
            return False, f"El tiempo de llegada {t_llegada} no es único (duplicado)"
        
        t_llegadas.append(t_llegada)
    
    return True, "Validación exitosa"

def planificacion_fcfs_validada(procesos):
    """
    Versión con validación completa.
    """
    valido, mensaje = validar_procesos(procesos)
    if not valido:
        print(f"Error de validación: {mensaje}")
        return None
    
    return planificacion_fcfs_corregida(procesos)

# Probar validación
print("Probando validación:")
procesos_invalidos = [
    {'t-llegada': 0, 'rafaga': 10},
    {'t-llegada': 0, 'rafaga': 12}  # Tiempo de llegada duplicado
]
resultados_invalidos = planificacion_fcfs_validada(procesos_invalidos)
print()

# Versión 4: Con diagrama de Gantt
print("=== Versión 4: Con Diagrama de Gantt ===")
def generar_diagrama_gantt(resultados):
    """
    Genera un diagrama de Gantt simple en texto.
    """
    if not resultados:
        return
    
    print("\nDiagrama de Gantt:")
    print("=" * 80)
    
    tiempo_total = max(r['finalizacion'] for r in resultados)
    
    # Línea de tiempo
    print("Tiempo: ", end="")
    for i in range(0, tiempo_total + 1, 5):
        print(f"{i:^5}", end="")
    print()
    print("-" * 80)
    
    # Barras de procesos
    for i, res in enumerate(resultados):
        proceso_id = f"P{i+1}"
        inicio = res['inicio']
        duracion = res['rafaga']
        
        print(f"{proceso_id:>8} |", end="")
        espacios = inicio
        print(" " * espacios, end="")
        print("█" * duracion, end="")
        print(f" ({inicio}-{res['finalizacion']})")
    
    print("=" * 80)

resultados_gantt = planificacion_fcfs_corregida(procesos_test)
if resultados_gantt:
    generar_diagrama_gantt(resultados_gantt)
print()

# Versión 5: Función completa mejorada
print("=== Versión 5: Función Completa Mejorada ===")
def planificacion_fcfs_completa(procesos, mostrar_tabla=True, mostrar_gantt=False):
    """
    Función completa que ejecuta el algoritmo FCFS con todas las opciones.
    """
    # Validar
    valido, mensaje = validar_procesos(procesos)
    if not valido:
        print(f"Error: {mensaje}")
        return None
    
    # Ejecutar algoritmo
    resultados = planificacion_fcfs_corregida(procesos)
    if not resultados:
        return None
    
    # Mostrar tabla
    if mostrar_tabla:
        print("\n--- Resultados del Algoritmo FCFS ---")
        mostrar_resultados_fcfs(resultados)
    
    # Mostrar diagrama de Gantt
    if mostrar_gantt:
        generar_diagrama_gantt(resultados)
    
    return resultados

# Ejecutar versión completa
print("Ejecutando versión completa:")
resultados_completos = planificacion_fcfs_completa(procesos_test, mostrar_gantt=True)
print()

# Versión 6: Comparación con el código original
print("=== Versión 6: Análisis del Código Original ===")
print("Problemas identificados en el código original:")
print("1. El cálculo de tiempo de respuesta no considera correctamente el tiempo de llegada")
print("2. El cálculo de tiempo de espera es incorrecto (usa 'te - contador')")
print("3. Elimina el último elemento y lo reemplaza con 0, lo cual es confuso")
print("4. Ordena los tiempos de espera, perdiendo la relación con los procesos")
print("5. No valida tiempos de llegada únicos como menciona el comentario")
print("6. No considera el caso cuando un proceso llega después del tiempo actual")
print()
print("Correcciones implementadas:")
print("1. Cálculo correcto: TR = Finalización - Llegada")
print("2. Cálculo correcto: TE = TR - Ráfaga")
print("3. Validación de tiempos de llegada únicos")
print("4. Manejo correcto de procesos que llegan después")
print("5. Estructura de datos más clara")
print("6. Diagrama de Gantt para visualización")
print()

# Resumen
print("=== Resumen ===")
print("El algoritmo FCFS (First Come First Served) es un algoritmo de planificación")
print("de procesos donde los procesos se ejecutan en el orden de llegada.")
print("\nFórmulas importantes:")
print("  - Tiempo de respuesta (TR) = Tiempo de finalización - Tiempo de llegada")
print("  - Tiempo de espera (TE) = Tiempo de respuesta - Ráfaga")
print("  - Tiempo de finalización = Tiempo de inicio + Ráfaga")
