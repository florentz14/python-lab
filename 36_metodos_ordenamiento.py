# Archivo: 36_metodos_ordenamiento.py
# Descripción: Métodos de ordenamiento - Algoritmos de clasificación

import time
import random
import matplotlib.pyplot as plt
import numpy as np

print("=== Métodos de Ordenamiento ===\n")

# Función auxiliar para verificar si una lista está ordenada
def esta_ordenada(lista):
    """Verifica si una lista está ordenada de forma ascendente."""
    return all(lista[i] <= lista[i+1] for i in range(len(lista)-1))

# Función auxiliar para generar listas de prueba
def generar_lista_aleatoria(n, minimo=1, maximo=100):
    """Genera una lista aleatoria de n elementos."""
    return [random.randint(minimo, maximo) for _ in range(n)]

# =============================================================================
# 1. BUBBLE SORT (Ordenamiento de burbuja)
# =============================================================================
print("=== 1. BUBBLE SORT (Ordenamiento de Burbuja) ===")
def bubble_sort(lista):
    """
    Ordenamiento de burbuja.
    Complejidad: O(n²) en el peor caso
    Estable: Sí
    In-place: Sí
    """
    lista = lista.copy()  # No modificar la original
    n = len(lista)
    
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista

# Versión optimizada (se detiene si no hay intercambios)
def bubble_sort_optimizado(lista):
    """
    Bubble sort optimizado: se detiene si no hay intercambios.
    """
    lista = lista.copy()
    n = len(lista)
    
    for i in range(n):
        intercambiado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True
        
        # Si no hubo intercambios, la lista ya está ordenada
        if not intercambiado:
            break
    
    return lista

# Ejemplo
print("Ejemplo Bubble Sort:")
lista_ejemplo = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {lista_ejemplo}")
print(f"Bubble Sort: {bubble_sort(lista_ejemplo)}")
print(f"Bubble Sort Optimizado: {bubble_sort_optimizado(lista_ejemplo)}")
print()

# =============================================================================
# 2. SELECTION SORT (Ordenamiento por selección)
# =============================================================================
print("=== 2. SELECTION SORT (Ordenamiento por Selección) ===")
def selection_sort(lista):
    """
    Ordenamiento por selección.
    Complejidad: O(n²)
    Estable: No
    In-place: Sí
    """
    lista = lista.copy()
    n = len(lista)
    
    for i in range(n):
        # Encontrar el elemento mínimo en el resto de la lista
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        
        # Intercambiar el elemento mínimo con el primero
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    
    return lista

# Ejemplo
print("Ejemplo Selection Sort:")
lista_ejemplo = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {lista_ejemplo}")
print(f"Selection Sort: {selection_sort(lista_ejemplo)}")
print()

# =============================================================================
# 3. INSERTION SORT (Ordenamiento por inserción)
# =============================================================================
print("=== 3. INSERTION SORT (Ordenamiento por Inserción) ===")
def insertion_sort(lista):
    """
    Ordenamiento por inserción.
    Complejidad: O(n²) en el peor caso, O(n) en el mejor caso
    Estable: Sí
    In-place: Sí
    Eficiente para listas pequeñas o casi ordenadas
    """
    lista = lista.copy()
    
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        
        # Mover elementos mayores que la clave una posición adelante
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = clave
    
    return lista

# Ejemplo
print("Ejemplo Insertion Sort:")
lista_ejemplo = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {lista_ejemplo}")
print(f"Insertion Sort: {insertion_sort(lista_ejemplo)}")
print()

# =============================================================================
# 4. MERGE SORT (Ordenamiento por mezcla)
# =============================================================================
print("=== 4. MERGE SORT (Ordenamiento por Mezcla) ===")
def merge_sort(lista):
    """
    Ordenamiento por mezcla (divide y vencerás).
    Complejidad: O(n log n) siempre
    Estable: Sí
    In-place: No (requiere espacio adicional O(n))
    """
    if len(lista) <= 1:
        return lista.copy()
    
    # Dividir
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    
    # Combinar
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    """Combina dos listas ordenadas en una lista ordenada."""
    resultado = []
    i = j = 0
    
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    # Agregar elementos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    
    return resultado

