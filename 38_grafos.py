# Archivo: 38_grafos.py
# Descripción: Estructuras de datos - Grafos

from collections import deque, defaultdict

print("=== Estructuras de Datos: Grafos ===\n")

# =============================================================================
# 1. GRAFO USANDO LISTA DE ADYACENCIA
# =============================================================================
print("=== 1. Grafo con Lista de Adyacencia ===")

class GrafoListaAdyacencia:
    """Grafo implementado con lista de adyacencia."""
    
    def __init__(self, dirigido=False):
        self.grafo = defaultdict(list)
        self.dirigido = dirigido
    
    def agregar_arista(self, origen, destino, peso=1):
        """Agrega una arista al grafo."""
        self.grafo[origen].append((destino, peso))
        if not self.dirigido:
            self.grafo[destino].append((origen, peso))
    
    def obtener_vecinos(self, nodo):
        """Obtiene los vecinos de un nodo."""
        return self.grafo[nodo]
    
    def obtener_nodos(self):
        """Obtiene todos los nodos del grafo."""
        return list(self.grafo.keys())
    
    def imprimir_grafo(self):
        """Imprime el grafo."""
        for nodo in self.grafo:
            print(f"{nodo}: {self.grafo[nodo]}")
    
    def bfs(self, inicio):
        """Recorrido en anchura (Breadth First Search)."""
        visitados = set()
        cola = deque([inicio])
        visitados.add(inicio)
        resultado = []
        
        while cola:
            nodo = cola.popleft()
            resultado.append(nodo)
            
            for vecino, _ in self.grafo[nodo]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        
        return resultado
    
    def dfs(self, inicio):
        """Recorrido en profundidad (Depth First Search)."""
        visitados = set()
        resultado = []
        
        def _dfs_recursivo(nodo):
            visitados.add(nodo)
            resultado.append(nodo)
            
            for vecino, _ in self.grafo[nodo]:
                if vecino not in visitados:
                    _dfs_recursivo(vecino)
        
        _dfs_recursivo(inicio)
        return resultado
    
    def dfs_iterativo(self, inicio):
        """DFS iterativo usando pila."""
        visitados = set()
        pila = [inicio]
        resultado = []
        
        while pila:
            nodo = pila.pop()
            if nodo not in visitados:
                visitados.add(nodo)
                resultado.append(nodo)
                # Agregar vecinos en orden inverso para mantener orden
                for vecino, _ in reversed(self.grafo[nodo]):
                    if vecino not in visitados:
                        pila.append(vecino)
        
        return resultado

# Ejemplo
print("Creando grafo no dirigido:")
grafo = GrafoListaAdyacencia(dirigido=False)
grafo.agregar_arista('A', 'B')
grafo.agregar_arista('A', 'C')
grafo.agregar_arista('B', 'D')
grafo.agregar_arista('C', 'D')
grafo.agregar_arista('D', 'E')

print("Grafo (lista de adyacencia):")
grafo.imprimir_grafo()
print(f"\nBFS desde 'A': {grafo.bfs('A')}")
print(f"DFS desde 'A': {grafo.dfs('A')}")
print(f"DFS iterativo desde 'A': {grafo.dfs_iterativo('A')}")
print()

# =============================================================================
# 2. GRAFO CON MATRIZ DE ADYACENCIA
# =============================================================================
print("=== 2. Grafo con Matriz de Adyacencia ===")

class GrafoMatrizAdyacencia:
    """Grafo implementado con matriz de adyacencia."""
    
    def __init__(self, num_nodos, dirigido=False):
        self.num_nodos = num_nodos
        self.dirigido = dirigido
        self.matriz = [[0] * num_nodos for _ in range(num_nodos)]
        self.nodos = {}
        self.indices = {}
        self.contador = 0
    
    def agregar_nodo(self, nombre):
        """Agrega un nodo al grafo."""
        if nombre not in self.nodos:
            self.nodos[nombre] = self.contador
            self.indices[self.contador] = nombre
            self.contador += 1
    
    def agregar_arista(self, origen, destino, peso=1):
        """Agrega una arista al grafo."""
        self.agregar_nodo(origen)
        self.agregar_nodo(destino)
        
        i = self.nodos[origen]
        j = self.nodos[destino]
        
        self.matriz[i][j] = peso
        if not self.dirigido:
            self.matriz[j][i] = peso
    
    def imprimir_matriz(self):
        """Imprime la matriz de adyacencia."""
        print("Matriz de adyacencia:")
        print("   ", end="")
        for i in range(self.contador):
            print(f"{self.indices[i]:4s}", end="")
        print()
        
        for i in range(self.contador):
            print(f"{self.indices[i]:3s}", end=" ")
            for j in range(self.contador):
                print(f"{self.matriz[i][j]:4d}", end="")
            print()
    
    def obtener_vecinos(self, nodo):
        """Obtiene los vecinos de un nodo."""
        if nodo not in self.nodos:
            return []
        
        i = self.nodos[nodo]
        vecinos = []
        for j in range(self.contador):
            if self.matriz[i][j] != 0:
                vecinos.append((self.indices[j], self.matriz[i][j]))
        return vecinos

