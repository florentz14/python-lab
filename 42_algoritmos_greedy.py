# Archivo: 42_algoritmos_greedy.py
# Descripción: Algoritmos Greedy (Voraces)

print("=== Algoritmos Greedy (Voraces) ===\n")

# =============================================================================
# 1. PROBLEMA DE LA MOCHILA FRACCIONARIA (Fractional Knapsack)
# =============================================================================
print("=== 1. Problema de la Mochila Fraccionaria ===")

def mochila_fraccionaria(pesos, valores, capacidad):
    """
    Resuelve el problema de la mochila fraccionaria usando algoritmo greedy.
    Puedes tomar fracciones de los items.
    Estrategia: Tomar items con mayor valor/peso primero.
    Complejidad: O(n log n) debido al ordenamiento
    """
    n = len(pesos)
    items = [(valores[i] / pesos[i], pesos[i], valores[i], i) for i in range(n)]
    
    # Ordenar por valor/peso en orden descendente
    items.sort(reverse=True)
    
    valor_total = 0
    peso_actual = 0
    solucion = []
    
    for ratio, peso, valor, indice in items:
        if peso_actual + peso <= capacidad:
            # Tomar el item completo
            peso_actual += peso
            valor_total += valor
            solucion.append((indice, 1.0))  # 1.0 = 100% del item
        else:
            # Tomar fracción del item
            fraccion = (capacidad - peso_actual) / peso
            peso_actual = capacidad
            valor_total += valor * fraccion
            solucion.append((indice, fraccion))
            break
    
    return valor_total, solucion

# Ejemplo
pesos_mochila = [10, 20, 30]
valores_mochila = [60, 100, 120]
capacidad_mochila = 50

print(f"Pesos: {pesos_mochila}")
print(f"Valores: {valores_mochila}")
print(f"Capacidad: {capacidad_mochila}")

valor_optimo, solucion = mochila_fraccionaria(pesos_mochila, valores_mochila, capacidad_mochila)
print(f"\nValor máximo: {valor_optimo}")
print("Solución (índice, fracción):")
for indice, fraccion in solucion:
    print(f"  Item {indice}: {fraccion*100:.1f}% (peso: {pesos_mochila[indice]*fraccion:.1f}, valor: {valores_mochila[indice]*fraccion:.1f})")
print()

# =============================================================================
# 2. ACTIVITY SELECTION PROBLEM (Selección de Actividades)
# =============================================================================
print("=== 2. Problema de Selección de Actividades ===")

def seleccion_actividades(inicios, fines):
    """
    Encuentra el máximo número de actividades que no se solapan.
    Estrategia: Seleccionar actividades que terminan primero (greedy).
    Complejidad: O(n log n) debido al ordenamiento
    """
    n = len(inicios)
    actividades = list(zip(inicios, fines, range(n)))
    
    # Ordenar por tiempo de finalización
    actividades.sort(key=lambda x: x[1])
    
    seleccionadas = []
    ultimo_fin = 0
    
    for inicio, fin, indice in actividades:
        if inicio >= ultimo_fin:
            seleccionadas.append(indice)
            ultimo_fin = fin
    
    return seleccionadas

# Ejemplo
inicios = [1, 3, 0, 5, 8, 5]
fines = [2, 4, 6, 7, 9, 9]

print(f"Actividades:")
for i, (inicio, fin) in enumerate(zip(inicios, fines)):
    print(f"  Actividad {i}: [{inicio}, {fin}]")

seleccionadas = seleccion_actividades(inicios, fines)
print(f"\nNúmero máximo de actividades: {len(seleccionadas)}")
print(f"Actividades seleccionadas: {seleccionadas}")
for indice in seleccionadas:
    print(f"  Actividad {indice}: [{inicios[indice]}, {fines[indice]}]")
print()

# =============================================================================
# 3. MINIMUM SPANNING TREE - ALGORITMO DE KRUSKAL (Greedy)
# =============================================================================
print("=== 3. Algoritmo de Kruskal (MST) ===")

class UnionFind:
    """Estructura de datos Union-Find para Kruskal."""
    
    def __init__(self, n):
        self.padre = list(range(n))
        self.rango = [0] * n
    
    def encontrar(self, x):
        """Encuentra la raíz con path compression."""
        if self.padre[x] != x:
            self.padre[x] = self.encontrar(self.padre[x])
        return self.padre[x]
    
    def unir(self, x, y):
        """Une dos conjuntos usando union by rank."""
        raiz_x = self.encontrar(x)
        raiz_y = self.encontrar(y)
        
        if raiz_x == raiz_y:
            return False
        
        if self.rango[raiz_x] < self.rango[raiz_y]:
            self.padre[raiz_x] = raiz_y
        elif self.rango[raiz_x] > self.rango[raiz_y]:
            self.padre[raiz_y] = raiz_x
        else:
            self.padre[raiz_y] = raiz_x
            self.rango[raiz_x] += 1
        
        return True

