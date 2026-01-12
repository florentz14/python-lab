# Archivo: 09_matrices.py
# Descripción: Trabajar con matrices usando NumPy

import numpy as np

print("=== Matrices con NumPy ===\n")

# Crear matrices
print("=== Crear Matrices ===")
# Matriz desde lista
matriz1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matriz 3x3:")
print(matriz1)
print()

# Matriz de ceros
ceros = np.zeros((3, 3))
print("Matriz de ceros 3x3:")
print(ceros)
print()

# Matriz de unos
unos = np.ones((2, 4))
print("Matriz de unos 2x4:")
print(unos)
print()

# Matriz identidad
identidad = np.eye(3)
print("Matriz identidad 3x3:")
print(identidad)
print()

# Matriz con valores aleatorios
aleatorios = np.random.randint(1, 10, (3, 3))
print("Matriz aleatoria 3x3:")
print(aleatorios)
print()

# Matriz con rango
rango = np.arange(1, 13).reshape(3, 4)
print("Matriz con números del 1 al 12 (3x4):")
print(rango)
print()

# Operaciones con matrices
print("=== Operaciones con Matrices ===")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(f"Matriz A:\n{A}")
print(f"\nMatriz B:\n{B}\n")

# Suma
suma = A + B
print(f"Suma (A + B):\n{suma}")

# Resta
resta = A - B
print(f"\nResta (A - B):\n{resta}")

# Multiplicación elemento por elemento
mult_elemento = A * B
print(f"\nMultiplicación elemento por elemento (A * B):\n{mult_elemento}")

# Multiplicación de matrices
mult_matriz = np.dot(A, B)  # o A @ B
print(f"\nMultiplicación de matrices (A @ B):\n{mult_matriz}")

# Multiplicación por escalar
escalar = 2 * A
print(f"\nMultiplicación por escalar (2 * A):\n{escalar}\n")

# Propiedades de matrices
print("=== Propiedades de Matrices ===")
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Matriz M:\n{M}")
print(f"Dimensiones (shape): {M.shape}")
print(f"Tamaño (size): {M.size}")
print(f"Número de dimensiones (ndim): {M.ndim}")
print(f"Tipo de datos (dtype): {M.dtype}\n")

# Acceder a elementos
print("=== Acceder a Elementos ===")
print(f"Matriz:\n{M}")
print(f"Elemento [1, 2]: {M[1, 2]}")
print(f"Fila 0: {M[0, :]}")
print(f"Columna 1: {M[:, 1]}")
print(f"Submatriz 2x2: {M[0:2, 0:2]}\n")

# Operaciones matemáticas
print("=== Operaciones Matemáticas ===")
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Matriz:\n{matriz}")
print(f"Suma de todos los elementos: {np.sum(matriz)}")
print(f"Suma por filas: {np.sum(matriz, axis=1)}")
print(f"Suma por columnas: {np.sum(matriz, axis=0)}")
print(f"Promedio: {np.mean(matriz)}")
print(f"Valor máximo: {np.max(matriz)}")
print(f"Valor mínimo: {np.min(matriz)}")
print(f"Desviación estándar: {np.std(matriz):.2f}\n")

# Transpuesta
print("=== Transpuesta ===")
matriz_original = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Matriz original:\n{matriz_original}")
print(f"Transpuesta:\n{matriz_original.T}\n")

# Determinante (solo matrices cuadradas)
print("=== Determinante ===")
matriz_cuadrada = np.array([[2, 1], [3, 4]])
determinante = np.linalg.det(matriz_cuadrada)
print(f"Matriz:\n{matriz_cuadrada}")
print(f"Determinante: {determinante:.2f}\n")

# Inversa de matriz
print("=== Matriz Inversa ===")
matriz_inv = np.array([[1, 2], [3, 4]])
try:
    inversa = np.linalg.inv(matriz_inv)
    print(f"Matriz original:\n{matriz_inv}")
    print(f"Matriz inversa:\n{inversa}")
    # Verificar: A * A^-1 = I
    producto = np.dot(matriz_inv, inversa)
    print(f"\nVerificación (A * A^-1):\n{producto}")
except np.linalg.LinAlgError:
    print("La matriz no tiene inversa")

print()

# Resolver sistema de ecuaciones lineales
print("=== Resolver Sistema de Ecuaciones ===")
# Sistema: 2x + y = 5
#          x + 3y = 10
coeficientes = np.array([[2, 1], [1, 3]])
constantes = np.array([5, 10])
solucion = np.linalg.solve(coeficientes, constantes)
print(f"Coeficientes:\n{coeficientes}")
print(f"Constantes: {constantes}")
print(f"Solución (x, y): {solucion}\n")

# Ejemplo práctico: operaciones con matrices más grandes
print("=== Ejemplo Práctico ===")
matriz_grande = np.random.randint(1, 100, (4, 4))
print(f"Matriz 4x4 aleatoria:\n{matriz_grande}")
print(f"Suma total: {np.sum(matriz_grande)}")
print(f"Promedio: {np.mean(matriz_grande):.2f}")
print(f"Valores únicos: {np.unique(matriz_grande)}")
