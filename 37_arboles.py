# Archivo: 37_arboles.py
# Descripción: Estructuras de datos - Árboles

from collections import deque

print("=== Estructuras de Datos: Árboles ===\n")

# =============================================================================
# 1. ÁRBOL BINARIO BÁSICO
# =============================================================================
print("=== 1. Árbol Binario Básico ===")

class NodoArbol:
    """Nodo de un árbol binario."""
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
    
    def __str__(self):
        return str(self.valor)

class ArbolBinario:
    """Árbol binario simple."""
    
    def __init__(self, valor_raiz=None):
        if valor_raiz is not None:
            self.raiz = NodoArbol(valor_raiz)
        else:
            self.raiz = None
    
    def insertar(self, valor):
        """Inserta un valor en el árbol."""
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo, valor):
        """Inserta recursivamente en el árbol."""
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)
    
    def buscar(self, valor):
        """Busca un valor en el árbol."""
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, nodo, valor):
        """Busca recursivamente en el árbol."""
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        return self._buscar_recursivo(nodo.derecha, valor)
    
    def altura(self):
        """Calcula la altura del árbol."""
        return self._altura_recursiva(self.raiz)
    
    def _altura_recursiva(self, nodo):
        """Calcula la altura recursivamente."""
        if nodo is None:
            return -1
        return 1 + max(self._altura_recursiva(nodo.izquierda), 
                      self._altura_recursiva(nodo.derecha))
    
    def tamaño(self):
        """Calcula el número de nodos."""
        return self._tamaño_recursivo(self.raiz)
    
    def _tamaño_recursivo(self, nodo):
        """Calcula el tamaño recursivamente."""
        if nodo is None:
            return 0
        return 1 + self._tamaño_recursivo(nodo.izquierda) + \
               self._tamaño_recursivo(nodo.derecha)

# Ejemplo
print("Creando árbol binario:")
arbol = ArbolBinario()
valores = [50, 30, 70, 20, 40, 60, 80]
for valor in valores:
    arbol.insertar(valor)

print(f"Valores insertados: {valores}")
print(f"Buscar 40: {arbol.buscar(40)}")
print(f"Buscar 100: {arbol.buscar(100)}")
print(f"Altura del árbol: {arbol.altura()}")
print(f"Tamaño del árbol: {arbol.tamaño()}")
print()

# =============================================================================
# 2. RECORRIDOS DE ÁRBOL
# =============================================================================
print("=== 2. Recorridos de Árbol ===")

