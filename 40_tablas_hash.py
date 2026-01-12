# Archivo: 40_tablas_hash.py
# Descripción: Estructuras de datos - Tablas Hash (Hash Tables)

print("=== Estructuras de Datos: Tablas Hash ===\n")

# =============================================================================
# 1. TABLA HASH BÁSICA (Hash Table)
# =============================================================================
print("=== 1. Tabla Hash Básica ===")

class TablaHash:
    """Implementación básica de una tabla hash usando listas (chaining)."""
    
    def __init__(self, capacidad=16):
        """Inicializa la tabla hash con una capacidad predeterminada."""
        self.capacidad = capacidad
        self.tabla = [[] for _ in range(capacidad)]
        self.tamaño = 0
    
    def _hash(self, clave):
        """
        Función hash: convierte una clave en un índice.
        Usa hash() de Python y módulo para obtener índice válido.
        """
        return hash(clave) % self.capacidad
    
    def insertar(self, clave, valor):
        """Inserta un par clave-valor en la tabla hash."""
        indice = self._hash(clave)
        bucket = self.tabla[indice]
        
        # Buscar si la clave ya existe
        for i, (k, v) in enumerate(bucket):
            if k == clave:
                bucket[i] = (clave, valor)  # Actualizar valor existente
                return
        
        # Si no existe, agregar nuevo
        bucket.append((clave, valor))
        self.tamaño += 1
        
        # Redimensionar si la carga es alta (factor de carga > 0.75)
        if self.tamaño > self.capacidad * 0.75:
            self._redimensionar()
    
    def obtener(self, clave, valor_por_defecto=None):
        """Obtiene el valor asociado a una clave."""
        indice = self._hash(clave)
        bucket = self.tabla[indice]
        
        for k, v in bucket:
            if k == clave:
                return v
        
        return valor_por_defecto
    
    def eliminar(self, clave):
        """Elimina un par clave-valor de la tabla hash."""
        indice = self._hash(clave)
        bucket = self.tabla[indice]
        
        for i, (k, v) in enumerate(bucket):
            if k == clave:
                bucket.pop(i)
                self.tamaño -= 1
                return True
        
        return False
    
    def existe(self, clave):
        """Verifica si una clave existe en la tabla hash."""
        indice = self._hash(clave)
        bucket = self.tabla[indice]
        
        for k, v in bucket:
            if k == clave:
                return True
        
        return False
    
    def _redimensionar(self):
        """Redimensiona la tabla hash cuando está demasiado cargada."""
        vieja_tabla = self.tabla
        self.capacidad *= 2
        self.tabla = [[] for _ in range(self.capacidad)]
        self.tamaño = 0
        
        # Reinsertar todos los elementos
        for bucket in vieja_tabla:
            for clave, valor in bucket:
                self.insertar(clave, valor)
    
    def obtener_todos(self):
        """Obtiene todos los pares clave-valor."""
        elementos = []
        for bucket in self.tabla:
            elementos.extend(bucket)
        return elementos
    
    def mostrar(self):
        """Muestra el contenido de la tabla hash."""
        print(f"Tabla Hash (capacidad: {self.capacidad}, tamaño: {self.tamaño}):")
        for i, bucket in enumerate(self.tabla):
            if bucket:
                print(f"  [{i}]: {bucket}")

# Ejemplo
print("Creando tabla hash:")
hash_table = TablaHash(capacidad=8)

# Insertar elementos
hash_table.insertar("nombre", "Juan")
hash_table.insertar("edad", 25)
hash_table.insertar("ciudad", "Bogotá")
hash_table.insertar("profesion", "Ingeniero")

hash_table.mostrar()
print(f"\nObtener 'edad': {hash_table.obtener('edad')}")
print(f"Existe 'ciudad': {hash_table.existe('ciudad')}")
print(f"Existe 'pais': {hash_table.existe('pais')}")

# Eliminar
hash_table.eliminar("profesion")
print(f"\nDespués de eliminar 'profesion':")
hash_table.mostrar()
print()

# =============================================================================
# 2. FUNCIONES HASH PERSONALIZADAS
# =============================================================================
print("=== 2. Funciones Hash Personalizadas ===")

def hash_simple(clave, capacidad):
    """Función hash simple para strings (suma de códigos ASCII)."""
    suma = sum(ord(c) for c in str(clave))
    return suma % capacidad

def hash_djb2(clave, capacidad):
    """
    Función hash DJB2 (popular para strings).
    Mejor distribución que hash_simple.
    """
    hash_val = 5381
    for c in str(clave):
        hash_val = ((hash_val << 5) + hash_val) + ord(c)
    return abs(hash_val) % capacidad

def hash_division(clave, capacidad):
    """Función hash por división (módulo)."""
    return hash(clave) % capacidad