def kruskal(nodos, aristas):
    """
    Encuentra el Minimum Spanning Tree usando algoritmo de Kruskal.
    Estrategia: Ordenar aristas por peso y agregar las más ligeras que no formen ciclos.
    Complejidad: O(E log E) donde E es el número de aristas
    """
    # Ordenar aristas por peso
    aristas.sort(key=lambda x: x[2])
    
    uf = UnionFind(nodos)
    mst = []
    peso_total = 0
    
    for u, v, peso in aristas:
        if uf.unir(u, v):
            mst.append((u, v, peso))
            peso_total += peso
            if len(mst) == nodos - 1:
                break
    
    return mst, peso_total

# Ejemplo
nodos_kruskal = 4
aristas_kruskal = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

print(f"Grafo con {nodos_kruskal} nodos y {len(aristas_kruskal)} aristas:")
for u, v, peso in aristas_kruskal:
    print(f"  {u} --{peso}-- {v}")

mst, peso_total = kruskal(nodos_kruskal, aristas_kruskal)
print(f"\nMinimum Spanning Tree (peso total: {peso_total}):")
for u, v, peso in mst:
    print(f"  {u} --{peso}-- {v}")
print()

# =============================================================================
# 4. HUFFMAN CODING (Codificación de Huffman - Greedy)
# =============================================================================
print("=== 4. Codificación de Huffman ===")

import heapq

class NodoHuffman:
    """Nodo para el árbol de Huffman."""
    def __init__(self, caracter=None, frecuencia=0, izquierda=None, derecha=None):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = izquierda
        self.derecha = derecha
    
    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia
    
    def es_hoja(self):
        return self.izquierda is None and self.derecha is None

def construir_arbol_huffman(frecuencias):
    """
    Construye el árbol de Huffman usando algoritmo greedy.
    Estrategia: Combinar siempre los dos nodos con menor frecuencia.
    Complejidad: O(n log n) donde n es el número de caracteres únicos
    """
    cola = []
    for caracter, frecuencia in frecuencias.items():
        heapq.heappush(cola, NodoHuffman(caracter, frecuencia))
    
    while len(cola) > 1:
        izquierda = heapq.heappop(cola)
        derecha = heapq.heappop(cola)
        
        nodo_fusion = NodoHuffman(
            frecuencia=izquierda.frecuencia + derecha.frecuencia,
            izquierda=izquierda,
            derecha=derecha
        )
        heapq.heappush(cola, nodo_fusion)
    
    return cola[0] if cola else None

def generar_codigos_huffman(nodo, codigo="", codigos={}):
    """Genera los códigos binarios recorriendo el árbol."""
    if nodo is None:
        return
    
    if nodo.es_hoja():
        codigos[nodo.caracter] = codigo if codigo else "0"
        return
    
    generar_codigos_huffman(nodo.izquierda, codigo + "0", codigos)
    generar_codigos_huffman(nodo.derecha, codigo + "1", codigos)
    
    return codigos

def codificar_huffman(texto):
    """Codifica un texto usando Huffman."""
    # Calcular frecuencias
    frecuencias = {}
    for caracter in texto:
        frecuencias[caracter] = frecuencias.get(caracter, 0) + 1
    
    # Construir árbol
    raiz = construir_arbol_huffman(frecuencias)
    if raiz is None:
        return {}, ""
    
    # Generar códigos
    codigos = generar_codigos_huffman(raiz)
    
    # Codificar texto
    texto_codificado = ''.join(codigos[caracter] for caracter in texto)
    
    return codigos, texto_codificado

# Ejemplo
texto_huffman = "hello world"
print(f"Texto original: '{texto_huffman}'")

codigos, texto_cod = codificar_huffman(texto_huffman)
print("\nCódigos de Huffman:")
for caracter, codigo in sorted(codigos.items()):
    print(f"  '{caracter}': {codigo}")

print(f"\nTexto codificado: {texto_cod}")
print(f"Longitud original: {len(texto_huffman) * 8} bits (ASCII)")
print(f"Longitud codificada: {len(texto_cod)} bits")
print(f"Compresión: {len(texto_cod) / (len(texto_huffman) * 8) * 100:.1f}%")
print()

# =============================================================================
# 5. COIN CHANGE GREEDY (Cambio de Monedas Greedy)
# =============================================================================
print("=== 5. Cambio de Monedas (Algoritmo Greedy) ===")

def cambio_monedas_greedy(monedas, cantidad):
    """
    Encuentra el cambio usando algoritmo greedy.
    IMPORTANTE: Solo funciona para sistemas de monedas "canónicos" (como USD, EUR).
    No funciona para sistemas arbitrarios (ej: monedas [1, 3, 4] y cantidad 6).
    Complejidad: O(n) donde n es el número de tipos de monedas
    """
    # Ordenar monedas en orden descendente
    monedas = sorted(monedas, reverse=True)
    
    cambio = []
    cantidad_restante = cantidad
    
    for moneda in monedas:
        if cantidad_restante >= moneda:
            cantidad_moneda = cantidad_restante // moneda
            cambio.append((moneda, cantidad_moneda))
            cantidad_restante -= cantidad_moneda * moneda
        
        if cantidad_restante == 0:
            break
    
    return cambio, cantidad_restante