class ArbolRecorridos(ArbolBinario):
    """Árbol binario con métodos de recorrido."""
    
    def recorrido_preorden(self):
        """Recorrido preorden: raíz, izquierda, derecha."""
        resultado = []
        self._preorden(self.raiz, resultado)
        return resultado
    
    def _preorden(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            self._preorden(nodo.izquierda, resultado)
            self._preorden(nodo.derecha, resultado)
    
    def recorrido_inorden(self):
        """Recorrido inorden: izquierda, raíz, derecha."""
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado
    
    def _inorden(self, nodo, resultado):
        if nodo:
            self._inorden(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._inorden(nodo.derecha, resultado)
    
    def recorrido_postorden(self):
        """Recorrido postorden: izquierda, derecha, raíz."""
        resultado = []
        self._postorden(self.raiz, resultado)
        return resultado
    
    def _postorden(self, nodo, resultado):
        if nodo:
            self._postorden(nodo.izquierda, resultado)
            self._postorden(nodo.derecha, resultado)
            resultado.append(nodo.valor)
    
    def recorrido_nivel_orden(self):
        """Recorrido por niveles (BFS - Breadth First Search)."""
        if self.raiz is None:
            return []
        
        resultado = []
        cola = deque([self.raiz])
        
        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.valor)
            
            if nodo.izquierda:
                cola.append(nodo.izquierda)
            if nodo.derecha:
                cola.append(nodo.derecha)
        
        return resultado

# Ejemplo
print("Creando árbol para recorridos:")
arbol_rec = ArbolRecorridos()
valores = [50, 30, 70, 20, 40, 60, 80]
for valor in valores:
    arbol_rec.insertar(valor)

print(f"Preorden (raíz, izq, der):   {arbol_rec.recorrido_preorden()}")
print(f"Inorden (izq, raíz, der):    {arbol_rec.recorrido_inorden()}")
print(f"Postorden (izq, der, raíz):  {arbol_rec.recorrido_postorden()}")
print(f"Nivel orden (BFS):           {arbol_rec.recorrido_nivel_orden()}")
print()

# =============================================================================
# 3. ÁRBOL BINARIO DE BÚSQUEDA (BST)
# =============================================================================
print("=== 3. Árbol Binario de Búsqueda (BST) ===")

class ArbolBST(ArbolRecorridos):
    """Árbol Binario de Búsqueda completo."""
    
    def es_bst(self):
        """Verifica si el árbol es un BST válido."""
        return self._es_bst_recursivo(self.raiz, float('-inf'), float('inf'))
    
    def _es_bst_recursivo(self, nodo, minimo, maximo):
        """Verifica recursivamente si es BST."""
        if nodo is None:
            return True
        if nodo.valor <= minimo or nodo.valor >= maximo:
            return False
        return (self._es_bst_recursivo(nodo.izquierda, minimo, nodo.valor) and
                self._es_bst_recursivo(nodo.derecha, nodo.valor, maximo))
    
    def encontrar_minimo(self):
        """Encuentra el valor mínimo en el árbol."""
        if self.raiz is None:
            return None
        return self._encontrar_minimo_recursivo(self.raiz)
    
    def _encontrar_minimo_recursivo(self, nodo):
        """Encuentra el mínimo recursivamente."""
        if nodo.izquierda is None:
            return nodo.valor
        return self._encontrar_minimo_recursivo(nodo.izquierda)
    
    def encontrar_maximo(self):
        """Encuentra el valor máximo en el árbol."""
        if self.raiz is None:
            return None
        return self._encontrar_maximo_recursivo(self.raiz)
    
    def _encontrar_maximo_recursivo(self, nodo):
        """Encuentra el máximo recursivamente."""
        if nodo.derecha is None:
            return nodo.valor
        return self._encontrar_maximo_recursivo(nodo.derecha)

# Ejemplo
print("Árbol Binario de Búsqueda:")
arbol_bst = ArbolBST()
valores = [50, 30, 70, 20, 40, 60, 80]
for valor in valores:
    arbol_bst.insertar(valor)

print(f"¿Es BST válido? {arbol_bst.es_bst()}")
print(f"Valor mínimo: {arbol_bst.encontrar_minimo()}")
print(f"Valor máximo: {arbol_bst.encontrar_maximo()}")
print()

# =============================================================================
# 4. ÁRBOL AVL (ÁRBOL BALANCEADO)
# =============================================================================
print("=== 4. Árbol AVL (Auto-balanceado) ===")

class NodoAVL:
    """Nodo para árbol AVL."""
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class ArbolAVL:
    """Árbol AVL (balanceado)."""
    
    def __init__(self):
        self.raiz = None
    
    def obtener_altura(self, nodo):
        """Obtiene la altura de un nodo."""
        if nodo is None:
            return 0
        return nodo.altura
    
    def obtener_factor_balance(self, nodo):
        """Calcula el factor de balance."""
        if nodo is None:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)
    
    def rotar_derecha(self, y):
        """Rotación a la derecha."""
        x = y.izquierda
        T2 = x.derecha
        
        x.derecha = y
        y.izquierda = T2
        
        y.altura = 1 + max(self.obtener_altura(y.izquierda),
                          self.obtener_altura(y.derecha))
        x.altura = 1 + max(self.obtener_altura(x.izquierda),
                          self.obtener_altura(x.derecha))
        
        return x
    
    def rotar_izquierda(self, x):
        """Rotación a la izquierda."""
        y = x.derecha
        T2 = y.izquierda
        
        y.izquierda = x
        x.derecha = T2
        
        x.altura = 1 + max(self.obtener_altura(x.izquierda),
                          self.obtener_altura(x.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda),
                          self.obtener_altura(y.derecha))
        
        return y
    
    def insertar(self, valor):
        """Inserta un valor manteniendo el balance."""
        self.raiz = self._insertar_avl(self.raiz, valor)
    
    def _insertar_avl(self, nodo, valor):
        """Inserta y balancea el árbol."""
        if nodo is None:
            return NodoAVL(valor)
        
        if valor < nodo.valor:
            nodo.izquierda = self._insertar_avl(nodo.izquierda, valor)
        else:
            nodo.derecha = self._insertar_avl(nodo.derecha, valor)
        
        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda),
                             self.obtener_altura(nodo.derecha))
        
        balance = self.obtener_factor_balance(nodo)
        
        # Rotación izquierda-izquierda
        if balance > 1 and valor < nodo.izquierda.valor:
            return self.rotar_derecha(nodo)
        
        # Rotación derecha-derecha
        if balance < -1 and valor > nodo.derecha.valor:
            return self.rotar_izquierda(nodo)
        
        # Rotación izquierda-derecha
        if balance > 1 and valor > nodo.izquierda.valor:
            nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
            return self.rotar_derecha(nodo)
        
        # Rotación derecha-izquierda
        if balance < -1 and valor < nodo.derecha.valor:
            nodo.derecha = self.rotar_derecha(nodo.derecha)
            return self.rotar_izquierda(nodo)
        
        return nodo
    
    def inorden(self):
        """Recorrido inorden."""
        resultado = []
        self._inorden_rec(self.raiz, resultado)
        return resultado
    
    def _inorden_rec(self, nodo, resultado):
        if nodo:
            self._inorden_rec(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._inorden_rec(nodo.derecha, resultado)

# Ejemplo (simplificado)
print("Árbol AVL (implementación básica):")
print("Nota: Árbol AVL mantiene balance automáticamente")
print("      Evita árboles degenerados (que se convierten en listas)")
print()

# =============================================================================
# 5. ÁRBOL N-ARIO (ÁRBOL GENERAL)
# =============================================================================
print("=== 5. Árbol N-ario (Árbol General) ===")

class NodoNario:
    """Nodo de un árbol n-ario (múltiples hijos)."""
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []
    
    def agregar_hijo(self, hijo):
        """Agrega un hijo al nodo."""
        self.hijos.append(hijo)
    
    def __str__(self):
        return str(self.valor)

class ArbolNario:
    """Árbol n-ario (árbol general)."""
    
    def __init__(self, valor_raiz=None):
        if valor_raiz is not None:
            self.raiz = NodoNario(valor_raiz)
        else:
            self.raiz = None
    
    def recorrido_profundidad(self):
        """Recorrido en profundidad (DFS)."""
        if self.raiz is None:
            return []
        
        resultado = []
        self._dfs(self.raiz, resultado)
        return resultado
    
    def _dfs(self, nodo, resultado):
        """Recorrido en profundidad recursivo."""
        resultado.append(nodo.valor)
        for hijo in nodo.hijos:
            self._dfs(hijo, resultado)
    
    def recorrido_anchura(self):
        """Recorrido en anchura (BFS)."""
        if self.raiz is None:
            return []
        
        resultado = []
        cola = deque([self.raiz])
        
        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.valor)
            cola.extend(nodo.hijos)
        
        return resultado