# Ejemplo
claves = ["apple", "banana", "cherry", "date", "elderberry"]
capacidad = 10

print(f"Claves: {claves}")
print("\nDistribución con diferentes funciones hash:")
print("  Índice | Hash Simple | Hash DJB2 | Hash División")
print("  " + "-" * 50)

for clave in claves:
    idx1 = hash_simple(clave, capacidad)
    idx2 = hash_djb2(clave, capacidad)
    idx3 = hash_division(clave, capacidad)
    print(f"  {clave:10s} | {idx1:11d} | {idx2:9d} | {idx3:14d}")

print()

# =============================================================================
# 3. MANEJO DE COLISIONES
# =============================================================================
print("=== 3. Manejo de Colisiones ===")

class TablaHashOpenAddressing:
    """
    Tabla hash con direccionamiento abierto (open addressing).
    Usa linear probing para manejar colisiones.
    """
    
    def __init__(self, capacidad=16):
        self.capacidad = capacidad
        self.tabla = [None] * capacidad
        self.tamaño = 0
        self.DELETED = object()  # Marcador para elementos eliminados
    
    def _hash(self, clave):
        """Función hash principal."""
        return hash(clave) % self.capacidad
    
    def _hash2(self, clave):
        """Función hash secundaria (para double hashing)."""
        return 7 - (hash(clave) % 7)
    
    def insertar(self, clave, valor):
        """Inserta usando linear probing."""
        if self.tamaño >= self.capacidad * 0.75:
            self._redimensionar()
        
        indice = self._hash(clave)
        
        # Linear probing
        while self.tabla[indice] is not None and self.tabla[indice] is not self.DELETED:
            if self.tabla[indice][0] == clave:
                self.tabla[indice] = (clave, valor)  # Actualizar
                return
            indice = (indice + 1) % self.capacidad
        
        self.tabla[indice] = (clave, valor)
        self.tamaño += 1
    
    def obtener(self, clave):
        """Obtiene un valor usando linear probing."""
        indice = self._hash(clave)
        intentos = 0
        
        while self.tabla[indice] is not None and intentos < self.capacidad:
            if self.tabla[indice] is not self.DELETED and self.tabla[indice][0] == clave:
                return self.tabla[indice][1]
            indice = (indice + 1) % self.capacidad
            intentos += 1
        
        return None
    
    def eliminar(self, clave):
        """Elimina usando marcador DELETED."""
        indice = self._hash(clave)
        intentos = 0
        
        while self.tabla[indice] is not None and intentos < self.capacidad:
            if self.tabla[indice] is not self.DELETED and self.tabla[indice][0] == clave:
                self.tabla[indice] = self.DELETED
                self.tamaño -= 1
                return True
            indice = (indice + 1) % self.capacidad
            intentos += 1
        
        return False
    
    def _redimensionar(self):
        """Redimensiona la tabla."""
        vieja_tabla = self.tabla
        self.capacidad *= 2
        self.tabla = [None] * self.capacidad
        self.tamaño = 0
        
        for elemento in vieja_tabla:
            if elemento is not None and elemento is not self.DELETED:
                self.insertar(elemento[0], elemento[1])
    
    def mostrar(self):
        """Muestra el contenido de la tabla."""
        print(f"Tabla Hash Open Addressing (capacidad: {self.capacidad}, tamaño: {self.tamaño}):")
        for i, elemento in enumerate(self.tabla):
            if elemento is not None:
                if elemento is self.DELETED:
                    print(f"  [{i}]: DELETED")
                else:
                    print(f"  [{i}]: {elemento}")

# Ejemplo
print("Tabla Hash con Open Addressing (Linear Probing):")
hash_open = TablaHashOpenAddressing(capacidad=8)

hash_open.insertar("a", 1)
hash_open.insertar("b", 2)
hash_open.insertar("c", 3)
hash_open.insertar("d", 4)

hash_open.mostrar()
print(f"\nObtener 'b': {hash_open.obtener('b')}")

hash_open.eliminar("b")
print(f"\nDespués de eliminar 'b':")
hash_open.mostrar()
print()

# =============================================================================
# 4. APLICACIONES PRÁCTICAS
# =============================================================================
print("=== 4. Aplicaciones Prácticas ===")

def contar_frecuencias(lista):
    """Cuenta la frecuencia de elementos usando tabla hash."""
    frecuencias = TablaHash()
    
    for elemento in lista:
        frecuencia_actual = frecuencias.obtener(elemento, 0)
        frecuencias.insertar(elemento, frecuencia_actual + 1)
    
    return frecuencias

# Ejemplo: contar palabras
texto = "el gato come pescado el gato duerme el perro juega"
palabras = texto.split()
frecuencias = contar_frecuencias(palabras)

