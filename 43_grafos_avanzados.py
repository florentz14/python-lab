# Archivo: 43_grafos_avanzados.py
# Descripción: Algoritmos Avanzados de Grafos

from collections import deque, defaultdict
import sys

print("=== Algoritmos Avanzados de Grafos ===\n")

# =============================================================================
# 1. ALGORITMO DE FLOYD-WARSHALL (Todos los Caminos Más Cortos)
# =============================================================================
print("=== 1. Algoritmo de Floyd-Warshall ===")

def floyd_warshall(grafo, num_nodos):
    """
    Encuentra los caminos más cortos entre todos los pares de nodos.
    Funciona con pesos negativos (pero no ciclos negativos).
    Complejidad: O(V³) donde V es el número de nodos
    """
    # Inicializar matriz de distancias
    dist = [[float('inf')] * num_nodos for _ in range(num_nodos)]
    
    # Distancia de un nodo a sí mismo es 0
    for i in range(num_nodos):
        dist[i][i] = 0
    
    # Distancias iniciales de las aristas
    for u, v, peso in grafo:
        dist[u][v] = peso
    
    # Floyd-Warshall: actualizar distancias considerando cada nodo como intermedio
    for k in range(num_nodos):
        for i in range(num_nodos):
            for j in range(num_nodos):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

# Ejemplo
nodos_fw = 4
grafo_fw = [
    (0, 1, 5),
    (0, 3, 10),
    (1, 2, 3),
    (2, 3, 1),
    (3, 1, 2)
]

print(f"Grafo dirigido con {nodos_fw} nodos:")
for u, v, peso in grafo_fw:
    print(f"  {u} --{peso}--> {v}")

distancias = floyd_warshall(grafo_fw, nodos_fw)

print("\nMatriz de distancias más cortas (Floyd-Warshall):")
print("    ", end="")
for j in range(nodos_fw):
    print(f"{j:6d}", end="")
print()
for i in range(nodos_fw):
    print(f"{i}: ", end="")
    for j in range(nodos_fw):
        if distancias[i][j] == float('inf'):
            print("   INF", end="")
        else:
            print(f"{distancias[i][j]:6.1f}", end="")
    print()
print()

# =============================================================================
# 2. ALGORITMO DE BELLMAN-FORD
# =============================================================================
print("=== 2. Algoritmo de Bellman-Ford ===")

def bellman_ford(grafo, num_nodos, origen):
    """
    Encuentra los caminos más cortos desde un nodo origen.
    Funciona con pesos negativos y detecta ciclos negativos.
    Complejidad: O(V * E) donde V=nodos, E=aristas
    """
    distancias = [float('inf')] * num_nodos
    distancias[origen] = 0
    
    # Relajar todas las aristas V-1 veces
    for _ in range(num_nodos - 1):
        for u, v, peso in grafo:
            if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
                distancias[v] = distancias[u] + peso
    
    # Verificar ciclos negativos
    ciclo_negativo = False
    for u, v, peso in grafo:
        if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
            ciclo_negativo = True
            break
    
    return distancias, ciclo_negativo

# Ejemplo
nodos_bf = 5
grafo_bf = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3)
]

print(f"Grafo dirigido con {nodos_bf} nodos (puede tener pesos negativos):")
for u, v, peso in grafo_bf:
    print(f"  {u} --{peso}--> {v}")

origen_bf = 0
distancias_bf, ciclo = bellman_ford(grafo_bf, nodos_bf, origen_bf)

print(f"\nDistancias más cortas desde nodo {origen_bf}:")
if ciclo:
    print("  ⚠️  ADVERTENCIA: Se detectó un ciclo negativo!")
else:
    for i, dist in enumerate(distancias_bf):
        if dist == float('inf'):
            print(f"  Nodo {i}: INFINITO")
        else:
            print(f"  Nodo {i}: {dist}")
print()

# =============================================================================
# 3. TOPOLOGICAL SORT (Ordenamiento Topológico)
# =============================================================================
print("=== 3. Ordenamiento Topológico ===")