# Ejemplo
print("Creando árbol n-ario:")
arbol_nario = ArbolNario(1)
nodo2 = NodoNario(2)
nodo3 = NodoNario(3)
nodo4 = NodoNario(4)
nodo5 = NodoNario(5)
nodo6 = NodoNario(6)

arbol_nario.raiz.agregar_hijo(nodo2)
arbol_nario.raiz.agregar_hijo(nodo3)
nodo2.agregar_hijo(nodo4)
nodo2.agregar_hijo(nodo5)
nodo3.agregar_hijo(nodo6)

print("Estructura: 1 -> [2, 3], 2 -> [4, 5], 3 -> [6]")
print(f"Recorrido en profundidad (DFS): {arbol_nario.recorrido_profundidad()}")
print(f"Recorrido en anchura (BFS): {arbol_nario.recorrido_anchura()}")
print()

# =============================================================================
# 6. OPERACIONES COMUNES EN ÁRBOLES
# =============================================================================
print("=== 6. Operaciones Comunes ===")

def contar_hojas(arbol):
    """Cuenta el número de hojas en un árbol binario."""
    def _contar_hojas(nodo):
        if nodo is None:
            return 0
        if nodo.izquierda is None and nodo.derecha is None:
            return 1
        return _contar_hojas(nodo.izquierda) + _contar_hojas(nodo.derecha)
    
    return _contar_hojas(arbol.raiz)

