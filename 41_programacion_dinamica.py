# Archivo: 41_programacion_dinamica.py
# Descripción: Programación Dinámica - Problemas clásicos

from functools import lru_cache
import time

print("=== Programación Dinámica ===\n")

# =============================================================================
# 1. PROBLEMA DE LA MOCHILA (Knapsack Problem)
# =============================================================================
print("=== 1. Problema de la Mochila (0/1 Knapsack) ===")

def mochila_recursivo(pesos, valores, capacidad, n):
    """
    Solución recursiva naive (sin memoización).
    Complejidad: O(2^n) - exponencial
    """
    if n == 0 or capacidad == 0:
        return 0
    
    # Si el peso del item n-1 es mayor que la capacidad, no lo incluimos
    if pesos[n-1] > capacidad:
        return mochila_recursivo(pesos, valores, capacidad, n-1)
    
    # Retornamos el máximo entre:
    # 1. Incluir el item
    # 2. No incluir el item
    return max(
        valores[n-1] + mochila_recursivo(pesos, valores, capacidad - pesos[n-1], n-1),
        mochila_recursivo(pesos, valores, capacidad, n-1)
    )

def mochila_memoizacion(pesos, valores, capacidad):
    """
    Solución con memoización (top-down).
    Complejidad: O(n * capacidad)
    """
    n = len(pesos)
    memo = {}
    
    def dp(cap, i):
        if (cap, i) in memo:
            return memo[(cap, i)]
        
        if i == n or cap == 0:
            return 0
        
        if pesos[i] > cap:
            resultado = dp(cap, i + 1)
        else:
            resultado = max(
                valores[i] + dp(cap - pesos[i], i + 1),
                dp(cap, i + 1)
            )
        
        memo[(cap, i)] = resultado
        return resultado
    
    return dp(capacidad, 0)

def mochila_programacion_dinamica(pesos, valores, capacidad):
    """
    Solución con programación dinámica (bottom-up).
    Complejidad: O(n * capacidad)
    Complejidad espacial: O(capacidad) - optimizada
    """
    n = len(pesos)
    # Solo necesitamos la fila anterior
    dp = [0] * (capacidad + 1)
    
    for i in range(n):
        # Iterar hacia atrás para evitar sobrescribir valores que necesitamos
        for w in range(capacidad, pesos[i] - 1, -1):
            dp[w] = max(dp[w], valores[i] + dp[w - pesos[i]])
    
    return dp[capacidad]

# Ejemplo
pesos = [1, 3, 4, 5]
valores = [1, 4, 5, 7]
capacidad = 7

print(f"Pesos: {pesos}")
print(f"Valores: {valores}")
print(f"Capacidad: {capacidad}")

# Solución con DP (más eficiente)
valor_maximo = mochila_programacion_dinamica(pesos, valores, capacidad)
print(f"\nValor máximo (DP): {valor_maximo}")

# Comparación de tiempos
print("\nComparación de métodos:")
n_pequeño = len(pesos)
pesos_peq = pesos
valores_peq = valores

inicio = time.time()
resultado_rec = mochila_recursivo(pesos_peq, valores_peq, capacidad, n_pequeño)
tiempo_rec = time.time() - inicio

inicio = time.time()
resultado_memo = mochila_memoizacion(pesos_peq, valores_peq, capacidad)
tiempo_memo = time.time() - inicio

inicio = time.time()
resultado_dp = mochila_programacion_dinamica(pesos_peq, valores_peq, capacidad)
tiempo_dp = time.time() - inicio

print(f"  Recursivo: {tiempo_rec*1000:.4f} ms (valor: {resultado_rec})")
print(f"  Memoización: {tiempo_memo*1000:.4f} ms (valor: {resultado_memo})")
print(f"  Programación Dinámica: {tiempo_dp*1000:.4f} ms (valor: {resultado_dp})")
print()

# =============================================================================
# 2. SUBsecuencia Común Más Larga (LCS - Longest Common Subsequence)
# =============================================================================
print("=== 2. Subsecuencia Común Más Larga (LCS) ===")

def lcs_recursivo(X, Y, m, n):
    """Solución recursiva naive."""
    if m == 0 or n == 0:
        return 0
    if X[m-1] == Y[n-1]:
        return 1 + lcs_recursivo(X, Y, m-1, n-1)
    else:
        return max(lcs_recursivo(X, Y, m, n-1), lcs_recursivo(X, Y, m-1, n))

def lcs_programacion_dinamica(X, Y):
    """
    Solución con programación dinámica.
    Complejidad: O(m * n)
    """
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Construir tabla dp
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

def lcs_obtener_subsecuencia(X, Y):
    """
    Obtiene la subsecuencia común más larga (no solo la longitud).
    """
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Construir tabla
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruir la subsecuencia
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs.append(X[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))

# Ejemplo
X = "ABCDGH"
Y = "AEDFHR"
print(f"String 1: '{X}'")
print(f"String 2: '{Y}'")

longitud = lcs_programacion_dinamica(X, Y)
subsecuencia = lcs_obtener_subsecuencia(X, Y)
print(f"Longitud de LCS: {longitud}")
print(f"LCS: '{subsecuencia}'")
print()

# =============================================================================
# 3. CAMINO MÍNIMO EN GRID
# =============================================================================
print("=== 3. Camino Mínimo en Grid ===")

def camino_minimo_grid(grid):
    """
    Encuentra la suma mínima de un camino desde (0,0) hasta (m-1, n-1).
    Solo se puede mover hacia abajo o hacia la derecha.
    Complejidad: O(m * n)
    """
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    
    # Inicializar primera fila y primera columna
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Llenar el resto de la tabla
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    
    return dp[m-1][n-1]