# Ejemplo
print("Creando grafo con matriz de adyacencia:")
grafo_matriz = GrafoMatrizAdyacencia(5, dirigido=False)
grafo_matriz.agregar_arista('A', 'B', 1)
grafo_matriz.agregar_arista('A', 'C', 1)
grafo_matriz.agregar_arista('B', 'D', 1)
grafo_matriz.agregar_arista('C', 'D', 1)
grafo_matriz.agregar_arista('D', 'E', 1)

grafo_matriz.imprimir_matriz()
print(f"Vecinos de 'A': {grafo_matriz.obtener_vecinos('A')}")
print()

# =============================================================================
# 3. ALGORITMOS DE BÚSQUEDA
# =============================================================================
print("=== 3. Algoritmos de Búsqueda ===")

class GrafoCompleto(GrafoListaAdyacencia):
    """Grafo con algoritmos completos."""
    
    def buscar_camino(self, inicio, destino):
        """Busca un camino entre dos nodos usando BFS."""
        if inicio == destino:
            return [inicio]
        
        visitados = set()
        cola = deque([(inicio, [inicio])])
        visitados.add(inicio)
        
        while cola:
            nodo, camino = cola.popleft()
            
            for vecino, _ in self.grafo[nodo]:
                if vecino == destino:
                    return camino + [vecino]
                
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append((vecino, camino + [vecino]))
        
        return None  # No hay camino
    
    def todos_los_caminos(self, inicio, destino):
        """Encuentra todos los caminos entre dos nodos."""
        caminos = []
        
        def _buscar_caminos(nodo_actual, destino, visitados, camino_actual):
            visitados.add(nodo_actual)
            camino_actual.append(nodo_actual)
            
            if nodo_actual == destino:
                caminos.append(camino_actual.copy())
            else:
                for vecino, _ in self.grafo[nodo_actual]:
                    if vecino not in visitados:
                        _buscar_caminos(vecino, destino, visitados, camino_actual)
            
            camino_actual.pop()
            visitados.remove(nodo_actual)
        
        _buscar_caminos(inicio, destino, set(), [])
        return caminos
    
    def componentes_conexas(self):
        """Encuentra todas las componentes conexas."""
        visitados = set()
        componentes = []
        
        for nodo in self.grafo:
            if nodo not in visitados:
                componente = self.bfs(nodo)
                componentes.append(componente)
                visitados.update(componente)
        
        return componentes

# Ejemplo
print("Búsqueda de caminos:")
grafo_caminos = GrafoCompleto(dirigido=False)
grafo_caminos.agregar_arista('A', 'B')
grafo_caminos.agregar_arista('A', 'C')
grafo_caminos.agregar_arista('B', 'D')
grafo_caminos.agregar_arista('C', 'D')
grafo_caminos.agregar_arista('D', 'E')

camino = grafo_caminos.buscar_camino('A', 'E')
print(f"Camino de A a E: {camino}")

todos_caminos = grafo_caminos.todos_los_caminos('A', 'D')
print(f"Todos los caminos de A a D: {todos_caminos}")

componentes = grafo_caminos.componentes_conexas()
print(f"Componentes conexas: {componentes}")
print()

# =============================================================================
# 4. ALGORITMO DE DIJKSTRA (CAMINO MÁS CORTO)
# =============================================================================
print("=== 4. Algoritmo de Dijkstra (Camino Más Corto) ===")

def dijkstra(grafo, inicio):
    """
    Algoritmo de Dijkstra para encontrar el camino más corto.
    """
    distancias = {nodo: float('inf') for nodo in grafo.obtener_nodos()}
    distancias[inicio] = 0
    visitados = set()
    
    # Cola de prioridad simple (podría usar heapq para eficiencia)
    while len(visitados) < len(distancias):
        # Encontrar nodo no visitado con menor distancia
        nodo_actual = None
        min_distancia = float('inf')
        
        for nodo, distancia in distancias.items():
            if nodo not in visitados and distancia < min_distancia:
                min_distancia = distancia
                nodo_actual = nodo
        
        if nodo_actual is None:
            break
        
        visitados.add(nodo_actual)
        
        # Actualizar distancias de vecinos
        for vecino, peso in grafo.obtener_vecinos(nodo_actual):
            if vecino not in visitados:
                nueva_distancia = distancias[nodo_actual] + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
    
    return distancias

