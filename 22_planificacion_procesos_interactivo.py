# Archivo: 22_planificacion_procesos_interactivo.py
# Descripción: Algoritmo FCFS interactivo de planificación de procesos

from operator import itemgetter

try:
    from tabulate import tabulate  # type: ignore[reportMissingModuleSource]
    TABULATE_AVAILABLE = True
except ImportError:
    TABULATE_AVAILABLE = False

print("=== Planificación de Procesos FCFS (Interactivo) ===\n")

# Versión 1: Original (con comentarios sobre problemas)
print("=== Versión 1: Original ===")
def planificacion_original_interactiva():
    """
    Versión original del código interactivo.
    Nota: Esta versión tiene problemas de lógica en los cálculos.
    """
    try:
        print('💻💻💻💻💻💻 OBTENEMOS DATOS DE ENTRADA 💻💻💻💻💻💻')
        print()
        cantidad_procesos = int(input('Ingrese el número de procesos: '))
        if cantidad_procesos > 0:
            procesos = {}
            for pr in range(cantidad_procesos):
                print(f'Proceso #{pr + 1}')
                t_llegada = int(input(f'Ingrese el tiempo de llegada ⏱️  del proceso #{pr + 1}: '))
                rafaga = int(input(f'Ingrese el valor de rafaga 🔥 en CPU del proceso #{pr + 1}: '))
                procesos[t_llegada] = rafaga
                print()
                print()
            
            print('✅✅✅✅✅ ORDENAMOS LOS PROCESOS SEGÚN SU TIEMPO DE LLEGADA ✅✅✅✅✅')
            procesos_ordenados = dict(sorted(procesos.items(), key=itemgetter(0)))
            
            tiempoRespuesta = 0
            totalTR = []
            for t_llegada, rafaga in procesos_ordenados.items():
                tiempoRespuesta += rafaga
                print(f"""
            Proceso con tiempo de llegada: #{t_llegada}
            Tiempo de respuesta: {tiempoRespuesta}
            ------------ Fin del proceso ------------
            """)
                totalTR.append(tiempoRespuesta)

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
    except Exception as e:
        print(e)

# Descomentar para probar:
# planificacion_original_interactiva()

# Versión 2: Corregida (Lógica FCFS correcta)
print("=== Versión 2: Corregida (Lógica FCFS Correcta) ===")
def planificacion_fcfs_interactiva_corregida():
    """
    Versión corregida con lógica FCFS correcta.
    
    Corrige:
    - Cálculo correcto de tiempo de respuesta
    - Cálculo correcto de tiempo de espera
    - Validación de tiempos de llegada únicos
    - Manejo de procesos que llegan después
    """
    try:
        print('💻💻💻💻💻💻 OBTENEMOS DATOS DE ENTRADA 💻💻💻💻💻💻\n')
        cantidad_procesos = int(input('Ingrese el número de procesos: '))
        
        if cantidad_procesos <= 0:
            print('❌ El número de procesos debe ser mayor a 0 (cero)')
            return
        
        procesos = {}
        for pr in range(cantidad_procesos):
            print(f'\n📋 Proceso #{pr + 1}')
            while True:
                try:
                    t_llegada = int(input(f'  ⏱️  Tiempo de llegada del proceso #{pr + 1}: '))
                    
                    # Validar que el tiempo de llegada sea único
                    if t_llegada in procesos:
                        print(f'  ⚠️  El tiempo de llegada {t_llegada} ya existe. Debe ser único.')
                        continue
                    
                    if t_llegada < 0:
                        print(f'  ⚠️  El tiempo de llegada debe ser >= 0')
                        continue
                    
                    break
                except ValueError:
                    print('  ⚠️  Por favor ingrese un número entero válido')
            
            while True:
                try:
                    rafaga = int(input(f'  🔥 Ráfaga en CPU del proceso #{pr + 1}: '))
                    if rafaga <= 0:
                        print(f'  ⚠️  La ráfaga debe ser mayor a 0')
                        continue
                    break
                except ValueError:
                    print('  ⚠️  Por favor ingrese un número entero válido')
            
            procesos[t_llegada] = rafaga
        
        print('\n✅✅✅✅✅ ORDENAMOS LOS PROCESOS SEGÚN SU TIEMPO DE LLEGADA ✅✅✅✅✅\n')
        procesos_ordenados = dict(sorted(procesos.items(), key=itemgetter(0)))
        
        # Algoritmo FCFS corregido
        tiempo_actual = 0
        resultados = []
        
        for t_llegada, rafaga in procesos_ordenados.items():
            # Si el proceso llega después del tiempo actual, actualizar tiempo
            if tiempo_actual < t_llegada:
                tiempo_actual = t_llegada
            
            tiempo_inicio = tiempo_actual
            tiempo_finalizacion = tiempo_actual + rafaga
            tiempo_respuesta = tiempo_finalizacion - t_llegada
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
        
        # Mostrar resultados
        print('📊 RESULTADOS DEL ALGORITMO FCFS 📊\n')
        
        if TABULATE_AVAILABLE:
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
            print(tabulate(tabla_datos, headers=headers, tablefmt="grid"))
        else:
            print("T-Llegada | Ráfaga | Inicio | Finalización | T-Respuesta | T-Espera")
            print("-" * 70)
            for res in resultados:
                print(f"{res['t-llegada']:^9} | {res['rafaga']:^6} | {res['inicio']:^6} | "
                      f"{res['finalizacion']:^12} | {res['tiempo-respuesta']:^11} | {res['tiempo-espera']:^9}")
        
        # Calcular promedios
        promedio_tr = sum(r['tiempo-respuesta'] for r in resultados) / len(resultados)
        promedio_te = sum(r['tiempo-espera'] for r in resultados) / len(resultados)
        
        print(f'\n📈 ESTADÍSTICAS:')
        print(f'  ⏱️  Tiempo de respuesta promedio: {promedio_tr:.2f} ut.')
        print(f'  ⏳ Tiempo de espera promedio: {promedio_te:.2f} ut.')
        
        return resultados
        
    except ValueError as e:
        print(f'❌ Error: Por favor ingrese números enteros válidos. {e}')
    except KeyboardInterrupt:
        print('\n\n⚠️  Operación cancelada por el usuario')
    except Exception as e:
        print(f'❌ Error: {e}')