# Ejemplo
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print("Grid:")
for fila in grid:
    print(f"  {fila}")

suma_minima = camino_minimo_grid(grid)
print(f"\nSuma mínima del camino: {suma_minima}")
print()

# =============================================================================
# 4. NÚMEROS DE FIBONACCI (comparación con memoización)
# =============================================================================
print("=== 4. Fibonacci con Programación Dinámica ===")

@lru_cache(maxsize=None)
def fibonacci_memo(n):
    """Fibonacci con memoización usando decorador."""
    if n <= 1:
        return n
    return fibonacci_memo(n-1) + fibonacci_memo(n-2)

def fibonacci_dp(n):
    """Fibonacci con programación dinámica (bottom-up)."""
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Ejemplo
n_fib = 30
print(f"Fibonacci({n_fib}):")

inicio = time.time()
resultado_memo = fibonacci_memo(n_fib)
tiempo_memo = time.time() - inicio

inicio = time.time()
resultado_dp = fibonacci_dp(n_fib)
tiempo_dp = time.time() - inicio

print(f"  Con memoización: {resultado_memo} ({tiempo_memo*1000:.4f} ms)")
print(f"  Con DP: {resultado_dp} ({tiempo_dp*1000:.4f} ms)")
print()

# =============================================================================
# 5. COIN CHANGE (Cambio de Monedas)
# =============================================================================
print("=== 5. Problema del Cambio de Monedas ===")

def coin_change_cantidad_minima(monedas, cantidad):
    """
    Encuentra la cantidad mínima de monedas necesarias para formar una cantidad.
    Complejidad: O(cantidad * len(monedas))
    """
    dp = [float('inf')] * (cantidad + 1)
    dp[0] = 0
    
    for i in range(1, cantidad + 1):
        for moneda in monedas:
            if moneda <= i:
                dp[i] = min(dp[i], dp[i - moneda] + 1)
    
    return dp[cantidad] if dp[cantidad] != float('inf') else -1

def coin_change_numero_formas(monedas, cantidad):
    """
    Cuenta el número de formas de formar una cantidad con las monedas dadas.
    """
    dp = [0] * (cantidad + 1)
    dp[0] = 1
    
    for moneda in monedas:
        for i in range(moneda, cantidad + 1):
            dp[i] += dp[i - moneda]
    
    return dp[cantidad]

# Ejemplo
monedas = [1, 3, 4]
cantidad = 6
print(f"Monedas: {monedas}")
print(f"Cantidad objetivo: {cantidad}")

min_monedas = coin_change_cantidad_minima(monedas, cantidad)
num_formas = coin_change_numero_formas(monedas, cantidad)

print(f"Cantidad mínima de monedas: {min_monedas}")
print(f"Número de formas de formar {cantidad}: {num_formas}")
print()

# =============================================================================
# 6. LONGEST INCREASING SUBSEQUENCE (LIS)
# =============================================================================
print("=== 6. Subsecuencia Creciente Más Larga (LIS) ===")

def lis_programacion_dinamica(nums):
    """
    Encuentra la longitud de la subsecuencia creciente más larga.
    Complejidad: O(n²)
    """
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def lis_binaria(nums):
    """
    Versión optimizada usando búsqueda binaria.
    Complejidad: O(n log n)
    """
    if not nums:
        return 0
    
    tails = []
    
    for num in nums:
        # Búsqueda binaria para encontrar la posición
        izquierda, derecha = 0, len(tails)
        while izquierda < derecha:
            medio = (izquierda + derecha) // 2
            if tails[medio] < num:
                izquierda = medio + 1
            else:
                derecha = medio
        
        if izquierda == len(tails):
            tails.append(num)
        else:
            tails[izquierda] = num
    
    return len(tails)

# Ejemplo
nums_lis = [10, 9, 2, 5, 3, 7, 101, 18]
print(f"Lista: {nums_lis}")

lis_dp = lis_programacion_dinamica(nums_lis)
lis_bin = lis_binaria(nums_lis)

print(f"LIS (DP O(n²)): {lis_dp}")
print(f"LIS (Binaria O(n log n)): {lis_bin}")
print()

# Resumen
print("=== RESUMEN ===")
print("""
Problemas de Programación Dinámica implementados:

1. Problema de la Mochila (0/1 Knapsack):
   - Recursivo: O(2^n)
   - Memoización: O(n * capacidad)
   - Programación Dinámica: O(n * capacidad)

2. Subsecuencia Común Más Larga (LCS):
   - Encuentra la subsecuencia común más larga entre dos strings
   - Complejidad: O(m * n)

3. Camino Mínimo en Grid:
   - Encuentra el camino con suma mínima en un grid
   - Solo movimientos: abajo o derecha
   - Complejidad: O(m * n)

4. Fibonacci:
   - Ejemplo clásico de optimización con DP
   - De O(2^n) a O(n)

5. Cambio de Monedas (Coin Change):
   - Cantidad mínima de monedas
   - Número de formas
   - Complejidad: O(cantidad * num_monedas)

6. Subsecuencia Creciente Más Larga (LIS):
   - DP: O(n²)
   - Búsqueda binaria: O(n log n)

Principios de Programación Dinámica:
- Dividir el problema en subproblemas más pequeños
- Almacenar resultados de subproblemas (memoización)
- Construir solución desde subproblemas (bottom-up)
- Evitar recalcular subproblemas

Cuándo usar DP:
- Problemas con subestructura óptima
- Subproblemas superpuestos
- Problemas de optimización
- Problemas de conteo/permutaciones
""")