# Ejemplo con sistema canónico
monedas_canonicas = [1, 5, 10, 25, 50, 100]  # Sistema como USD
cantidad_cambio = 287

print(f"Monedas disponibles: {monedas_canonicas}")
print(f"Cantidad a cambiar: {cantidad_cambio}")

cambio, resto = cambio_monedas_greedy(monedas_canonicas, cantidad_cambio)
print(f"\nCambio (moneda, cantidad):")
total = 0
for moneda, cantidad in cambio:
    print(f"  {moneda}: {cantidad} moneda(s)")
    total += moneda * cantidad

print(f"Total: {total}")
if resto > 0:
    print(f"Resto no cambiado: {resto}")

# Ejemplo donde greedy falla
print("\n⚠️  Ejemplo donde Greedy NO funciona óptimamente:")
monedas_no_canonicas = [1, 3, 4]
cantidad_falla = 6
cambio_greedy, _ = cambio_monedas_greedy(monedas_no_canonicas, cantidad_falla)
print(f"Monedas: {monedas_no_canonicas}, Cantidad: {cantidad_falla}")
print(f"Greedy da: {sum(m*c for m, c in cambio_greedy)} monedas")
print(f"Óptimo sería: 2 monedas (3+3), pero greedy da: {sum(c for _, c in cambio_greedy)} monedas")
print()

# =============================================================================
# 6. INTERVAL SCHEDULING (Programación de Intervalos)
# =============================================================================
print("=== 6. Programación de Intervalos con Pesos ===")

def interval_scheduling_pesos(intervals):
    """
    Interval Scheduling con pesos (Weighted Interval Scheduling).
    Encuentra el conjunto de intervalos con peso máximo que no se solapan.
    Esta es una versión simplificada - la versión completa usa DP.
    """
    # Ordenar por tiempo de finalización
    intervals.sort(key=lambda x: x[1])
    
    n = len(intervals)
    pesos_acumulados = [0] * n
    seleccionados = []
    
    for i, (inicio, fin, peso) in enumerate(intervals):
        # Buscar el último intervalo que no se solapa con el actual
        mejor_peso = peso
        mejor_indice_anterior = -1
        
        for j in range(i - 1, -1, -1):
            if intervals[j][1] <= inicio:
                if pesos_acumulados[j] + peso > mejor_peso:
                    mejor_peso = pesos_acumulados[j] + peso
                    mejor_indice_anterior = j
                break
        
        pesos_acumulados[i] = mejor_peso
    
    # Reconstruir solución
    i = n - 1
    while i >= 0:
        if i == 0 or pesos_acumulados[i] > pesos_acumulados[i-1]:
            seleccionados.append(i)
            # Buscar siguiente intervalo no solapado
            fin_actual = intervals[i][0]
            i -= 1
            while i >= 0 and intervals[i][1] > fin_actual:
                i -= 1
        else:
            i -= 1
    
    seleccionados.reverse()
    return seleccionados, pesos_acumulados[-1] if pesos_acumulados else 0

# Ejemplo
intervalos_pesos = [
    (1, 4, 3),
    (3, 5, 4),
    (0, 6, 2),
    (5, 7, 1),
    (8, 9, 5),
    (5, 9, 2)
]

print("Intervalos (inicio, fin, peso):")
for i, (ini, fin, peso) in enumerate(intervalos_pesos):
    print(f"  Intervalo {i}: [{ini}, {fin}] peso={peso}")

seleccionados, peso_total = interval_scheduling_pesos(intervalos_pesos)
print(f"\nIntervalos seleccionados: {seleccionados}")
print(f"Peso total: {peso_total}")
for indice in seleccionados:
    ini, fin, peso = intervalos_pesos[indice]
    print(f"  Intervalo {indice}: [{ini}, {fin}] peso={peso}")
print()

# Resumen
print("=== RESUMEN ===")
print("""
Algoritmos Greedy implementados:

1. Mochila Fraccionaria:
   - Estrategia: Tomar items con mayor valor/peso primero
   - Complejidad: O(n log n)
   - Siempre da solución óptima

2. Selección de Actividades:
   - Estrategia: Seleccionar actividades que terminan primero
   - Complejidad: O(n log n)
   - Siempre da solución óptima

3. Algoritmo de Kruskal (MST):
   - Estrategia: Agregar aristas más ligeras que no formen ciclos
   - Complejidad: O(E log E)
   - Siempre da solución óptima

4. Codificación de Huffman:
   - Estrategia: Combinar nodos con menor frecuencia
   - Complejidad: O(n log n)
   - Siempre da solución óptima

5. Cambio de Monedas (Greedy):
   - Estrategia: Usar monedas más grandes primero
   - Complejidad: O(n)
   - Solo funciona para sistemas canónicos

6. Interval Scheduling con Pesos:
   - Versión simplificada (completa requiere DP)
   - Complejidad: O(n²)

Características de Algoritmos Greedy:
- Hacen la elección localmente óptima en cada paso
- No reconsideran decisiones previas
- Eficientes pero no siempre óptimos
- Funcionan bien para problemas con estructura greedy (subestructura óptima)
""")