def sumar_valores(arbol):
    """Suma todos los valores del árbol."""
    def _sumar(nodo):
        if nodo is None:
            return 0
        return nodo.valor + _sumar(nodo.izquierda) + _sumar(nodo.derecha)
    
    return _sumar(arbol.raiz)

def es_completo(arbol):
    """Verifica si el árbol binario está completo."""
    def _es_completo(nodo, indice, num_nodos):
        if nodo is None:
            return True
        if indice >= num_nodos:
            return False
        return (_es_completo(nodo.izquierda, 2*indice + 1, num_nodos) and
                _es_completo(nodo.derecha, 2*indice + 2, num_nodos))
    
    num_nodos = arbol.tamaño()
    return _es_completo(arbol.raiz, 0, num_nodos)

# Ejemplo
print("Operaciones comunes:")
arbol_ops = ArbolBST()
valores = [50, 30, 70, 20, 40, 60, 80]
for valor in valores:
    arbol_ops.insertar(valor)

print(f"Número de hojas: {contar_hojas(arbol_ops)}")
print(f"Suma de valores: {sumar_valores(arbol_ops)}")
print(f"Altura: {arbol_ops.altura()}")
print(f"Tamaño: {arbol_ops.tamaño()}")
print()

# =============================================================================
# 7. COMPARACIÓN Y RESUMEN
# =============================================================================
print("=== 7. Resumen de Tipos de Árboles ===")
print("""
Tipos de Árboles:

1. ÁRBOL BINARIO:
   - Cada nodo tiene máximo 2 hijos
   - Operaciones: O(n) en el peor caso
   - Uso: Estructura básica

2. ÁRBOL BINARIO DE BÚSQUEDA (BST):
   - Árbol binario con propiedad de orden
   - Izquierda < Raíz < Derecha
   - Búsqueda: O(log n) promedio, O(n) peor caso
   - Uso: Búsqueda eficiente

3. ÁRBOL AVL:
   - BST auto-balanceado
   - Altura de subárboles difiere máximo en 1
   - Operaciones: O(log n) garantizado
   - Uso: Cuando se necesita garantía de rendimiento

4. ÁRBOL N-ARIO:
   - Cada nodo puede tener múltiples hijos
   - Uso: Representar jerarquías (archivos, organizaciones)

Recorridos:
- Preorden: Raíz -> Izquierda -> Derecha
- Inorden: Izquierda -> Raíz -> Derecha (ordena en BST)
- Postorden: Izquierda -> Derecha -> Raíz
- Por niveles (BFS): Nivel por nivel

Aplicaciones:
- Búsqueda y ordenamiento
- Expresiones matemáticas
- Estructuras de archivos
- Bases de datos (índices)
- Compresión (Huffman)
""")
