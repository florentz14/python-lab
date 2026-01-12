# Archivo: 49_metodos_numericos.py
# Descripción: Métodos Numéricos

import numpy as np
import matplotlib.pyplot as plt

print("=== Métodos Numéricos ===\n")

# =============================================================================
# 1. MÉTODO DE NEWTON-RAPHSON (Raíces)
# =============================================================================
print("=== 1. Método de Newton-Raphson ===")

def newton_raphson(f, df, x0, tolerancia=1e-6, max_iter=100):
    """
    Encuentra una raíz de f(x) = 0 usando el método de Newton-Raphson.
    
    Parámetros:
    - f: función f(x)
    - df: derivada f'(x)
    - x0: valor inicial
    - tolerancia: precisión deseada
    - max_iter: máximo número de iteraciones
    
    Retorna: (raíz, número de iteraciones, convergió)
    """
    x = x0
    iteraciones = []
    
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        
        if abs(dfx) < 1e-10:
            return None, i, False  # Derivada muy pequeña
        
        x_nuevo = x - fx / dfx
        iteraciones.append((x, fx, x_nuevo))
        
        if abs(x_nuevo - x) < tolerancia:
            return x_nuevo, i + 1, True
        
        x = x_nuevo
    
    return x, max_iter, False

def newton_raphson_grafico(f, df, x0, a=-5, b=5):
    """Muestra gráficamente el método de Newton-Raphson."""
    x_vals = np.linspace(a, b, 1000)
    y_vals = [f(x) for x in x_vals]
    
    # Aplicar método
    raiz, iteraciones, convergio = newton_raphson(f, df, x0)
    
    # Calcular puntos de iteración
    x_actual = x0
    puntos_iteracion = [x0]
    for i in range(min(iteraciones, 10)):
        fx = f(x_actual)
        dfx = df(x_actual)
        if abs(dfx) < 1e-10:
            break
        x_actual = x_actual - fx / dfx
        puntos_iteracion.append(x_actual)
    
    print(f"Raíz encontrada: {raiz}")
    print(f"Iteraciones: {iteraciones}")
    print(f"Convergió: {convergio}")
    print(f"Valor f(raíz): {f(raiz) if raiz else 'N/A'}")
    
    return raiz, puntos_iteracion

# Ejemplo 1: Raíz cuadrada
print("Ejemplo 1: Encontrar raíz cuadrada de 16 (x² - 16 = 0)")
f1 = lambda x: x**2 - 16
df1 = lambda x: 2*x
raiz1, iter1, conv1 = newton_raphson(f1, df1, 5.0)
print(f"Raíz: {raiz1}, Iteraciones: {iter1}, Convergió: {conv1}")
print()

# Ejemplo 2: Función cúbica
print("Ejemplo 2: Encontrar raíz de x³ - x - 1 = 0")
f2 = lambda x: x**3 - x - 1
df2 = lambda x: 3*x**2 - 1
raiz2, iter2, conv2 = newton_raphson(f2, df2, 1.5)
print(f"Raíz: {raiz2:.6f}, Iteraciones: {iter2}, Convergió: {conv2}")
print()

# =============================================================================
# 2. INTERPOLACIÓN DE LAGRANGE
# =============================================================================
print("=== 2. Interpolación de Lagrange ===")

def interpolacion_lagrange(x_puntos, y_puntos, x_evaluar):
    """
    Interpola un punto usando polinomio de Lagrange.
    
    Parámetros:
    - x_puntos: lista de puntos x conocidos
    - y_puntos: lista de valores y conocidos
    - x_evaluar: punto x donde evaluar
    
    Retorna: valor interpolado
    """
    n = len(x_puntos)
    resultado = 0.0
    
    for i in range(n):
        producto = 1.0
        for j in range(n):
            if i != j:
                producto *= (x_evaluar - x_puntos[j]) / (x_puntos[i] - x_puntos[j])
        resultado += y_puntos[i] * producto
    
    return resultado

def construir_polinomio_lagrange(x_puntos, y_puntos):
    """Construye el polinomio de Lagrange como función."""
    def polinomio(x):
        return interpolacion_lagrange(x_puntos, y_puntos, x)
    return polinomio

