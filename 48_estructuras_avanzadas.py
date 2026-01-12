# Archivo: 48_estructuras_avanzadas.py
# Descripción: Estructuras de Datos Avanzadas

print("=== Estructuras de Datos Avanzadas ===\n")

# =============================================================================
# 1. TRIE (ÁRBOL DE PREFIJOS)
# =============================================================================
print("=== 1. Trie (Árbol de Prefijos) ===")

class NodoTrie:
    """Nodo para el árbol Trie."""
    def __init__(self):
        self.hijos = {}  # Diccionario: char -> NodoTrie
        self.es_fin_palabra = False
        self.conteo = 0  # Número de palabras que pasan por este nodo

class Trie:
    """
    Estructura de datos Trie para almacenar y buscar strings eficientemente.
    Complejidad: O(m) donde m es la longitud de la palabra
    """
    def __init__(self):
        self.raiz = NodoTrie()
    
    def insertar(self, palabra):
        """Inserta una palabra en el Trie."""
        nodo_actual = self.raiz
        
        for caracter in palabra:
            if caracter not in nodo_actual.hijos:
                nodo_actual.hijos[caracter] = NodoTrie()
            nodo_actual = nodo_actual.hijos[caracter]
            nodo_actual.conteo += 1
        
        nodo_actual.es_fin_palabra = True
    
    def buscar(self, palabra):
        """Busca una palabra en el Trie. Retorna True si existe."""
        nodo_actual = self.raiz
        
        for caracter in palabra:
            if caracter not in nodo_actual.hijos:
                return False
            nodo_actual = nodo_actual.hijos[caracter]
        
        return nodo_actual.es_fin_palabra
    
    def buscar_prefijo(self, prefijo):
        """Verifica si existe alguna palabra con el prefijo dado."""
        nodo_actual = self.raiz
        
        for caracter in prefijo:
            if caracter not in nodo_actual.hijos:
                return False
            nodo_actual = nodo_actual.hijos[caracter]
        
        return True
    
    def autocompletar(self, prefijo):
        """Encuentra todas las palabras que empiezan con el prefijo."""
        nodo_actual = self.raiz
        
        # Navegar hasta el final del prefijo
        for caracter in prefijo:
            if caracter not in nodo_actual.hijos:
                return []
            nodo_actual = nodo_actual.hijos[caracter]
        
        # Recopilar todas las palabras desde este nodo
        palabras = []
        
        def dfs(nodo, prefijo_actual):
            if nodo.es_fin_palabra:
                palabras.append(prefijo_actual)
            
            for caracter, hijo in nodo.hijos.items():
                dfs(hijo, prefijo_actual + caracter)
        
        dfs(nodo_actual, prefijo)
        return palabras
    
    def eliminar(self, palabra):
        """Elimina una palabra del Trie."""
        def _eliminar(nodo, palabra, indice):
            if indice == len(palabra):
                if not nodo.es_fin_palabra:
                    return False
                nodo.es_fin_palabra = False
                return len(nodo.hijos) == 0
            
            caracter = palabra[indice]
            if caracter not in nodo.hijos:
                return False
            
            debe_eliminar_nodo = _eliminar(nodo.hijos[caracter], palabra, indice + 1)
            
            if debe_eliminar_nodo:
                del nodo.hijos[caracter]
                nodo.conteo -= 1
                return len(nodo.hijos) == 0 and not nodo.es_fin_palabra
            
            return False
        
        _eliminar(self.raiz, palabra, 0)

# Ejemplo
trie = Trie()
palabras = ["apple", "app", "apricot", "banana", "band", "bandana"]

print("Insertando palabras:", palabras)
for palabra in palabras:
    trie.insertar(palabra)

print(f"\n¿'apple' existe? {trie.buscar('apple')}")
print(f"¿'apples' existe? {trie.buscar('apples')}")
print(f"¿Existe prefijo 'app'? {trie.buscar_prefijo('app')}")
print(f"Autocompletar 'ban': {trie.autocompletar('ban')}")
print()

# =============================================================================
# 2. SEGMENT TREE
# =============================================================================
print("=== 2. Segment Tree ===")