def topological_sort_kahn(grafo, num_nodos):
    """
    Ordenamiento topológico usando algoritmo de Kahn (BFS-based).
    Complejidad: O(V + E)
    """
    # Calcular grados de entrada
    grados_entrada = [0] * num_nodos
    lista_adyacencia = defaultdict(list)
    
    for u, v in grafo:
        lista_adyacencia[u].append(v)
        grados_entrada[v] += 1
    
    # Cola de nodos sin dependencias
    cola = deque([i for i in range(num_nodos) if grados_entrada[i] == 0])
    orden = []
    
    while cola:
        nodo = cola.popleft()
        orden.append(nodo)
        
        for vecino in lista_adyacencia[nodo]:
            grados_entrada[vecino] -= 1
            if grados_entrada[vecino] == 0:
                cola.append(vecino)
    
    # Si no se procesaron todos los nodos, hay un ciclo
    if len(orden) != num_nodos:
        return None  # Ciclo detectado
    
    return orden

def topological_sort_dfs(grafo, num_nodos):
    """
    Ordenamiento topológico usando DFS.
    Complejidad: O(V + E)
    """
    lista_adyacencia = defaultdict(list)
    for u, v in grafo:
        lista_adyacencia[u].append(v)
    
    visitados = [False] * num_nodos
    pila_recursion = [False] * num_nodos
    resultado = []
    ciclo_detectado = False
    
    def dfs(nodo):
        nonlocal ciclo_detectado
        if pila_recursion[nodo]:
            ciclo_detectado = True
            return
        if visitados[nodo]:
            return
        
        visitados[nodo] = True
        pila_recursion[nodo] = True
        
        for vecino in lista_adyacencia[nodo]:
            dfs(vecino)
        
        pila_recursion[nodo] = False
        resultado.append(nodo)
    
    for i in range(num_nodos):
        if not visitados[i]:
            dfs(i)
    
    if ciclo_detectado:
        return None
    
    resultado.reverse()
    return resultado

# Ejemplo
nodos_top = 6
grafo_top = [
    (5, 2),
    (5, 0),
    (4, 0),
    (4, 1),
    (2, 3),
    (3, 1)
]

print(f"Grafo dirigido acíclico (DAG) con {nodos_top} nodos:")
for u, v in grafo_top:
    print(f"  {u} --> {v}")

orden_kahn = topological_sort_kahn(grafo_top, nodos_top)
orden_dfs = topological_sort_dfs(grafo_top, nodos_top)

print(f"\nOrdenamiento topológico (Kahn): {orden_kahn}")
print(f"Ordenamiento topológico (DFS): {orden_dfs}")
print()

# =============================================================================
# 4. DETECCIÓN DE CICLOS (Cycle Detection)
# =============================================================================
print("=== 4. Detección de Ciclos en Grafos ===")

def detectar_ciclo_dfs(grafo, num_nodos):
    """
    Detecta si hay un ciclo en un grafo dirigido usando DFS.
    """
    lista_adyacencia = defaultdict(list)
    for u, v in grafo:
        lista_adyacencia[u].append(v)
    
    visitados = [False] * num_nodos
    pila_recursion = [False] * num_nodos
    ciclo_encontrado = False
    
    def dfs(nodo):
        nonlocal ciclo_encontrado
        if pila_recursion[nodo]:
            ciclo_encontrado = True
            return
        if visitados[nodo]:
            return
        
        visitados[nodo] = True
        pila_recursion[nodo] = True
        
        for vecino in lista_adyacencia[nodo]:
            if not ciclo_encontrado:
                dfs(vecino)
        
        pila_recursion[nodo] = False
    
    for i in range(num_nodos):
        if not visitados[i] and not ciclo_encontrado:
            dfs(i)
    
    return ciclo_encontrado

def detectar_ciclo_union_find(grafo, num_nodos):
    """
    Detecta ciclos en grafo no dirigido usando Union-Find.
    """
    class UnionFind:
        def __init__(self, n):
            self.padre = list(range(n))
        
        def encontrar(self, x):
            if self.padre[x] != x:
                self.padre[x] = self.encontrar(self.padre[x])
            return self.padre[x]
        
        def unir(self, x, y):
            raiz_x = self.encontrar(x)
            raiz_y = self.encontrar(y)
            if raiz_x == raiz_y:
                return False  # Ya están en el mismo conjunto (ciclo)
            self.padre[raiz_x] = raiz_y
            return True
    
    uf = UnionFind(num_nodos)
    
    for u, v in grafo:
        if not uf.unir(u, v):
            return True  # Ciclo detectado
    
    return False

# Ejemplo
grafo_con_ciclo = [
    (0, 1),
    (1, 2),
    (2, 0)
]