print(f"Texto: '{texto}'")
print("\nFrecuencias de palabras:")
for palabra, frecuencia in frecuencias.obtener_todos():
    print(f"  '{palabra}': {frecuencia}")

print()

def encontrar_duplicados(lista):
    """Encuentra elementos duplicados usando tabla hash."""
    visto = TablaHash()
    duplicados = []
    
    for elemento in lista:
        if visto.existe(elemento):
            if elemento not in duplicados:
                duplicados.append(elemento)
        else:
            visto.insertar(elemento, True)
    
    return duplicados

# Ejemplo
lista_numeros = [1, 2, 3, 2, 4, 3, 5, 6, 5, 5]
print(f"Lista: {lista_numeros}")
print(f"Elementos duplicados: {encontrar_duplicados(lista_numeros)}")
print()

def dos_sumas(lista, objetivo):
    """
    Encuentra dos números que sumen el objetivo.
    Usa tabla hash para eficiencia O(n).
    """
    visto = TablaHash()
    
    for i, num in enumerate(lista):
        complemento = objetivo - num
        if visto.existe(complemento):
            return (visto.obtener(complemento), i)
        visto.insertar(num, i)
    
    return None

# Ejemplo
lista_suma = [2, 7, 11, 15]
objetivo = 9
print(f"Lista: {lista_suma}, Objetivo: {objetivo}")
resultado = dos_sumas(lista_suma, objetivo)
if resultado:
    print(f"Índices que suman {objetivo}: {resultado} ({lista_suma[resultado[0]]} + {lista_suma[resultado[1]]})")
else:
    print("No se encontraron dos números que sumen el objetivo")
print()

# =============================================================================
# 5. COMPARACIÓN CON DICCIONARIO DE PYTHON
# =============================================================================
print("=== 5. Comparación con dict() de Python ===")

import time

def comparar_operaciones(cantidad=10000):
    """Compara nuestra implementación con dict() de Python."""
    print(f"\nComparación con {cantidad} operaciones:")
    
    # Nuestra implementación
    mi_hash = TablaHash(capacidad=100)
    inicio = time.time()
    for i in range(cantidad):
        mi_hash.insertar(f"clave_{i}", i)
    tiempo_insertar_mio = time.time() - inicio
    
    inicio = time.time()
    for i in range(cantidad):
        mi_hash.obtener(f"clave_{i}")
    tiempo_obtener_mio = time.time() - inicio
    
    # dict() de Python
    py_dict = {}
    inicio = time.time()
    for i in range(cantidad):
        py_dict[f"clave_{i}"] = i
    tiempo_insertar_py = time.time() - inicio
    
    inicio = time.time()
    for i in range(cantidad):
        _ = py_dict[f"clave_{i}"]
    tiempo_obtener_py = time.time() - inicio
    
    print(f"  Insertar:")
    print(f"    Nuestra: {tiempo_insertar_mio*1000:.2f} ms")
    print(f"    Python dict: {tiempo_insertar_py*1000:.2f} ms")
    print(f"    Ratio: {tiempo_insertar_mio/tiempo_insertar_py:.2f}x")
    
    print(f"  Obtener:")
    print(f"    Nuestra: {tiempo_obtener_mio*1000:.2f} ms")
    print(f"    Python dict: {tiempo_obtener_py*1000:.2f} ms")
    print(f"    Ratio: {tiempo_obtener_mio/tiempo_obtener_py:.2f}x")
    
    print("\n  Nota: dict() de Python está optimizado en C y es mucho más rápido.")
    print("  Nuestra implementación es para fines educativos.")

comparar_operaciones(1000)

print()

# Resumen
print("=== RESUMEN ===")
print("""
Tablas Hash implementadas:

1. Tabla Hash con Chaining (listas enlazadas):
   - Cada bucket es una lista
   - Maneja colisiones agregando elementos a la lista
   - Redimensiona automáticamente cuando está cargada

2. Tabla Hash con Open Addressing (Linear Probing):
   - Los elementos se almacenan directamente en la tabla
   - Las colisiones se resuelven buscando el siguiente espacio disponible
   - Usa marcador DELETED para elementos eliminados

3. Funciones Hash:
   - Hash simple: suma de códigos ASCII
   - Hash DJB2: algoritmo popular para strings
   - Hash por división: módulo (usado por defecto)

4. Aplicaciones:
   - Conteo de frecuencias
   - Detección de duplicados
   - Búsqueda eficiente (O(1) promedio)
   - Problemas como "dos sumas"

Complejidad:
- Insertar: O(1) promedio, O(n) peor caso
- Obtener: O(1) promedio, O(n) peor caso
- Eliminar: O(1) promedio, O(n) peor caso

Nota: En Python, usar dict() para aplicaciones reales.
Esta implementación es para entender cómo funcionan las tablas hash.
""")