class SegmentTree:
    """
    Segment Tree para consultas de rango eficientes.
    Complejidad: O(log n) para consulta y actualización
    """
    def __init__(self, arr, funcion=sum):
        """
        Inicializa el Segment Tree.
        arr: lista de elementos
        funcion: función a aplicar (sum, min, max, etc.)
        """
        self.n = len(arr)
        self.funcion = funcion
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        
        # Árbol representado como array
        self.arbol = [0] * (2 * self.size)
        
        # Construir el árbol
        for i in range(self.n):
            self.arbol[self.size + i] = arr[i]
        
        # Para funciones como min/max, inicializar con valor neutro
        if funcion == min:
            for i in range(self.size + self.n, 2 * self.size):
                self.arbol[i] = float('inf')
        
        # Construir niveles superiores
        for i in range(self.size - 1, 0, -1):
            self.arbol[i] = self._aplicar_funcion(
                self.arbol[2 * i],
                self.arbol[2 * i + 1]
            )
    
    def _aplicar_funcion(self, a, b):
        """Aplica la función a dos valores."""
        if self.funcion == sum:
            return a + b
        elif self.funcion == min:
            return min(a, b)
        elif self.funcion == max:
            return max(a, b)
        else:
            return self.funcion([a, b])
    
    def consultar_rango(self, l, r):
        """
        Consulta el rango [l, r) (l incluido, r excluido).
        """
        l += self.size
        r += self.size
        resultado = 0 if self.funcion == sum else []
        
        if self.funcion == min:
            resultado = float('inf')
        elif self.funcion == max:
            resultado = float('-inf')
        
        while l < r:
            if l % 2 == 1:
                resultado = self._aplicar_funcion(resultado, self.arbol[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                resultado = self._aplicar_funcion(resultado, self.arbol[r])
            l //= 2
            r //= 2
        
        return resultado
    
    def actualizar(self, indice, valor):
        """Actualiza el valor en la posición indice."""
        indice += self.size
        self.arbol[indice] = valor
        
        indice //= 2
        while indice >= 1:
            self.arbol[indice] = self._aplicar_funcion(
                self.arbol[2 * indice],
                self.arbol[2 * indice + 1]
            )
            indice //= 2

# Ejemplo
arr_seg = [1, 3, 5, 7, 9, 11]
print(f"Array: {arr_seg}")

# Segment Tree para suma
seg_tree_sum = SegmentTree(arr_seg, sum)
print(f"Suma [1, 4): {seg_tree_sum.consultar_rango(1, 4)}")
print(f"Suma [0, 6): {seg_tree_sum.consultar_rango(0, 6)}")

# Segment Tree para mínimo
seg_tree_min = SegmentTree(arr_seg, min)
print(f"Mínimo [1, 4): {seg_tree_min.consultar_rango(1, 4)}")

# Actualizar
seg_tree_sum.actualizar(2, 10)
print(f"Después de actualizar índice 2 a 10: {seg_tree_sum.consultar_rango(0, 6)}")
print()

# =============================================================================
# 3. FENWICK TREE (Binary Indexed Tree)
# =============================================================================
print("=== 3. Fenwick Tree (Binary Indexed Tree) ===")

class FenwickTree:
    """
    Fenwick Tree (Binary Indexed Tree) para consultas de suma de prefijos eficientes.
    Complejidad: O(log n) para consulta y actualización
    Más simple y eficiente en memoria que Segment Tree para sumas.
    """
    def __init__(self, arr):
        self.n = len(arr)
        self.arbol = [0] * (self.n + 1)
        
        # Construir el árbol
        for i in range(self.n):
            self.actualizar(i, arr[i])
    
    def _lsb(self, x):
        """Retorna el bit menos significativo."""
        return x & -x
    
    def actualizar(self, indice, delta):
        """Actualiza el valor en indice agregando delta."""
        indice += 1  # Convertir a índice basado en 1
        
        while indice <= self.n:
            self.arbol[indice] += delta
            indice += self._lsb(indice)
    
    def consultar_prefijo(self, indice):
        """Consulta la suma desde 0 hasta indice (inclusive)."""
        indice += 1  # Convertir a índice basado en 1
        suma = 0
        
        while indice > 0:
            suma += self.arbol[indice]
            indice -= self._lsb(indice)
        
        return suma
    
    def consultar_rango(self, l, r):
        """Consulta la suma del rango [l, r] (inclusive)."""
        if l == 0:
            return self.consultar_prefijo(r)
        return self.consultar_prefijo(r) - self.consultar_prefijo(l - 1)

# Ejemplo
arr_fenwick = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Array: {arr_fenwick}")

fenwick = FenwickTree(arr_fenwick)
print(f"Suma prefijo [0, 5]: {fenwick.consultar_prefijo(5)}")
print(f"Suma rango [3, 7]: {fenwick.consultar_rango(3, 7)}")

# Actualizar
fenwick.actualizar(3, 6)  # Agregar 6 al índice 3
print(f"Después de agregar 6 al índice 3:")
print(f"  Nuevo valor en índice 3: {fenwick.consultar_rango(3, 3)}")
print(f"  Suma prefijo [0, 5]: {fenwick.consultar_prefijo(5)}")
print()

# =============================================================================
# 4. UNION-FIND MEJORADO
# =============================================================================
print("=== 4. Union-Find Mejorado ===")

class UnionFind:
    """
    Union-Find mejorado con path compression y union by rank.
    Complejidad: O(α(n)) donde α es la función de Ackermann inversa (casi constante).
    """
    def __init__(self, n):
        self.padre = list(range(n))
        self.rango = [0] * n
        self.tamaño = [1] * n  # Tamaño de cada componente
        self.num_componentes = n
    
    def encontrar(self, x):
        """Encuentra la raíz con path compression."""
        if self.padre[x] != x:
            self.padre[x] = self.encontrar(self.padre[x])  # Path compression
        return self.padre[x]
    
    def unir(self, x, y):
        """Une dos conjuntos usando union by rank."""
        raiz_x = self.encontrar(x)
        raiz_y = self.encontrar(y)
        
        if raiz_x == raiz_y:
            return False  # Ya están en el mismo conjunto
        
        # Union by rank
        if self.rango[raiz_x] < self.rango[raiz_y]:
            raiz_x, raiz_y = raiz_y, raiz_x
        
        self.padre[raiz_y] = raiz_x
        self.tamaño[raiz_x] += self.tamaño[raiz_y]
        
        if self.rango[raiz_x] == self.rango[raiz_y]:
            self.rango[raiz_x] += 1
        
        self.num_componentes -= 1
        return True
    
    def mismo_conjunto(self, x, y):
        """Verifica si x y y están en el mismo conjunto."""
        return self.encontrar(x) == self.encontrar(y)
    
    def tamaño_componente(self, x):
        """Retorna el tamaño de la componente que contiene x."""
        return self.tamaño[self.encontrar(x)]
    
    def obtener_componentes(self):
        """Retorna un diccionario de componentes."""
        componentes = {}
        for i in range(len(self.padre)):
            raiz = self.encontrar(i)
            if raiz not in componentes:
                componentes[raiz] = []
            componentes[raiz].append(i)
        return componentes

# Ejemplo
uf = UnionFind(10)
print("Uniendo elementos:")
uniones = [(0, 1), (2, 3), (4, 5), (6, 7), (0, 2), (4, 6), (1, 3)]

for x, y in uniones:
    uf.unir(x, y)
    print(f"  Unir {x} y {y}: Componentes = {uf.num_componentes}")

print(f"\nNúmero de componentes: {uf.num_componentes}")
print(f"¿0 y 3 en mismo conjunto? {uf.mismo_conjunto(0, 3)}")
print(f"Tamaño de componente de 0: {uf.tamaño_componente(0)}")
print(f"Componentes: {uf.obtener_componentes()}")
print()

# Resumen
print("=== RESUMEN ===")
print("""
Estructuras de datos avanzadas implementadas:

1. Trie (Árbol de Prefijos):
   - Almacenamiento eficiente de strings
   - Búsqueda: O(m) donde m = longitud palabra
   - Aplicaciones: Autocompletado, diccionarios, spell checkers

2. Segment Tree:
   - Consultas de rango eficientes
   - Consulta: O(log n)
   - Actualización: O(log n)
   - Aplicaciones: Suma/mín/máx en rangos, problemas de rango

3. Fenwick Tree (Binary Indexed Tree):
   - Sumas de prefijos eficientes
   - Más simple que Segment Tree
   - Consulta: O(log n)
   - Actualización: O(log n)
   - Aplicaciones: Sumas acumulativas, inversiones

4. Union-Find Mejorado:
   - Path compression + Union by rank
   - Casi constante: O(α(n))
   - Aplicaciones: Detección de ciclos, Kruskal, componentes conexas

Complejidades:
- Trie: O(m) búsqueda, O(m) inserción
- Segment Tree: O(log n) consulta/actualización, O(n) espacio
- Fenwick Tree: O(log n) consulta/actualización, O(n) espacio
- Union-Find: O(α(n)) ≈ O(1) prácticamente
""")
