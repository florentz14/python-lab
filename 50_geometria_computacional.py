# Archivo: 50_geometria_computacional.py
# Descripción: Algoritmos de Geometría Computacional

import math
import numpy as np

print("=== Geometría Computacional ===\n")

# =============================================================================
# 1. DISTANCIA ENTRE PUNTOS
# =============================================================================
print("=== 1. Distancias entre Puntos ===")

class Punto:
    """Representa un punto en 2D."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Punto({self.x}, {self.y})"
    
    def distancia_euclidiana(self, otro):
        """Distancia euclidiana entre dos puntos."""
        return math.sqrt((self.x - otro.x)**2 + (self.y - otro.y)**2)
    
    def distancia_manhattan(self, otro):
        """Distancia Manhattan (L1)."""
        return abs(self.x - otro.x) + abs(self.y - otro.y)
    
    def distancia_chebyshev(self, otro):
        """Distancia Chebyshev (L∞)."""
        return max(abs(self.x - otro.x), abs(self.y - otro.y))

def distancia_puntos(p1, p2):
    """Distancia euclidiana entre dos puntos."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Ejemplo
p1 = Punto(0, 0)
p2 = Punto(3, 4)

print(f"Punto 1: {p1}")
print(f"Punto 2: {p2}")
print(f"Distancia euclidiana: {p1.distancia_euclidiana(p2):.2f}")
print(f"Distancia Manhattan: {p1.distancia_manhattan(p2)}")
print(f"Distancia Chebyshev: {p1.distancia_chebyshev(p2)}")
print()

# =============================================================================
# 2. ÁREA DE POLÍGONOS
# =============================================================================
print("=== 2. Área de Polígonos ===")

def area_poligono_simple(puntos):
    """
    Calcula el área de un polígono simple usando fórmula del shoelace.
    Puntos deben estar en orden (horario o antihorario).
    """
    n = len(puntos)
    if n < 3:
        return 0.0
    
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += puntos[i][0] * puntos[j][1]
        area -= puntos[j][0] * puntos[i][1]
    
    return abs(area) / 2.0

def area_triangulo(p1, p2, p3):
    """Calcula el área de un triángulo usando fórmula del determinante."""
    return abs((p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1] - p2[1])) / 2.0)

# Ejemplo
triangulo = [(0, 0), (4, 0), (2, 3)]
print(f"Triángulo: {triangulo}")
print(f"Área: {area_triangulo(triangulo[0], triangulo[1], triangulo[2]):.2f}")

poligono = [(0, 0), (4, 0), (4, 3), (0, 3)]  # Rectángulo
print(f"\nPolígono (rectángulo): {poligono}")
print(f"Área: {area_poligono_simple(poligono):.2f}")
print()

# =============================================================================
# 3. CONVEX HULL (Graham Scan)
# =============================================================================
print("=== 3. Convex Hull (Graham Scan) ===")

def orientacion(p, q, r):
    """
    Determina la orientación del triple (p, q, r).
    Retorna: 0 (colineales), 1 (horario), 2 (antihorario)
    """
    valor = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    
    if valor == 0:
        return 0  # Colineales
    return 1 if valor > 0 else 2  # Horario o antihorario

def graham_scan(puntos):
    """
    Encuentra el Convex Hull usando algoritmo de Graham Scan.
    Complejidad: O(n log n)
    """
    n = len(puntos)
    if n < 3:
        return puntos
    
    # Encontrar el punto más bajo (y más a la izquierda si hay empate)
    punto_inferior = min(puntos, key=lambda p: (p[1], p[0]))
    
    # Ordenar puntos por ángulo polar respecto al punto inferior
    def angulo_polar(p):
        if p == punto_inferior:
            return (-1, 0, 0)
        dx = p[0] - punto_inferior[0]
        dy = p[1] - punto_inferior[1]
        return (0, -dy / math.sqrt(dx*dx + dy*dy), -(dx*dx + dy*dy))
    
    puntos_ordenados = sorted(puntos, key=angulo_polar)
    
    # Construir hull
    hull = [puntos_ordenados[0], puntos_ordenados[1]]
    
    for i in range(2, n):
        while len(hull) > 1 and orientacion(hull[-2], hull[-1], puntos_ordenados[i]) != 2:
            hull.pop()
        hull.append(puntos_ordenados[i])
    
    return hull

# Ejemplo
puntos_hull = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
print(f"Puntos: {puntos_hull}")
hull = graham_scan(puntos_hull)
print(f"Convex Hull: {hull}")
print()

# =============================================================================
# 4. INTERSECCIÓN DE LÍNEAS
# =============================================================================
print("=== 4. Intersección de Líneas ===")