grafo_sin_ciclo = [
    (0, 1),
    (1, 2),
    (2, 3)
]

print("Grafo con ciclo (0->1->2->0):")
ciclo1 = detectar_ciclo_dfs(grafo_con_ciclo, 3)
print(f"  Ciclo detectado: {ciclo1}")

print("\nGrafo sin ciclo (0->1->2->3):")
ciclo2 = detectar_ciclo_dfs(grafo_sin_ciclo, 4)
print(f"  Ciclo detectado: {ciclo2}")

# Union-Find para grafo no dirigido
grafo_no_dirigido_ciclo = [
    (0, 1),
    (1, 2),
    (2, 0)
]
print("\nGrafo no dirigido con ciclo:")
ciclo3 = detectar_ciclo_union_find(grafo_no_dirigido_ciclo, 3)
print(f"  Ciclo detectado (Union-Find): {ciclo3}")
print()

# =============================================================================
# 5. STRONGLY CONNECTED COMPONENTS (Kosaraju's Algorithm)
# =============================================================================
print("=== 5. Componentes Fuertemente Conexos (Kosaraju) ===")

def kosaraju_scc(grafo, num_nodos):
    """
    Encuentra las componentes fuertemente conexas usando algoritmo de Kosaraju.
    Complejidad: O(V + E)
    """
    # Construir grafo y grafo transpuesto
    lista_adyacencia = defaultdict(list)
    lista_adyacencia_transpuesto = defaultdict(list)
    
    for u, v in grafo:
        lista_adyacencia[u].append(v)
        lista_adyacencia_transpuesto[v].append(u)
    
    # Paso 1: DFS en grafo original para obtener orden de finalización
    visitados = [False] * num_nodos
    pila = []
    
    def dfs1(nodo):
        visitados[nodo] = True
        for vecino in lista_adyacencia[nodo]:
            if not visitados[vecino]:
                dfs1(vecino)
        pila.append(nodo)
    
    for i in range(num_nodos):
        if not visitados[i]:
            dfs1(i)
    
    # Paso 2: DFS en grafo transpuesto en orden inverso
    visitados = [False] * num_nodos
    componentes = []
    
    def dfs2(nodo, componente):
        visitados[nodo] = True
        componente.append(nodo)
        for vecino in lista_adyacencia_transpuesto[nodo]:
            if not visitados[vecino]:
                dfs2(vecino, componente)
    
    while pila:
        nodo = pila.pop()
        if not visitados[nodo]:
            componente = []
            dfs2(nodo, componente)
            componentes.append(componente)
    
    return componentes

# Ejemplo
nodos_scc = 8
grafo_scc = [
    (0, 1),
    (1, 2),
    (2, 0),
    (1, 3),
    (3, 4),
    (4, 5),
    (5, 3),
    (6, 5),
    (6, 7),
    (7, 6)
]

print(f"Grafo dirigido con {nodos_scc} nodos:")
for u, v in grafo_scc:
    print(f"  {u} --> {v}")

sccs = kosaraju_scc(grafo_scc, nodos_scc)
print(f"\nComponentes fuertemente conexas (SCC): {len(sccs)}")
for i, componente in enumerate(sccs):
    print(f"  SCC {i+1}: {componente}")
print()

# Resumen
print("=== RESUMEN ===")
print("""
Algoritmos avanzados de grafos implementados:

1. Floyd-Warshall:
   - Todos los caminos más cortos entre todos los pares
   - Complejidad: O(V³)
   - Funciona con pesos negativos (sin ciclos negativos)

2. Bellman-Ford:
   - Camino más corto desde un origen
   - Complejidad: O(V * E)
   - Detecta ciclos negativos

3. Topological Sort:
   - Ordenamiento de nodos en DAG
   - Algoritmos: Kahn (BFS) y DFS
   - Complejidad: O(V + E)

4. Detección de Ciclos:
   - DFS para grafos dirigidos
   - Union-Find para grafos no dirigidos
   - Complejidad: O(V + E)

5. Componentes Fuertemente Conexas (Kosaraju):
   - Encuentra SCC en grafo dirigido
   - Complejidad: O(V + E)

Aplicaciones:
- Floyd-Warshall: Redes, routing
- Bellman-Ford: Detección de ciclos negativos
- Topological Sort: Dependencias, compilación
- Cycle Detection: Validación de grafos
- SCC: Análisis de redes sociales, web crawling
""")
