# Archivo: 28_estadistica_basica.py
# Descripción: Estadísticas básicas de una lista de datos

import statistics
import numpy as np
from collections import Counter

print("=== Estadísticas Básicas ===\n")

# Versión 1: Original
print("=== Versión 1: Original ===")
def estadisticas_original(lista):
    """
    Versión original del código de estadísticas.
    """
    cantidad = len(lista)
    lista.sort()  # Ordenar la lista
    print(lista)
    print("Total de datos(N): {}".format(cantidad))
    
    # Sumar elementos de la lista
    suma = 0
    for item in lista:
        suma = suma + item
    print("La suma de los datos es: {} ".format(suma))
    
    # Hallar promedio
    promedio = suma/cantidad
    print("El promedio es: {}".format(promedio))

# Prueba con datos del código original
lista_original = [0, 10, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4]
print("Datos originales:")
print(lista_original)
print("\nEstadísticas (versión original):")
estadisticas_original(lista_original.copy())
print()

# Versión 2: Optimizada
print("=== Versión 2: Optimizada ===")
def estadisticas_optimizada(lista, mostrar_lista_ordenada=False):
    """
    Versión optimizada usando funciones built-in de Python.
    """
    if not lista:
        print("⚠️  La lista está vacía")
        return None
    
    cantidad = len(lista)
    lista_ordenada = sorted(lista)  # No modifica la lista original
    
    if mostrar_lista_ordenada:
        print(f"Lista ordenada: {lista_ordenada}")
    
    suma = sum(lista)  # Más eficiente que bucle
    promedio = suma / cantidad
    
    print(f"Total de datos (N): {cantidad}")
    print(f"Suma de los datos: {suma}")
    print(f"Promedio (Media aritmética): {promedio:.4f}")
    
    return {
        'cantidad': cantidad,
        'suma': suma,
        'promedio': promedio,
        'lista_ordenada': lista_ordenada
    }

print("Estadísticas (versión optimizada):")
resultado = estadisticas_optimizada(lista_original.copy(), mostrar_lista_ordenada=True)
print()