# Descomentar para probar:
# planificacion_fcfs_interactiva_corregida()

# Versión 3: Con datos de prueba (no interactiva)
print("=== Versión 3: Con Datos de Prueba (No Interactiva) ===")
def planificacion_fcfs_con_datos(procesos_dict):
    """
    Versión que acepta un diccionario de procesos y retorna resultados.
    Útil para pruebas y automatización.
    """
    if not procesos_dict:
        print('❌ Error: El diccionario de procesos está vacío')
        return None
    
    # Ordenar procesos
    procesos_ordenados = dict(sorted(procesos_dict.items(), key=itemgetter(0)))
    
    # Algoritmo FCFS
    tiempo_actual = 0
    resultados = []
    
    for t_llegada, rafaga in procesos_ordenados.items():
        if tiempo_actual < t_llegada:
            tiempo_actual = t_llegada
        
        tiempo_inicio = tiempo_actual
        tiempo_finalizacion = tiempo_actual + rafaga
        tiempo_respuesta = tiempo_finalizacion - t_llegada
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

# Prueba con datos de ejemplo
print("Prueba con datos de ejemplo:")
procesos_ejemplo = {
    0: 10,
    2: 12,
    4: 5,
    3: 6,
    1: 24
}

resultados_ejemplo = planificacion_fcfs_con_datos(procesos_ejemplo)
if resultados_ejemplo:
    print("\nResultados:")
    for res in resultados_ejemplo:
        print(f"  T-Llegada: {res['t-llegada']}, Ráfaga: {res['rafaga']}, "
              f"TR: {res['tiempo-respuesta']}, TE: {res['tiempo-espera']}")
    
    promedio_tr = sum(r['tiempo-respuesta'] for r in resultados_ejemplo) / len(resultados_ejemplo)
    promedio_te = sum(r['tiempo-espera'] for r in resultados_ejemplo) / len(resultados_ejemplo)
    print(f"\n  Promedio TR: {promedio_tr:.2f}, Promedio TE: {promedio_te:.2f}")
print()

# Versión 4: Con validación completa
print("=== Versión 4: Con Validación Completa ===")
def validar_proceso(t_llegada, rafaga, procesos_existentes):
    """
    Valida un proceso antes de agregarlo.
    """
    errores = []
    
    if t_llegada in procesos_existentes:
        errores.append(f"El tiempo de llegada {t_llegada} ya existe (debe ser único)")
    
    if t_llegada < 0:
        errores.append(f"El tiempo de llegada debe ser >= 0 (recibido: {t_llegada})")
    
    if rafaga <= 0:
        errores.append(f"La ráfaga debe ser > 0 (recibido: {rafaga})")
    
    return len(errores) == 0, errores