def interseccion_lineas(p1, p2, p3, p4):
    """
    Encuentra el punto de intersección entre dos líneas.
    Línea 1: de p1 a p2
    Línea 2: de p3 a p4
    Retorna: (x, y) o None si son paralelas
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    
    # Calcular denominador
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    
    if abs(denom) < 1e-10:
        return None  # Líneas paralelas
    
    # Calcular intersección
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
    x = x1 + t * (x2 - x1)
    y = y1 + t * (y2 - y1)
    
    return (x, y)

def interseccion_segmentos(p1, p2, p3, p4):
    """
    Verifica si dos segmentos se intersecan.
    """
    def ccw(A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])
    
    return ccw(p1, p3, p4) != ccw(p2, p3, p4) and ccw(p1, p2, p3) != ccw(p1, p2, p4)

# Ejemplo
linea1_p1 = (0, 0)
linea1_p2 = (2, 2)
linea2_p1 = (0, 2)
linea2_p2 = (2, 0)

interseccion = interseccion_lineas(linea1_p1, linea1_p2, linea2_p1, linea2_p2)
print(f"Línea 1: {linea1_p1} a {linea1_p2}")
print(f"Línea 2: {linea2_p1} a {linea2_p2}")
print(f"Intersección: {interseccion}")

se_intersecan = interseccion_segmentos(linea1_p1, linea1_p2, linea2_p1, linea2_p2)
print(f"¿Segmentos se intersecan? {se_intersecan}")
print()

# =============================================================================
# 5. INTERSECCIÓN DE CÍRCULOS
# =============================================================================
print("=== 5. Intersección de Círculos ===")

def interseccion_circulos(c1, r1, c2, r2):
    """
    Encuentra los puntos de intersección entre dos círculos.
    c1, c2: centros (x, y)
    r1, r2: radios
    Retorna: lista de puntos de intersección (0, 1, o 2 puntos)
    """
    x1, y1 = c1
    x2, y2 = c2
    
    # Distancia entre centros
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Sin intersección
    if d > r1 + r2:
        return []  # Círculos separados
    
    # Un círculo dentro del otro
    if d < abs(r1 - r2):
        return []  # Un círculo contiene al otro
    
    # Mismo centro
    if d == 0 and r1 == r2:
        return []  # Círculos idénticos
    
    # Un punto de intersección (tangentes)
    if d == r1 + r2 or d == abs(r1 - r2):
        # Punto en la línea entre centros
        t = r1 / d
        x = x1 + t * (x2 - x1)
        y = y1 + t * (y2 - y1)
        return [(x, y)]
    
    # Dos puntos de intersección
    # Usar ley de cosenos
    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = math.sqrt(r1**2 - a**2)
    
    # Punto medio en la línea entre centros
    x_m = x1 + a * (x2 - x1) / d
    y_m = y1 + a * (y2 - y1) / d
    
    # Puntos de intersección
    x3 = x_m + h * (y2 - y1) / d
    y3 = y_m - h * (x2 - x1) / d
    
    x4 = x_m - h * (y2 - y1) / d
    y4 = y_m + h * (x2 - x1) / d
    
    return [(x3, y3), (x4, y4)]

# Ejemplo
circulo1 = (0, 0)
radio1 = 5
circulo2 = (8, 0)
radio2 = 3

intersecciones = interseccion_circulos(circulo1, radio1, circulo2, radio2)
print(f"Círculo 1: centro {circulo1}, radio {radio1}")
print(f"Círculo 2: centro {circulo2}, radio {radio2}")
print(f"Puntos de intersección: {intersecciones}")

if intersecciones:
    for i, punto in enumerate(intersecciones, 1):
        print(f"  Punto {i}: ({punto[0]:.4f}, {punto[1]:.4f})")
print()

# =============================================================================
# 6. PUNTO EN POLÍGONO
# =============================================================================
print("=== 6. Punto en Polígono (Ray Casting) ===")

def punto_en_poligono(punto, poligono):
    """
    Determina si un punto está dentro de un polígono usando ray casting.
    Retorna: True si está dentro, False si está fuera
    """
    x, y = punto
    n = len(poligono)
    dentro = False
    
    j = n - 1
    for i in range(n):
        xi, yi = poligono[i]
        xj, yj = poligono[j]
        
        # Verificar intersección con el rayo
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            dentro = not dentro
        j = i
    
    return dentro

# Ejemplo
poligono_test = [(0, 0), (4, 0), (4, 4), (0, 4)]  # Cuadrado
punto_dentro = (2, 2)
punto_fuera = (5, 5)

print(f"Polígono: {poligono_test}")
print(f"¿Punto {punto_dentro} está dentro? {punto_en_poligono(punto_dentro, poligono_test)}")
print(f"¿Punto {punto_fuera} está dentro? {punto_en_poligono(punto_fuera, poligono_test)}")
print()

# Resumen
print("=== RESUMEN ===")
print("""
Algoritmos de Geometría Computacional implementados:

1. Distancias entre Puntos:
   - Euclidiana (L2)
   - Manhattan (L1)
   - Chebyshev (L∞)
   - Complejidad: O(1)

2. Área de Polígonos:
   - Fórmula del shoelace
   - Área de triángulos
   - Complejidad: O(n)

3. Convex Hull (Graham Scan):
   - Encuentra la envolvente convexa
   - Complejidad: O(n log n)
   - Aplicaciones: procesamiento de imágenes, planificación de rutas

4. Intersección de Líneas:
   - Punto de intersección
   - Verificación de intersección de segmentos
   - Complejidad: O(1)

5. Intersección de Círculos:
   - Encuentra puntos de intersección
   - Maneja todos los casos (0, 1, 2 puntos)
   - Complejidad: O(1)

6. Punto en Polígono:
   - Ray casting algorithm
   - Complejidad: O(n)
   - Aplicaciones: GIS, detección de colisiones

Aplicaciones:
- Gráficos por computadora
- Sistemas de información geográfica (GIS)
- Robótica y planificación de movimiento
- Detección de colisiones
- Análisis espacial
""")
