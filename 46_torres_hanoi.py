# Archivo: 46_torres_hanoi.py
# Descripción: Torres de Hanoi

import time
from typing import List, Tuple

print("=== Torres de Hanoi ===\n")

# =============================================================================
# 1. TORRES DE HANOI - SOLUCIÓN RECURSIVA
# =============================================================================
print("=== 1. Torres de Hanoi (Recursivo) ===")

class TorresHanoi:
    """Clase para representar y resolver el problema de las Torres de Hanoi."""
    
    def __init__(self, num_discos):
        """Inicializa las torres con num_discos discos en la primera torre."""
        self.num_discos = num_discos
        self.torres = {
            'A': list(range(num_discos, 0, -1)),  # Discos más grandes primero
            'B': [],
            'C': []
        }
        self.movimientos = []
        self.contador_movimientos = 0
    
    def mostrar_torres(self):
        """Muestra el estado actual de las torres."""
        print("\nEstado de las torres:")
        for torre in ['A', 'B', 'C']:
            discos = self.torres[torre].copy()
            discos.reverse()  # Mostrar con el más grande abajo
            representacion = '|' + ' '.join(str(d) for d in discos) if discos else '|'
            print(f"Torre {torre}: {representacion}")
    
    def mover_disco(self, origen, destino):
        """Mueve un disco de una torre a otra."""
        if not self.torres[origen]:
            raise ValueError(f"La torre {origen} está vacía")
        
        disco = self.torres[origen][-1]
        
        # Validar movimiento (disco más grande no puede ir sobre uno más pequeño)
        if self.torres[destino] and self.torres[destino][-1] < disco:
            raise ValueError(f"No se puede colocar el disco {disco} sobre el disco {self.torres[destino][-1]}")
        
        self.torres[origen].pop()
        self.torres[destino].append(disco)
        self.movimientos.append((origen, destino, disco))
        self.contador_movimientos += 1
    
    def resolver_recursivo(self, n=None, origen='A', destino='C', auxiliar='B', mostrar=True):
        """
        Resuelve el problema de las Torres de Hanoi usando recursión.
        
        Algoritmo:
        1. Mover n-1 discos de origen a auxiliar
        2. Mover el disco más grande de origen a destino
        3. Mover n-1 discos de auxiliar a destino
        
        Complejidad: O(2^n) - se requieren 2^n - 1 movimientos
        """
        if n is None:
            n = self.num_discos
        
        if n == 0:
            return
        
        if n == 1:
            # Caso base: mover un solo disco
            self.mover_disco(origen, destino)
            if mostrar:
                print(f"Movimiento {self.contador_movimientos}: Mover disco {self.torres[destino][-1]} de {origen} a {destino}")
            return
        
        # Paso 1: Mover n-1 discos a la torre auxiliar
        self.resolver_recursivo(n-1, origen, auxiliar, destino, mostrar)
        
        # Paso 2: Mover el disco más grande a destino
        self.mover_disco(origen, destino)
        if mostrar:
            print(f"Movimiento {self.contador_movimientos}: Mover disco {self.torres[destino][-1]} de {origen} a {destino}")
        
        # Paso 3: Mover n-1 discos de auxiliar a destino
        self.resolver_recursivo(n-1, auxiliar, destino, origen, mostrar)
    
    def resolver_iterativo(self, mostrar=True):
        """
        Resuelve el problema de las Torres de Hanoi usando iteración.
        Implementa el algoritmo usando un enfoque basado en la paridad.
        """
        # El número mínimo de movimientos es 2^n - 1
        total_movimientos = (1 << self.num_discos) - 1  # 2^n - 1
        
        # Si n es par, intercambiar destino y auxiliar
        origen, destino, auxiliar = 'A', 'C', 'B'
        if self.num_discos % 2 == 0:
            destino, auxiliar = auxiliar, destino
        
        for movimiento in range(1, total_movimientos + 1):
            if movimiento % 3 == 1:
                # Mover entre origen y destino
                if not self.torres[origen] or (self.torres[destino] and self.torres[origen][-1] > self.torres[destino][-1]):
                    origen, destino = destino, origen
                self.mover_disco(origen, destino)
                if mostrar:
                    print(f"Movimiento {self.contador_movimientos}: Mover disco de {origen} a {destino}")
            
            elif movimiento % 3 == 2:
                # Mover entre origen y auxiliar
                if not self.torres[origen] or (self.torres[auxiliar] and self.torres[origen][-1] > self.torres[auxiliar][-1]):
                    origen, auxiliar = auxiliar, origen
                self.mover_disco(origen, auxiliar)
                if mostrar:
                    print(f"Movimiento {self.contador_movimientos}: Mover disco de {origen} a {auxiliar}")
            
            else:  # movimiento % 3 == 0
                # Mover entre auxiliar y destino
                if not self.torres[auxiliar] or (self.torres[destino] and self.torres[auxiliar][-1] > self.torres[destino][-1]):
                    auxiliar, destino = destino, auxiliar
                self.mover_disco(auxiliar, destino)
                if mostrar:
                    print(f"Movimiento {self.contador_movimientos}: Mover disco de {auxiliar} a {destino}")
    
    def obtener_movimientos_minimos(self):
        """Retorna el número mínimo de movimientos requeridos (2^n - 1)."""
        return (1 << self.num_discos) - 1