def planificacion_fcfs_con_validacion():
    """
    Versión con validación completa de entrada.
    """
    try:
        print('💻💻💻💻💻💻 OBTENEMOS DATOS DE ENTRADA 💻💻💻💻💻💻\n')
        
        while True:
            try:
                cantidad_procesos = int(input('Ingrese el número de procesos: '))
                if cantidad_procesos > 0:
                    break
                print('❌ El número de procesos debe ser mayor a 0')
            except ValueError:
                print('❌ Por favor ingrese un número entero válido')
        
        procesos = {}
        for pr in range(cantidad_procesos):
            print(f'\n📋 Proceso #{pr + 1}')
            
            # Validar tiempo de llegada
            while True:
                try:
                    t_llegada = int(input(f'  ⏱️  Tiempo de llegada: '))
                    valido, errores = validar_proceso(t_llegada, 1, procesos)  # rafaga temporal para validar
                    if valido:
                        break
                    for error in errores:
                        if "ráfaga" not in error:
                            print(f'  ⚠️  {error}')
                except ValueError:
                    print('  ⚠️  Por favor ingrese un número entero válido')
            
            # Validar ráfaga
            while True:
                try:
                    rafaga = int(input(f'  🔥 Ráfaga en CPU: '))
                    if rafaga > 0:
                        break
                    print('  ⚠️  La ráfaga debe ser mayor a 0')
                except ValueError:
                    print('  ⚠️  Por favor ingrese un número entero válido')
            
            procesos[t_llegada] = rafaga
        
        # Ejecutar algoritmo
        resultados = planificacion_fcfs_con_datos(procesos)
        if resultados:
            # Mostrar resultados (similar a versión 2)
            print('\n✅✅✅✅✅ PROCESOS ORDENADOS ✅✅✅✅✅\n')
            for res in resultados:
                print(f"  Proceso T-Llegada: {res['t-llegada']}, "
                      f"Ráfaga: {res['rafaga']}, "
                      f"T-Respuesta: {res['tiempo-respuesta']}, "
                      f"T-Espera: {res['tiempo-espera']}")
            
            promedio_tr = sum(r['tiempo-respuesta'] for r in resultados) / len(resultados)
            promedio_te = sum(r['tiempo-espera'] for r in resultados) / len(resultados)
            print(f'\n📈 Promedios: TR={promedio_tr:.2f}, TE={promedio_te:.2f}')
        
    except KeyboardInterrupt:
        print('\n\n⚠️  Operación cancelada')
    except Exception as e:
        print(f'❌ Error: {e}')

# Descomentar para probar:
# planificacion_fcfs_con_validacion()

# Resumen de problemas y mejoras
print("=== Resumen de Problemas y Mejoras ===\n")
print("Problemas en el código original:")
print("1. ❌ Cálculo incorrecto de tiempo de respuesta (no considera tiempo de llegada)")
print("2. ❌ Cálculo incorrecto de tiempo de espera (usa 'te - contador')")
print("3. ❌ Elimina último elemento y lo reemplaza con 0")
print("4. ❌ Ordena tiempos de espera, perdiendo relación con procesos")
print("5. ❌ No valida que tiempos de llegada sean únicos (como menciona el comentario)")
print("6. ❌ No maneja procesos que llegan después del tiempo actual")
print("7. ⚠️  No valida ráfagas positivas")
print()
print("Mejoras implementadas:")
print("1. ✅ Cálculo correcto: TR = Finalización - Llegada")
print("2. ✅ Cálculo correcto: TE = TR - Ráfaga")
print("3. ✅ Validación de tiempos de llegada únicos")
print("4. ✅ Validación de valores positivos")
print("5. ✅ Manejo correcto de procesos que llegan después")
print("6. ✅ Estructura de datos clara y mantenible")
print("7. ✅ Manejo de errores mejorado")
print("8. ✅ Opción no interactiva para pruebas")
print()

# Función principal mejorada
def main():
    """
    Función principal mejorada que usa la versión corregida.
    """
    planificacion_fcfs_interactiva_corregida()

if __name__ == '__main__':
    # Descomentar para ejecutar:
    # main()
    print("Nota: Descomenta las funciones para probar interactivamente")
    print("Ejemplo: planificacion_fcfs_interactiva_corregida()")