# Versión 3: Estadísticas completas
print("=== Versión 3: Estadísticas Completas ===")
def estadisticas_completas(lista):
    """
    Calcula estadísticas descriptivas completas de una lista.
    """
    if not lista:
        print("⚠️  La lista está vacía")
        return None
    
    lista_ordenada = sorted(lista)
    cantidad = len(lista)
    
    # Estadísticas básicas
    suma = sum(lista)
    promedio = suma / cantidad
    
    # Mediana
    if cantidad % 2 == 0:
        mediana = (lista_ordenada[cantidad//2 - 1] + lista_ordenada[cantidad//2]) / 2
    else:
        mediana = lista_ordenada[cantidad//2]
    
    # Moda
    contador = Counter(lista)
    moda_valor = contador.most_common(1)[0][0]
    moda_frecuencia = contador[moda_valor]
    
    # Rango
    rango = max(lista) - min(lista)
    
    # Varianza y desviación estándar (poblacional)
    varianza = sum((x - promedio)**2 for x in lista) / cantidad
    desviacion_estandar = varianza ** 0.5
    
    # Varianza y desviación estándar (muestral)
    if cantidad > 1:
        varianza_muestral = sum((x - promedio)**2 for x in lista) / (cantidad - 1)
        desviacion_estandar_muestral = varianza_muestral ** 0.5
    else:
        varianza_muestral = 0
        desviacion_estandar_muestral = 0
    
    # Cuartiles
    q1_pos = cantidad // 4
    q2_pos = cantidad // 2  # Mediana
    q3_pos = 3 * cantidad // 4
    
    q1 = lista_ordenada[q1_pos] if q1_pos < cantidad else lista_ordenada[-1]
    q2 = mediana
    q3 = lista_ordenada[q3_pos] if q3_pos < cantidad else lista_ordenada[-1]
    
    # Mostrar resultados
    print("=" * 60)
    print("ESTADÍSTICAS DESCRIPTIVAS")
    print("=" * 60)
    print(f"\nDatos: {lista}")
    print(f"Total de datos (N): {cantidad}")
    
    print(f"\n📊 MEDIDAS DE TENDENCIA CENTRAL:")
    print(f"  Media (Promedio): {promedio:.4f}")
    print(f"  Mediana: {mediana:.4f}")
    print(f"  Moda: {moda_valor} (aparece {moda_frecuencia} vez/veces)")
    
    print(f"\n📈 MEDIDAS DE DISPERSIÓN:")
    print(f"  Rango: {rango:.4f}")
    print(f"  Varianza (poblacional): {varianza:.4f}")
    print(f"  Desviación estándar (poblacional): {desviacion_estandar:.4f}")
    if cantidad > 1:
        print(f"  Varianza (muestral): {varianza_muestral:.4f}")
        print(f"  Desviación estándar (muestral): {desviacion_estandar_muestral:.4f}")
    
    print(f"\n📋 CUARTILES:")
    print(f"  Q1 (Primer cuartil): {q1:.4f}")
    print(f"  Q2 (Mediana): {q2:.4f}")
    print(f"  Q3 (Tercer cuartil): {q3:.4f}")
    print(f"  Rango intercuartílico (IQR): {q3 - q1:.4f}")
    
    print(f"\n🔢 VALORES EXTREMOS:")
    print(f"  Mínimo: {min(lista)}")
    print(f"  Máximo: {max(lista)}")
    
    print("=" * 60)
    
    return {
        'cantidad': cantidad,
        'suma': suma,
        'promedio': promedio,
        'mediana': mediana,
        'moda': moda_valor,
        'moda_frecuencia': moda_frecuencia,
        'rango': rango,
        'varianza': varianza,
        'desviacion_estandar': desviacion_estandar,
        'q1': q1,
        'q2': q2,
        'q3': q3
    }

print("Estadísticas completas:")
resultado_completo = estadisticas_completas(lista_original.copy())
print()

# Versión 4: Usando bibliotecas especializadas
print("=== Versión 4: Usando Bibliotecas Especializadas ===")
def estadisticas_con_librerias(lista):
    """
    Calcula estadísticas usando la biblioteca statistics de Python.
    """
    if not lista:
        print("⚠️  La lista está vacía")
        return None
    
    print("Estadísticas usando biblioteca 'statistics':")
    print(f"  Media: {statistics.mean(lista):.4f}")
    print(f"  Mediana: {statistics.median(lista):.4f}")
    try:
        print(f"  Moda: {statistics.mode(lista)}")
    except statistics.StatisticsError:
        print(f"  Moda: Múltiples modas")
        print(f"       {statistics.multimode(lista)}")
    print(f"  Desviación estándar (poblacional): {statistics.pstdev(lista):.4f}")
    if len(lista) > 1:
        print(f"  Desviación estándar (muestral): {statistics.stdev(lista):.4f}")
        print(f"  Varianza (muestral): {statistics.variance(lista):.4f}")
    
    # Usando numpy
    if len(lista) > 0:
        arr = np.array(lista)
        print(f"\nEstadísticas usando NumPy:")
        print(f"  Media: {np.mean(arr):.4f}")
        print(f"  Mediana: {np.median(arr):.4f}")
        print(f"  Desviación estándar: {np.std(arr):.4f}")
        print(f"  Varianza: {np.var(arr):.4f}")
        print(f"  Mínimo: {np.min(arr)}")
        print(f"  Máximo: {np.max(arr)}")
        print(f"  Suma: {np.sum(arr)}")

estadisticas_con_librerias(lista_original.copy())
print()

# Versión 5: Tabla de frecuencias
print("=== Versión 5: Tabla de Frecuencias ===")
def tabla_frecuencias(lista):
    """
    Crea una tabla de frecuencias de los datos.
    """
    contador = Counter(lista)
    lista_ordenada_datos = sorted(contador.keys())
    
    print("=" * 50)
    print("TABLA DE FRECUENCIAS")
    print("=" * 50)
    print(f"{'Valor':<10} {'Frecuencia':<12} {'Frec. Relativa':<15} {'Frec. Acumulada':<15}")
    print("-" * 50)
    
    total = len(lista)
    acumulada = 0
    
    for valor in lista_ordenada_datos:
        frecuencia = contador[valor]
        acumulada += frecuencia
        frecuencia_relativa = frecuencia / total
        frecuencia_acumulada = acumulada / total
        
        print(f"{valor:<10} {frecuencia:<12} {frecuencia_relativa:<15.4f} {frecuencia_acumulada:<15.4f}")
    
    print("-" * 50)
    print(f"{'Total':<10} {total:<12} {1.0:<15.4f} {1.0:<15.4f}")
    print("=" * 50)
    
    return contador

print("Tabla de frecuencias:")
tabla_frecuencias(lista_original.copy())
print()

# Versión 6: Función interactiva
print("=== Versión 6: Función Interactiva ===")
def estadisticas_interactiva():
    """
    Función interactiva para calcular estadísticas.
    """
    print("\n" + "=" * 60)
    print("CALCULADORA DE ESTADÍSTICAS")
    print("=" * 60)
    
    while True:
        try:
            print("\nOpciones:")
            print("1. Ingresar lista manualmente")
            print("2. Usar lista de ejemplo")
            print("3. Salir")
            
            opcion = input("\nSeleccione una opción: ").strip()
            
            if opcion == "1":
                datos_str = input("Ingrese los datos separados por comas: ")
                lista = [float(x.strip()) for x in datos_str.split(',')]
            elif opcion == "2":
                lista = lista_original.copy()
                print(f"Usando lista de ejemplo: {lista}")
            elif opcion == "3":
                print("👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción no válida")
                continue
            
            print("\n¿Qué tipo de análisis desea?")
            print("1. Estadísticas básicas (original)")
            print("2. Estadísticas completas")
            print("3. Tabla de frecuencias")
            print("4. Todo lo anterior")
            
            analisis = input("Seleccione: ").strip()
            
            if analisis == "1":
                estadisticas_optimizada(lista, mostrar_lista_ordenada=True)
            elif analisis == "2":
                estadisticas_completas(lista)
            elif analisis == "3":
                tabla_frecuencias(lista)
            elif analisis == "4":
                estadisticas_optimizada(lista, mostrar_lista_ordenada=True)
                print()
                estadisticas_completas(lista)
                print()
                tabla_frecuencias(lista)
            else:
                print("❌ Opción no válida")
        
        except ValueError:
            print("❌ Error: Por favor ingrese números válidos")
        except KeyboardInterrupt:
            print("\n\n👋 Operación cancelada")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

# Descomentar para probar:
# estadisticas_interactiva()

# Versión 7: Comparación de métodos
print("=== Versión 7: Comparación de Métodos ===")
import time

def comparar_metodos(lista):
    """
    Compara el tiempo de ejecución de diferentes métodos.
    """
    print(f"\nComparando métodos para lista de {len(lista)} elementos:")
    
    # Método 1: Bucle manual
    inicio = time.time()
    suma = 0
    for item in lista:
        suma += item
    promedio = suma / len(lista)
    tiempo_bucle = time.time() - inicio
    
    # Método 2: sum()
    inicio = time.time()
    suma = sum(lista)
    promedio = suma / len(lista)
    tiempo_sum = time.time() - inicio
    
    # Método 3: numpy
    inicio = time.time()
    arr = np.array(lista)
    promedio = np.mean(arr)
    tiempo_numpy = time.time() - inicio
    
    print(f"  Bucle manual: {tiempo_bucle*1000000:.2f} microsegundos")
    print(f"  sum(): {tiempo_sum*1000000:.2f} microsegundos")
    print(f"  NumPy: {tiempo_numpy*1000000:.2f} microsegundos")
    print(f"\n  Resultados idénticos: {abs(suma - np.sum(arr)) < 1e-10}")

comparar_metodos(lista_original)
print()

# Resumen
print("=== Resumen de Análisis ===")
print("Código original:")
print("  ✓ Funciona correctamente")
print("  ✓ Calcula suma y promedio")
print("  ⚠️  Usa bucle manual para suma (puede usar sum())")
print("  ⚠️  Modifica la lista original con .sort()")
print("  ⚠️  Solo calcula estadísticas básicas")
print("  ⚠️  No calcula otras medidas (mediana, moda, desviación estándar, etc.)")
print()
print("Mejoras implementadas:")
print("  1. ✅ Uso de sum() en lugar de bucle")
print("  2. ✅ sorted() en lugar de .sort() (no modifica original)")
print("  3. ✅ Estadísticas completas (mediana, moda, varianza, etc.)")
print("  4. ✅ Tabla de frecuencias")
print("  5. ✅ Uso de bibliotecas especializadas (statistics, numpy)")
print("  6. ✅ Cuartiles y rango intercuartílico")
print("  7. ✅ Función interactiva")
print("  8. ✅ Comparación de métodos")
print("  9. ✅ Documentación completa")