# Ejemplo
print("Ejemplo Merge Sort:")
lista_ejemplo = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {lista_ejemplo}")
print(f"Merge Sort: {merge_sort(lista_ejemplo)}")
print()

# =============================================================================
# 5. QUICK SORT (Ordenamiento rápido)
# =============================================================================
print("=== 5. QUICK SORT (Ordenamiento Rápido) ===")
def quick_sort(lista):
    """
    Ordenamiento rápido (divide y vencerás).
    Complejidad: O(n log n) promedio, O(n²) en el peor caso
    Estable: No
    In-place: Sí (con algunas modificaciones)
    Muy eficiente en la práctica
    """
    if len(lista) <= 1:
        return lista.copy()
    
    # Elegir pivote (puede ser el primero, medio, o aleatorio)
    pivote = lista[len(lista) // 2]
    
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    
    return quick_sort(menores) + iguales + quick_sort(mayores)

# Versión in-place (más eficiente en memoria)
def quick_sort_inplace(lista, inicio=0, fin=None):
    """Quick sort in-place."""
    if fin is None:
        fin = len(lista) - 1
    
    if inicio < fin:
        # Particionar y obtener índice del pivote
        pivote_idx = particionar(lista, inicio, fin)
        
        # Ordenar recursivamente las dos partes
        quick_sort_inplace(lista, inicio, pivote_idx - 1)
        quick_sort_inplace(lista, pivote_idx + 1, fin)
    
    return lista

def particionar(lista, inicio, fin):
    """Particiona la lista alrededor de un pivote."""
    pivote = lista[fin]
    i = inicio - 1
    
    for j in range(inicio, fin):
        if lista[j] <= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
    return i + 1

# Ejemplo
print("Ejemplo Quick Sort:")
lista_ejemplo = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {lista_ejemplo}")
print(f"Quick Sort: {quick_sort(lista_ejemplo)}")
lista_copy = lista_ejemplo.copy()
quick_sort_inplace(lista_copy)
print(f"Quick Sort In-place: {lista_copy}")
print()

# =============================================================================
# 6. HEAP SORT (Ordenamiento por montículos)
# =============================================================================
print("=== 6. HEAP SORT (Ordenamiento por Montículos) ===")
def heap_sort(lista):
    """
    Ordenamiento por montículos.
    Complejidad: O(n log n) siempre
    Estable: No
    In-place: Sí
    """
    lista = lista.copy()
    n = len(lista)
    
    # Construir heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
    
    # Extraer elementos uno por uno
    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heapify(lista, i, 0)
    
    return lista

def heapify(lista, n, i):
    """Convierte un árbol en un heap máximo."""
    mayor = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2
    
    if izquierda < n and lista[izquierda] > lista[mayor]:
        mayor = izquierda
    
    if derecha < n and lista[derecha] > lista[mayor]:
        mayor = derecha
    
    if mayor != i:
        lista[i], lista[mayor] = lista[mayor], lista[i]
        heapify(lista, n, mayor)

# Ejemplo
print("Ejemplo Heap Sort:")
lista_ejemplo = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {lista_ejemplo}")
print(f"Heap Sort: {heap_sort(lista_ejemplo)}")
print()

# =============================================================================
# 7. COUNTING SORT (Ordenamiento por conteo)
# =============================================================================
print("=== 7. COUNTING SORT (Ordenamiento por Conteo) ===")
def counting_sort(lista, maximo=None):
    """
    Ordenamiento por conteo.
    Complejidad: O(n + k) donde k es el rango
    Estable: Sí
    In-place: No
    Eficiente cuando el rango de valores es pequeño
    """
    if maximo is None:
        maximo = max(lista) if lista else 0
    
    # Crear array de conteo
    count = [0] * (maximo + 1)
    
    # Contar ocurrencias
    for num in lista:
        count[num] += 1
    
    # Construir lista ordenada
    resultado = []
    for i in range(maximo + 1):
        resultado.extend([i] * count[i])
    
    return resultado

# Ejemplo
print("Ejemplo Counting Sort:")
lista_ejemplo = [4, 2, 2, 8, 3, 3, 1]
print(f"Lista original: {lista_ejemplo}")
print(f"Counting Sort: {counting_sort(lista_ejemplo)}")
print()

# =============================================================================
# 8. Comparación de Métodos
# =============================================================================
print("=== 8. Comparación de Métodos ===")
def comparar_metodos_ordenamiento(lista, mostrar_resultados=True):
    """
    Compara diferentes métodos de ordenamiento.
    """
    metodos = {
        'Bubble Sort': bubble_sort,
        'Bubble Sort Optimizado': bubble_sort_optimizado,
        'Selection Sort': selection_sort,
        'Insertion Sort': insertion_sort,
        'Merge Sort': merge_sort,
        'Quick Sort': quick_sort,
        'Heap Sort': heap_sort,
        'Python sorted()': sorted  # Método nativo (Timsort)
    }
    
    resultados = {}
    tiempos = {}
    
    print(f"\nComparando métodos para lista de {len(lista)} elementos:")
    print("=" * 70)
    
    for nombre, metodo in metodos.items():
        lista_copia = lista.copy()
        
        inicio = time.time()
        try:
            resultado = metodo(lista_copia)
            tiempo = time.time() - inicio
            
            # Verificar que esté ordenada
            ordenada = esta_ordenada(resultado)
            
            resultados[nombre] = resultado
            tiempos[nombre] = tiempo
            
            estado = "✓" if ordenada else "✗"
            if mostrar_resultados and len(lista) <= 20:
                print(f"{estado} {nombre:25s} {tiempo*1000:8.4f} ms")
            else:
                print(f"{estado} {nombre:25s} {tiempo*1000:8.4f} ms")
        except Exception as e:
            print(f"✗ {nombre:25s} Error: {e}")
            tiempos[nombre] = float('inf')
    
    print("=" * 70)
    
    # Encontrar el más rápido
    tiempos_validos = {k: v for k, v in tiempos.items() if v != float('inf')}
    if tiempos_validos:
        mas_rapido = min(tiempos_validos, key=tiempos_validos.get)
        print(f"\nMétodo más rápido: {mas_rapido} ({tiempos_validos[mas_rapido]*1000:.4f} ms)")
    
    return tiempos, resultados

# Comparar con lista pequeña
print("Comparación con lista pequeña (10 elementos):")
lista_pequena = generar_lista_aleatoria(10, 1, 50)
print(f"Lista: {lista_pequena}")
comparar_metodos_ordenamiento(lista_pequena, mostrar_resultados=True)
print()

# Comparar con lista mediana
print("Comparación con lista mediana (100 elementos):")
lista_mediana = generar_lista_aleatoria(100, 1, 100)
comparar_metodos_ordenamiento(lista_mediana, mostrar_resultados=False)
print()

# =============================================================================
# 9. Análisis de Complejidad
# =============================================================================
print("=== 9. Análisis de Complejidad ===")
def analizar_complejidad():
    """
    Muestra la complejidad temporal de cada método.
    """
    print("\nComplejidad Temporal de los Métodos:")
    print("=" * 70)
    print(f"{'Método':<25} {'Mejor Caso':<15} {'Caso Promedio':<15} {'Peor Caso':<15}")
    print("-" * 70)
    
    complejidades = [
        ("Bubble Sort", "O(n)", "O(n²)", "O(n²)"),
        ("Bubble Sort Optimizado", "O(n)", "O(n²)", "O(n²)"),
        ("Selection Sort", "O(n²)", "O(n²)", "O(n²)"),
        ("Insertion Sort", "O(n)", "O(n²)", "O(n²)"),
        ("Merge Sort", "O(n log n)", "O(n log n)", "O(n log n)"),
        ("Quick Sort", "O(n log n)", "O(n log n)", "O(n²)"),
        ("Heap Sort", "O(n log n)", "O(n log n)", "O(n log n)"),
        ("Counting Sort", "O(n + k)", "O(n + k)", "O(n + k)"),
        ("Python sorted() (Timsort)", "O(n)", "O(n log n)", "O(n log n)"),
    ]
    
    for metodo, mejor, promedio, peor in complejidades:
        print(f"{metodo:<25} {mejor:<15} {promedio:<15} {peor:<15}")
    
    print("=" * 70)
    print("\nNotas:")
    print("  - k: rango de valores (en Counting Sort)")
    print("  - Estable: mantiene el orden relativo de elementos iguales")
    print("  - In-place: usa espacio O(1) adicional")

analizar_complejidad()
print()

# =============================================================================
# 10. Casos Especiales
# =============================================================================
print("=== 10. Casos Especiales ===")
def probar_casos_especiales():
    """
    Prueba los algoritmos con casos especiales.
    """
    casos = {
        'Lista ya ordenada': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Lista inversamente ordenada': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        'Lista con elementos iguales': [5, 5, 5, 5, 5, 5],
        'Lista con un elemento': [42],
        'Lista vacía': [],
    }
    
    print("\nProbando casos especiales:")
    print("=" * 70)
    
    for nombre, lista in casos.items():
        print(f"\n{nombre}: {lista}")
        if lista:
            resultado = merge_sort(lista)
            print(f"  Ordenada: {resultado}")
            print(f"  Verificación: {'✓ Correcto' if esta_ordenada(resultado) else '✗ Error'}")
        else:
            print(f"  Lista vacía - no se puede ordenar")

probar_casos_especiales()
print()

# =============================================================================
# 11. Visualización del Proceso (opcional)
# =============================================================================
print("=== 11. Resumen y Recomendaciones ===")
print("\nRecomendaciones de uso:")
print("=" * 70)
print("1. Para listas pequeñas (< 50 elementos):")
print("   - Insertion Sort o incluso Bubble Sort son adecuados")
print()
print("2. Para listas medianas (50-1000 elementos):")
print("   - Quick Sort o Merge Sort (mejor rendimiento general)")
print()
print("3. Para listas grandes (> 1000 elementos):")
print("   - Quick Sort, Merge Sort, o Heap Sort")
print("   - Python's sorted() (Timsort) es excelente")
print()
print("4. Para datos con rango pequeño conocido:")
print("   - Counting Sort puede ser muy eficiente")
print()
print("5. Cuando se necesita estabilidad:")
print("   - Merge Sort, Insertion Sort, Bubble Sort, Counting Sort")
print("   - Evitar Quick Sort y Heap Sort")
print()
print("6. Cuando el espacio es limitado:")
print("   - Usar algoritmos in-place: Quick Sort, Heap Sort, Insertion Sort")
print("   - Evitar Merge Sort (requiere espacio O(n))")
print("=" * 70)

# Resumen final
print("\n=== Resumen ===")
print("Métodos de ordenamiento implementados:")
print("  1. Bubble Sort - Simple pero lento O(n²)")
print("  2. Selection Sort - Simple, siempre O(n²)")
print("  3. Insertion Sort - Eficiente para listas pequeñas")
print("  4. Merge Sort - Estable, O(n log n) garantizado")
print("  5. Quick Sort - Rápido en la práctica")
print("  6. Heap Sort - O(n log n) garantizado, in-place")
print("  7. Counting Sort - O(n + k) para rangos pequeños")
print("  8. Python sorted() - Timsort, híbrido optimizado")