# Ejemplo
x_conocidos = [0, 1, 2, 3]
y_conocidos = [1, 2, 5, 10]

print(f"Puntos conocidos:")
for i in range(len(x_conocidos)):
    print(f"  ({x_conocidos[i]}, {y_conocidos[i]})")

x_interpolar = 1.5
y_interpolado = interpolacion_lagrange(x_conocidos, y_conocidos, x_interpolar)
print(f"\nValor interpolado en x={x_interpolar}: {y_interpolado:.4f}")

# Verificar en puntos conocidos
print("\nVerificación en puntos conocidos:")
for x, y in zip(x_conocidos, y_conocidos):
    valor = interpolacion_lagrange(x_conocidos, y_conocidos, x)
    print(f"  x={x}: esperado={y}, obtenido={valor:.6f}")
print()

# =============================================================================
# 3. INTERPOLACIÓN DE NEWTON (Diferencias Divididas)
# =============================================================================
print("=== 3. Interpolación de Newton ===")

def diferencias_divididas(x_puntos, y_puntos):
    """
    Calcula las diferencias divididas para interpolación de Newton.
    """
    n = len(x_puntos)
    tabla = [[0.0] * n for _ in range(n)]
    
    # Primera columna: valores y
    for i in range(n):
        tabla[i][0] = y_puntos[i]
    
    # Calcular diferencias divididas
    for j in range(1, n):
        for i in range(n - j):
            tabla[i][j] = (tabla[i+1][j-1] - tabla[i][j-1]) / (x_puntos[i+j] - x_puntos[i])
    
    return tabla[0]  # Retornar primera fila (coeficientes)

def interpolacion_newton(x_puntos, y_puntos, x_evaluar):
    """
    Interpola usando método de Newton (diferencias divididas).
    """
    n = len(x_puntos)
    coeficientes = diferencias_divididas(x_puntos, y_puntos)
    
    resultado = coeficientes[0]
    producto = 1.0
    
    for i in range(1, n):
        producto *= (x_evaluar - x_puntos[i-1])
        resultado += coeficientes[i] * producto
    
    return resultado

# Ejemplo
x_newton = [1, 2, 4, 5]
y_newton = [0, 1, 15, 24]

print(f"Puntos conocidos:")
for i in range(len(x_newton)):
    print(f"  ({x_newton[i]}, {y_newton[i]})")

coefs = diferencias_divididas(x_newton, y_newton)
print(f"\nCoeficientes de diferencias divididas: {coefs}")

x_interp = 3.0
y_newton_interp = interpolacion_newton(x_newton, y_newton, x_interp)
print(f"Valor interpolado en x={x_interp}: {y_newton_interp:.4f}")
print()

# =============================================================================
# 4. REGRESIÓN LINEAL (Desde Cero)
# =============================================================================
print("=== 4. Regresión Lineal (Desde Cero) ===")

def regresion_lineal(x_datos, y_datos):
    """
    Calcula regresión lineal y = mx + b usando mínimos cuadrados.
    
    Retorna: (pendiente m, intercepto b, R²)
    """
    n = len(x_datos)
    
    # Calcular medias
    x_media = sum(x_datos) / n
    y_media = sum(y_datos) / n
    
    # Calcular sumas necesarias
    suma_xy = sum((x_datos[i] - x_media) * (y_datos[i] - y_media) for i in range(n))
    suma_x2 = sum((x_datos[i] - x_media) ** 2 for i in range(n))
    
    # Calcular pendiente e intercepto
    if suma_x2 == 0:
        return None, None, 0.0
    
    m = suma_xy / suma_x2
    b = y_media - m * x_media
    
    # Calcular R² (coeficiente de determinación)
    y_predicho = [m * x + b for x in x_datos]
    ss_res = sum((y_datos[i] - y_predicho[i]) ** 2 for i in range(n))
    ss_tot = sum((y_datos[i] - y_media) ** 2 for i in range(n))
    r_cuadrado = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0.0
    
    return m, b, r_cuadrado