# Ejemplo
print("Grafo con pesos:")
grafo_pesos = GrafoListaAdyacencia(dirigido=False)
grafo_pesos.agregar_arista('A', 'B', 4)
grafo_pesos.agregar_arista('A', 'C', 2)
grafo_pesos.agregar_arista('B', 'C', 1)
grafo_pesos.agregar_arista('B', 'D', 5)
grafo_pesos.agregar_arista('C', 'D', 8)
grafo_pesos.agregar_arista('C', 'E', 10)
grafo_pesos.agregar_arista('D', 'E', 2)

distancias = dijkstra(grafo_pesos, 'A')
print(f"Distancias más cortas desde 'A': {distancias}")
print()

# =============================================================================
# 5. DETECCIÓN DE CICLOS
# =============================================================================
print("=== 5. Detección de Ciclos ===")

def tiene_ciclo(grafo, dirigido=True):
    """Detecta si el grafo tiene ciclos."""
    if dirigido:
        return _tiene_ciclo_dirigido(grafo)
    else:
        return _tiene_ciclo_no_dirigido(grafo)

def _tiene_ciclo_no_dirigido(grafo):
    """Detecta ciclos en grafo no dirigido usando DFS."""
    visitados = set()
    
    def dfs_con_padre(nodo, padre):
        visitados.add(nodo)
        for vecino, _ in grafo.obtener_vecinos(nodo):
            if vecino not in visitados:
                if dfs_con_padre(vecino, nodo):
                    return True
            elif vecino != padre:
                return True
        return False
    
    for nodo in grafo.obtener_nodos():
        if nodo not in visitados:
            if dfs_con_padre(nodo, None):
                return True
    return False

def _tiene_ciclo_dirigido(grafo):
    """Detecta ciclos en grafo dirigido."""
    visitados = set()
    en_recursion = set()
    
    def dfs(nodo):
        visitados.add(nodo)
        en_recursion.add(nodo)
        
        for vecino, _ in grafo.obtener_vecinos(nodo):
            if vecino not in visitados:
                if dfs(vecino):
                    return True
            elif vecino in en_recursion:
                return True
        
        en_recursion.remove(nodo)
        return False
    
    for nodo in grafo.obtener_nodos():
        if nodo not in visitados:
            if dfs(nodo):
                return True
    return False

# Ejemplo
print("Detección de ciclos:")
grafo_ciclo = GrafoListaAdyacencia(dirigido=False)
grafo_ciclo.agregar_arista('A', 'B')
grafo_ciclo.agregar_arista('B', 'C')
grafo_ciclo.agregar_arista('C', 'A')  # Forma un ciclo

print(f"Grafo con ciclo: {tiene_ciclo(grafo_ciclo, dirigido=False)}")

grafo_sin_ciclo = GrafoListaAdyacencia(dirigido=False)
grafo_sin_ciclo.agregar_arista('A', 'B')
grafo_sin_ciclo.agregar_arista('B', 'C')
print(f"Grafo sin ciclo: {tiene_ciclo(grafo_sin_ciclo, dirigido=False)}")
print()

# =============================================================================
# 6. ORDENAMIENTO TOPOLÓGICO
# =============================================================================
print("=== 6. Ordenamiento Topológico ===")

def ordenamiento_topologico(grafo):
    """Ordenamiento topológico para grafos dirigidos acíclicos (DAG)."""
    # Calcular grados de entrada
    grados_entrada = defaultdict(int)
    for nodo in grafo.obtener_nodos():
        for vecino, _ in grafo.obtener_vecinos(nodo):
            grados_entrada[vecino] += 1
    
    # Cola con nodos sin dependencias
    cola = deque([nodo for nodo in grafo.obtener_nodos() 
                  if grados_entrada[nodo] == 0])
    
    resultado = []
    
    while cola:
        nodo = cola.popleft()
        resultado.append(nodo)
        
        for vecino, _ in grafo.obtener_vecinos(nodo):
            grados_entrada[vecino] -= 1
            if grados_entrada[vecino] == 0:
                cola.append(vecino)
    
    # Si hay nodos restantes, hay un ciclo
    if len(resultado) != len(grafo.obtener_nodos()):
        return None  # Hay ciclo
    
    return resultado

# Ejemplo
print("Ordenamiento topológico (DAG):")
grafo_dag = GrafoListaAdyacencia(dirigido=True)
grafo_dag.agregar_arista('A', 'B')
grafo_dag.agregar_arista('A', 'C')
grafo_dag.agregar_arista('B', 'D')
grafo_dag.agregar_arista('C', 'D')
grafo_dag.agregar_arista('D', 'E')