# Ejemplo con pocos discos
print("Ejemplo: 3 discos")
hanoi1 = TorresHanoi(3)
hanoi1.mostrar_torres()
print(f"\nNúmero mínimo de movimientos: {hanoi1.obtener_movimientos_minimos()}")
print("\nResolviendo recursivamente:")
hanoi1.resolver_recursivo(mostrar=False)
hanoi1.mostrar_torres()
print(f"Total de movimientos realizados: {hanoi1.contador_movimientos}")
print()

# =============================================================================
# 2. DEMOSTRACIÓN PASO A PASO
# =============================================================================
print("=== 2. Demostración Paso a Paso (3 discos) ===")

hanoi2 = TorresHanoi(3)
hanoi2.mostrar_torres()
print("\nIniciando solución paso a paso:\n")
hanoi2.resolver_recursivo(mostrar=True)
hanoi2.mostrar_torres()
print(f"\nOK Problema resuelto en {hanoi2.contador_movimientos} movimientos")
print()

# =============================================================================
# 3. ANÁLISIS DE COMPLEJIDAD
# =============================================================================
print("=== 3. Análisis de Complejidad ===")

def analizar_complejidad_hanoi(max_discos=8):
    """Analiza la complejidad del problema de las Torres de Hanoi."""
    print(f"Análisis para 1 a {max_discos} discos:\n")
    print("Discos | Movimientos Mínimos | T(n) = 2^n - 1")
    print("-" * 45)
    
    for n in range(1, max_discos + 1):
        movimientos = (1 << n) - 1  # 2^n - 1
        print(f"  {n:2d}   | {movimientos:19d} | 2^{n} - 1 = {movimientos}")

analizar_complejidad_hanoi(8)
print()

# =============================================================================
# 4. COMPARACIÓN RECURSIVO vs ITERATIVO
# =============================================================================
print("=== 4. Comparación: Recursivo vs Iterativo ===")

def comparar_metodos(num_discos):
    """Compara los métodos recursivo e iterativo."""
    print(f"\nComparación con {num_discos} discos:")
    
    # Método recursivo
    hanoi_rec = TorresHanoi(num_discos)
    inicio = time.time()
    hanoi_rec.resolver_recursivo(mostrar=False)
    tiempo_rec = time.time() - inicio
    
    # Método iterativo
    hanoi_iter = TorresHanoi(num_discos)
    inicio = time.time()
    hanoi_iter.resolver_iterativo(mostrar=False)
    tiempo_iter = time.time() - inicio
    
    print(f"  Recursivo: {tiempo_rec*1000:.4f} ms ({hanoi_rec.contador_movimientos} movimientos)")
    print(f"  Iterativo: {tiempo_iter*1000:.4f} ms ({hanoi_iter.contador_movimientos} movimientos)")
    print(f"  Movimientos mínimos requeridos: {(1 << num_discos) - 1}")

comparar_metodos(5)
print()

# =============================================================================
# 5. HISTORIA Y APLICACIONES
# =============================================================================
print("=== 5. Información Adicional ===")

print("""
Historia del Problema de las Torres de Hanoi:

El problema fue inventado por el matemático francés Édouard Lucas en 1883.
Según la leyenda, existe un templo en Hanoi (Vietnam) donde los monjes
están resolviendo este problema con 64 discos de oro. Se dice que cuando
completen la tarea, el mundo llegará a su fin.

Matemáticas:
- Número mínimo de movimientos: 2^n - 1
- Para n=3: 7 movimientos
- Para n=64: 18,446,744,073,709,551,615 movimientos
- Si cada movimiento toma 1 segundo: ~585 billones de años

Aplicaciones:
- Enseñanza de recursión
- Análisis de algoritmos
- Estructuras de datos (stack operations)
- Backup rotativo de datos
- Puzzles y juegos
""")

# Resumen
print("=== RESUMEN ===")
print("""
Torres de Hanoi implementado:

1. Solución Recursiva:
   - Divide el problema en subproblemas más pequeños
   - Complejidad: O(2^n)
   - Movimientos: 2^n - 1

2. Solución Iterativa:
   - Implementación basada en paridad
   - Mismo número de movimientos
   - Alternativa no recursiva

3. Características:
   - Problema clásico de recursión
   - Demuestra divide y vencerás
   - Ejemplo perfecto de recursión

4. Reglas:
   - Solo mover un disco a la vez
   - Solo mover el disco superior
   - Disco grande no puede ir sobre uno pequeño

Este problema es fundamental en ciencias de la computación para
entender recursión y análisis de complejidad algorítmica.
""")