def predecir_regresion(m, b, x):
    """Predice un valor usando la recta de regresión."""
    return m * x + b

# Ejemplo
x_reg = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_reg = [2.1, 4.2, 5.8, 8.1, 9.9, 12.2, 13.8, 16.1, 18.0, 20.1]

print(f"Datos X: {x_reg}")
print(f"Datos Y: {y_reg}")

m, b, r2 = regresion_lineal(x_reg, y_reg)
print(f"\nEcuación: y = {m:.4f}x + {b:.4f}")
print(f"R² (coeficiente de determinación): {r2:.4f}")

# Predicciones
print("\nPredicciones:")
for x in [11, 12, 15]:
    y_pred = predecir_regresion(m, b, x)
    print(f"  x={x}: y={y_pred:.2f}")

# Comparación con valores reales
print("\nComparación datos reales vs predichos:")
y_predichos = [predecir_regresion(m, b, x) for x in x_reg]
for i in range(len(x_reg)):
    print(f"  x={x_reg[i]}: real={y_reg[i]:.2f}, predicho={y_predichos[i]:.2f}, error={abs(y_reg[i]-y_predichos[i]):.2f}")
print()

# =============================================================================
# 5. REGRESIÓN POLINOMIAL
# =============================================================================
print("=== 5. Regresión Polinomial (Grado 2) ===")

def regresion_polinomial(x_datos, y_datos, grado=2):
    """
    Regresión polinomial usando mínimos cuadrados.
    Retorna coeficientes [a_n, a_{n-1}, ..., a_0] donde:
    y = a_n*x^n + a_{n-1}*x^{n-1} + ... + a_0
    """
    n = len(x_datos)
    
    # Construir matriz de Vandermonde
    A = []
    for x in x_datos:
        fila = [x**i for i in range(grado + 1)]
        A.append(fila)
    
    A = np.array(A)
    b = np.array(y_datos)
    
    # Resolver sistema normal: (A^T * A) * x = A^T * b
    ATA = np.dot(A.T, A)
    ATb = np.dot(A.T, b)
    
    try:
        coeficientes = np.linalg.solve(ATA, ATb)
        return coeficientes[::-1]  # Revertir para orden estándar
    except:
        return None

# Ejemplo
x_poly = [0, 1, 2, 3, 4, 5]
y_poly = [1, 2, 5, 10, 17, 26]  # y ≈ x² + 1

coefs_poly = regresion_polinomial(x_poly, y_poly, grado=2)
if coefs_poly is not None:
    print(f"Datos: x={x_poly}, y={y_poly}")
    print(f"Coeficientes (ax² + bx + c): a={coefs_poly[0]:.4f}, b={coefs_poly[1]:.4f}, c={coefs_poly[2]:.4f}")
    print(f"Ecuación: y = {coefs_poly[0]:.4f}x² + {coefs_poly[1]:.4f}x + {coefs_poly[2]:.4f}")
print()

# Resumen
print("=== RESUMEN ===")
print("""
Métodos numéricos implementados:

1. Método de Newton-Raphson:
   - Encuentra raíces de ecuaciones no lineales
   - Convergencia rápida (cuadrática)
   - Requiere derivada
   - Complejidad: O(k) donde k = número de iteraciones

2. Interpolación de Lagrange:
   - Construye polinomio que pasa por puntos dados
   - Exacto en puntos conocidos
   - Complejidad: O(n²) para n puntos

3. Interpolación de Newton:
   - Usa diferencias divididas
   - Más eficiente que Lagrange para agregar puntos
   - Complejidad: O(n²)

4. Regresión Lineal:
   - Ajusta recta y = mx + b
   - Mínimos cuadrados
   - Calcula R² (bondad de ajuste)
   - Complejidad: O(n)

5. Regresión Polinomial:
   - Ajusta polinomio de grado k
   - Mínimos cuadrados
   - Complejidad: O(n³) para resolver sistema

Aplicaciones:
- Ingeniería: encontrar raíces de ecuaciones
- Ciencia de datos: interpolación y extrapolación
- Machine Learning: regresión como base
- Análisis numérico: solución de problemas matemáticos
""")