orden = ordenamiento_topologico(grafo_dag)
print(f"Orden topológico: {orden}")
print()

# =============================================================================
# 7. GRAFO PONDERADO COMPLETO
# =============================================================================
print("=== 7. Grafo Ponderado Completo ===")

class GrafoPonderado(GrafoListaAdyacencia):
    """Grafo con operaciones avanzadas para grafos ponderados."""
    
    def camino_minimo(self, inicio, destino):
        """Encuentra el camino mínimo usando Dijkstra mejorado."""
        distancias = {nodo: float('inf') for nodo in self.obtener_nodos()}
        distancias[inicio] = 0
        padres = {}
        visitados = set()
        
        while len(visitados) < len(distancias):
            nodo_actual = min((n for n in distancias.items() 
                              if n[0] not in visitados), key=lambda x: x[1])[0]
            
            if distancias[nodo_actual] == float('inf'):
                break
            
            visitados.add(nodo_actual)
            
            for vecino, peso in self.obtener_vecinos(nodo_actual):
                if vecino not in visitados:
                    nueva_distancia = distancias[nodo_actual] + peso
                    if nueva_distancia < distancias[vecino]:
                        distancias[vecino] = nueva_distancia
                        padres[vecino] = nodo_actual
        
        # Reconstruir camino
        if destino not in padres and inicio != destino:
            return None
        
        camino = []
        nodo = destino
        while nodo is not None:
            camino.append(nodo)
            nodo = padres.get(nodo)
        
        camino.reverse()
        return camino if camino[0] == inicio else None
    
    def arbol_expansion_minima(self):
        """Algoritmo de Prim para árbol de expansión mínima."""
        # Implementación simplificada
        if not self.obtener_nodos():
            return []
        
        inicio = self.obtener_nodos()[0]
        visitados = {inicio}
        aristas_mst = []
        
        while len(visitados) < len(self.obtener_nodos()):
            min_arista = None
            min_peso = float('inf')
            
            for nodo in visitados:
                for vecino, peso in self.obtener_vecinos(nodo):
                    if vecino not in visitados and peso < min_peso:
                        min_peso = peso
                        min_arista = (nodo, vecino, peso)
            
            if min_arista:
                aristas_mst.append(min_arista)
                visitados.add(min_arista[1])
        
        return aristas_mst

# Ejemplo
print("Grafo ponderado:")
grafo_pond = GrafoPonderado(dirigido=False)
grafo_pond.agregar_arista('A', 'B', 4)
grafo_pond.agregar_arista('A', 'C', 2)
grafo_pond.agregar_arista('B', 'C', 1)
grafo_pond.agregar_arista('B', 'D', 5)
grafo_pond.agregar_arista('C', 'D', 8)

camino_min = grafo_pond.camino_minimo('A', 'D')
print(f"Camino mínimo de A a D: {camino_min}")

mst = grafo_pond.arbol_expansion_minima()
print(f"Árbol de expansión mínima: {mst}")
print()

# =============================================================================
# 8. COMPARACIÓN Y RESUMEN
# =============================================================================
print("=== 8. Resumen de Representaciones de Grafos ===")
print("""
REPRESENTACIONES DE GRAFOS:

1. LISTA DE ADYACENCIA:
   - Ventajas: Eficiente en memoria, fácil agregar nodos
   - Desventajas: Más lento para verificar si existe arista
   - Complejidad: O(V + E) espacio, O(1) agregar arista
   - Uso: Grafos dispersos (pocas aristas)

2. MATRIZ DE ADYACENCIA:
   - Ventajas: Rápido verificar aristas, simple implementación
   - Desventajas: Mucha memoria para grafos dispersos
   - Complejidad: O(V²) espacio, O(1) verificar arista
   - Uso: Grafos densos (muchas aristas)

ALGORITMOS PRINCIPALES:

1. BFS (Breadth First Search):
   - Complejidad: O(V + E)
   - Usa cola
   - Encuentra camino más corto en grafos no ponderados

2. DFS (Depth First Search):
   - Complejidad: O(V + E)
   - Usa pila (recursivo o iterativo)
   - Detecta ciclos, componentes conexas

3. Dijkstra:
   - Complejidad: O((V + E) log V) con heap
   - Encuentra camino más corto en grafos ponderados
   - Requiere pesos no negativos

4. Ordenamiento Topológico:
   - Complejidad: O(V + E)
   - Solo para DAG (grafos dirigidos acíclicos)
   - Usado en scheduling, compilación

APLICACIONES:
- Redes sociales
- Sistemas de navegación (GPS)
- Redes de computadoras
- Sistemas de recomendación
- Compiladores
- Scheduling de tareas
""")
