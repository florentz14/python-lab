# Archivo: 47_backtracking.py
# Descripción: Algoritmos de Backtracking

print("=== Algoritmos de Backtracking ===\n")

# =============================================================================
# 1. PROBLEMA DE LAS N-REINAS
# =============================================================================
print("=== 1. Problema de las N-Reinas ===")

def es_seguro(tablero, fila, col, n):
    """Verifica si es seguro colocar una reina en (fila, col)."""
    # Verificar fila (solo hacia la izquierda, ya que no hemos colocado reinas a la derecha)
    for i in range(col):
        if tablero[fila][i] == 1:
            return False
    
    # Verificar diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False
    
    # Verificar diagonal inferior izquierda
    for i, j in zip(range(fila, n, 1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False
    
    return True

def n_reinas_backtracking(tablero, col, n, soluciones):
    """Resuelve el problema de las N-Reinas usando backtracking."""
    # Caso base: todas las reinas están colocadas
    if col >= n:
        # Guardar solución (copia del tablero)
        soluciones.append([fila[:] for fila in tablero])
        return True
    
    # Intentar colocar reina en cada fila de esta columna
    res = False
    for fila in range(n):
        if es_seguro(tablero, fila, col, n):
            # Colocar reina
            tablero[fila][col] = 1
            
            # Recursión para las siguientes columnas
            res = n_reinas_backtracking(tablero, col + 1, n, soluciones) or res
            
            # Backtrack: quitar la reina
            tablero[fila][col] = 0
    
    return res

def resolver_n_reinas(n, encontrar_todas=True):
    """Resuelve el problema de las N-Reinas."""
    tablero = [[0] * n for _ in range(n)]
    soluciones = []
    
    n_reinas_backtracking(tablero, 0, n, soluciones)
    
    return soluciones

def imprimir_tablero(tablero):
    """Imprime el tablero de forma visual."""
    n = len(tablero)
    print("  " + " ".join(str(i) for i in range(n)))
    for i, fila in enumerate(tablero):
        print(f"{i} " + " ".join("Q" if celda == 1 else "." for celda in fila))

# Ejemplo
n_reinas = 4
print(f"Problema de las {n_reinas}-Reinas:")
soluciones = resolver_n_reinas(n_reinas, encontrar_todas=True)
print(f"\nNúmero de soluciones encontradas: {len(soluciones)}")

if soluciones:
    print("\nPrimera solución:")
    imprimir_tablero(soluciones[0])
print()

# =============================================================================
# 2. SOLUCIONADOR DE SUDOKU
# =============================================================================
print("=== 2. Solucionador de Sudoku ===")

def es_valido_sudoku(tablero, fila, col, num):
    """Verifica si es válido colocar num en (fila, col)."""
    n = len(tablero)
    tam_cuadrante = int(n ** 0.5)
    
    # Verificar fila
    for j in range(n):
        if tablero[fila][j] == num:
            return False
    
    # Verificar columna
    for i in range(n):
        if tablero[i][col] == num:
            return False
    
    # Verificar cuadrante 3x3 (o n x n)
    inicio_fila = (fila // tam_cuadrante) * tam_cuadrante
    inicio_col = (col // tam_cuadrante) * tam_cuadrante
    
    for i in range(inicio_fila, inicio_fila + tam_cuadrante):
        for j in range(inicio_col, inicio_col + tam_cuadrante):
            if tablero[i][j] == num:
                return False
    
    return True

def resolver_sudoku(tablero):
    """Resuelve el Sudoku usando backtracking."""
    n = len(tablero)
    
    # Buscar celda vacía
    fila_vacia = col_vacia = -1
    for i in range(n):
        for j in range(n):
            if tablero[i][j] == 0:
                fila_vacia, col_vacia = i, j
                break
        if fila_vacia != -1:
            break
    
    # Si no hay celdas vacías, el Sudoku está resuelto
    if fila_vacia == -1:
        return True
    
    # Intentar números del 1 al 9
    for num in range(1, n + 1):
        if es_valido_sudoku(tablero, fila_vacia, col_vacia, num):
            # Colocar número
            tablero[fila_vacia][col_vacia] = num
            
            # Recursión
            if resolver_sudoku(tablero):
                return True
            
            # Backtrack
            tablero[fila_vacia][col_vacia] = 0
    
    return False

def imprimir_sudoku(tablero):
    """Imprime el Sudoku de forma visual."""
    n = len(tablero)
    tam_cuadrante = int(n ** 0.5)
    
    for i in range(n):
        if i % tam_cuadrante == 0 and i != 0:
            print("-" * (n * 2 + tam_cuadrante))
        for j in range(n):
            if j % tam_cuadrante == 0 and j != 0:
                print("|", end=" ")
            print(tablero[i][j] if tablero[i][j] != 0 else ".", end=" ")
        print()

# Ejemplo
sudoku_ejemplo = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku original:")
imprimir_sudoku(sudoku_ejemplo)

if resolver_sudoku(sudoku_ejemplo):
    print("\nSudoku resuelto:")
    imprimir_sudoku(sudoku_ejemplo)
else:
    print("\nNo se encontró solución")
print()

# =============================================================================
# 3. RESOLUCIÓN DE LABERINTOS
# =============================================================================
print("=== 3. Resolución de Laberintos ===")

def resolver_laberinto(laberinto, inicio, destino):
    """
    Resuelve un laberinto usando backtracking.
    0 = camino libre, 1 = pared
    Retorna el camino si existe, None si no.
    """
    n, m = len(laberinto), len(laberinto[0])
    visitados = [[False] * m for _ in range(n)]
    camino = []
    
    direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # derecha, abajo, izquierda, arriba
    
    def es_valido(x, y):
        return (0 <= x < n and 0 <= y < m and 
                laberinto[x][y] == 0 and not visitados[x][y])
    
    def backtrack(x, y):
        # Caso base: llegamos al destino
        if (x, y) == destino:
            camino.append((x, y))
            return True
        
        # Marcar como visitado
        visitados[x][y] = True
        camino.append((x, y))
        
        # Intentar todas las direcciones
        for dx, dy in direcciones:
            nuevo_x, nuevo_y = x + dx, y + dy
            if es_valido(nuevo_x, nuevo_y):
                if backtrack(nuevo_x, nuevo_y):
                    return True
        
        # Backtrack: quitar del camino
        camino.pop()
        return False
    
    if backtrack(inicio[0], inicio[1]):
        return camino
    return None

def imprimir_laberinto_con_camino(laberinto, camino):
    """Imprime el laberinto marcando el camino."""
    n, m = len(laberinto), len(laberinto[0])
    solucion = [[' ' if laberinto[i][j] == 0 else '#' for j in range(m)] for i in range(n)]
    
    for x, y in camino:
        solucion[x][y] = '*'
    
    # Marcar inicio y destino
    if camino:
        solucion[camino[0][0]][camino[0][1]] = 'S'  # Start
        solucion[camino[-1][0]][camino[-1][1]] = 'E'  # End
    
    print("  " + "".join(str(i % 10) for i in range(m)))
    for i, fila in enumerate(solucion):
        print(f"{i % 10} " + "".join(fila))

# Ejemplo
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

inicio = (0, 0)
destino = (4, 4)

print("Laberinto (0=camino, 1=pared):")
for fila in laberinto:
    print(f"  {fila}")

camino = resolver_laberinto(laberinto, inicio, destino)

if camino:
    print(f"\nCamino encontrado ({len(camino)} pasos):")
    imprimir_laberinto_con_camino(laberinto, camino)
else:
    print("\nNo se encontró camino")
print()

# =============================================================================
# 4. GENERACIÓN DE PERMUTACIONES (Backtracking)
# =============================================================================
print("=== 4. Generación de Permutaciones (Backtracking) ===")

def permutaciones_backtracking(elements):
    """Genera todas las permutaciones usando backtracking."""
    resultado = []
    n = len(elements)
    
    def backtrack(permutacion_actual, usados):
        # Caso base: permutación completa
        if len(permutacion_actual) == n:
            resultado.append(permutacion_actual[:])
            return
        
        # Intentar agregar cada elemento no usado
        for i in range(n):
            if not usados[i]:
                permutacion_actual.append(elements[i])
                usados[i] = True
                backtrack(permutacion_actual, usados)
                # Backtrack
                permutacion_actual.pop()
                usados[i] = False
    
    backtrack([], [False] * n)
    return resultado

# Ejemplo
elementos = [1, 2, 3]
perms = permutaciones_backtracking(elementos)
print(f"Permutaciones de {elementos}:")
for i, perm in enumerate(perms, 1):
    print(f"  {i}. {perm}")
print(f"Total: {len(perms)} permutaciones")
print()

# =============================================================================
# 5. GENERACIÓN DE COMBINACIONES (Backtracking)
# =============================================================================
print("=== 5. Generación de Combinaciones (Backtracking) ===")

def combinaciones_backtracking(elements, k):
    """Genera todas las combinaciones de k elementos usando backtracking."""
    resultado = []
    n = len(elements)
    
    def backtrack(combinacion_actual, inicio):
        # Caso base: combinación completa
        if len(combinacion_actual) == k:
            resultado.append(combinacion_actual[:])
            return
        
        # Intentar agregar elementos desde inicio hasta el final
        for i in range(inicio, n):
            combinacion_actual.append(elements[i])
            backtrack(combinacion_actual, i + 1)
            # Backtrack
            combinacion_actual.pop()
    
    backtrack([], 0)
    return resultado

# Ejemplo
elementos_comb = ['A', 'B', 'C', 'D']
k = 2
combs = combinaciones_backtracking(elementos_comb, k)
print(f"Combinaciones de {elementos_comb} tomando {k} elementos:")
for i, comb in enumerate(combs, 1):
    print(f"  {i}. {comb}")
print(f"Total: {len(combs)} combinaciones (C({len(elementos_comb)}, {k}) = {len(combs)})")
print()

# =============================================================================
# 6. SUBSET SUM (Suma de Subconjuntos)
# =============================================================================
print("=== 6. Problema de Suma de Subconjuntos (Subset Sum) ===")

def subset_sum_backtracking(numeros, objetivo):
    """Encuentra un subconjunto que sume exactamente el objetivo."""
    resultado = []
    n = len(numeros)
    
    def backtrack(subconjunto_actual, indice, suma_actual):
        # Caso base: suma igual al objetivo
        if suma_actual == objetivo:
            resultado.append(subconjunto_actual[:])
            return
        
        # Caso base: nos pasamos o no quedan elementos
        if suma_actual > objetivo or indice >= n:
            return
        
        # Incluir el elemento actual
        subconjunto_actual.append(numeros[indice])
        backtrack(subconjunto_actual, indice + 1, suma_actual + numeros[indice])
        subconjunto_actual.pop()
        
        # No incluir el elemento actual
        backtrack(subconjunto_actual, indice + 1, suma_actual)
    
    backtrack([], 0, 0)
    return resultado

# Ejemplo
numeros_subset = [3, 34, 4, 12, 5, 2]
objetivo_subset = 9
soluciones_subset = subset_sum_backtracking(numeros_subset, objetivo_subset)

print(f"Números: {numeros_subset}")
print(f"Objetivo: {objetivo_subset}")
print(f"Subconjuntos que suman {objetivo_subset}:")
for sol in soluciones_subset:
    print(f"  {sol} (suma = {sum(sol)})")
print()

# Resumen
print("=== RESUMEN ===")
print("""
Algoritmos de Backtracking implementados:

1. Problema de las N-Reinas:
   - Colocar N reinas en un tablero NxN sin que se ataquen
   - Complejidad: O(N!)
   - Ejemplo clásico de backtracking

2. Solucionador de Sudoku:
   - Resuelve Sudokus 9x9 usando backtracking
   - Complejidad: O(9^m) donde m es número de celdas vacías
   - Puede resolver cualquier Sudoku válido

3. Resolución de Laberintos:
   - Encuentra camino desde inicio a destino
   - Complejidad: O(4^(n*m)) en peor caso
   - Usa backtracking para explorar todas las rutas

4. Generación de Permutaciones:
   - Genera todas las permutaciones de n elementos
   - Complejidad: O(n! * n)
   - Ejemplo fundamental de backtracking

5. Generación de Combinaciones:
   - Genera combinaciones de k elementos de n
   - Complejidad: O(C(n,k) * k)
   - Útil para problemas combinatorios

6. Subset Sum:
   - Encuentra subconjuntos que sumen un objetivo
   - Complejidad: O(2^n)
   - Problema NP-completo

Características del Backtracking:
- Técnica de búsqueda sistemática
- Construye soluciones incrementalmente
- Abandona soluciones parciales si no pueden llevar a solución válida
- Útil para problemas de decisión y optimización
- Generalmente exponencial en complejidad temporal

Cuándo usar Backtracking:
- Problemas con restricciones
- Búsqueda exhaustiva necesaria
- Problemas combinatorios
- Puzzles y juegos
- Optimización discreta
""")
