# Archivo: 34_rango_matriz.py
# Descripción: Calcular el rango de una matriz usando NumPy

import numpy as np

print("=== Rango de una Matriz ===\n")
print("El rango de una matriz es el número de filas (o columnas) linealmente independientes.\n")

# Versión 1: Original
print("=== Versión 1: Original ===")
def rango_matriz_original():
    """
    Versión original del código para calcular el rango de una matriz.
    """
    A = np.array([[1, 2, 3, 4], [0, 2, -1, 5], [0, 0, 3, 7]])
    print(A)
    resultado = np.linalg.matrix_rank(A)  # Calcula el rango de la matriz A
    print(resultado)

print("Resultado versión original:")
rango_matriz_original()
print()

# Versión 2: Optimizada y mejorada
print("=== Versión 2: Optimizada y Mejorada ===")
def calcular_rango_matriz(A, mostrar_info=True):
    """
    Calcula el rango de una matriz con información adicional.
    
    Parámetros:
    - A: Matriz numpy
    - mostrar_info: Si mostrar información detallada
    
    Retorna:
    - rango: Rango de la matriz
    - info: Diccionario con información adicional
    """
    rango = np.linalg.matrix_rank(A)
    
    if mostrar_info:
        print(f"Matriz ({A.shape[0]}x{A.shape[1]}):")
        print(A)
        print(f"\nRango de la matriz: {rango}")
        print(f"Rango máximo posible: min({A.shape[0]}, {A.shape[1]}) = {min(A.shape)}")
        
        if rango == min(A.shape):
            print("✓ Matriz de rango completo (full rank)")
        else:
            print(f"⚠️  Matriz de rango reducido (rank deficient)")
            print(f"   Dependencias: {min(A.shape) - rango} fila(s) o columna(s) dependientes")
    
    info = {
        'rango': rango,
        'forma': A.shape,
        'rango_maximo': min(A.shape),
        'rango_completo': rango == min(A.shape)
    }
    
    return rango, info

# Matriz del ejemplo original
A = np.array([[1, 2, 3, 4], [0, 2, -1, 5], [0, 0, 3, 7]])
rango, info = calcular_rango_matriz(A.copy())
print()

# Versión 3: Análisis completo
print("=== Versión 3: Análisis Completo ===")
def analizar_rango_completo(A):
    """
    Realiza un análisis completo del rango de la matriz.
    """
    print("=" * 70)
    print("ANÁLISIS DEL RANGO DE LA MATRIZ")
    print("=" * 70)
    
    print(f"\nMatriz A ({A.shape[0]}x{A.shape[1]}):")
    print(A)
    
    # Rango
    rango = np.linalg.matrix_rank(A)
    print(f"\n1. Rango de la matriz: {rango}")
    
    # Rango máximo
    rango_maximo = min(A.shape)
    print(f"2. Rango máximo posible: min({A.shape[0]}, {A.shape[1]}) = {rango_maximo}")
    
    # Tipo de matriz
    print(f"\n3. Tipo de matriz:")
    if rango == rango_maximo:
        print(f"   ✓ Matriz de rango completo (full rank)")
        print(f"   → Todas las filas (o columnas) son linealmente independientes")
    else:
        print(f"   ⚠️  Matriz de rango reducido (rank deficient)")
        dependencias = rango_maximo - rango
        print(f"   → {dependencias} fila(s) o columna(s) son linealmente dependientes")
    
    # Determinante (solo para matrices cuadradas)
    if A.shape[0] == A.shape[1]:
        det = np.linalg.det(A)
        print(f"\n4. Determinante (matriz cuadrada): {det:.6f}")
        if abs(det) < 1e-10:
            print(f"   ⚠️  Determinante ≈ 0 → Matriz singular")
            print(f"   → El rango es menor que {A.shape[0]}")
        else:
            print(f"   ✓ Determinante ≠ 0 → Matriz no singular")
            print(f"   → El rango es {A.shape[0]} (rango completo)")
    
    # Espacios fundamentales
    print(f"\n5. Espacios fundamentales:")
    print(f"   Dimensión del espacio de columnas: {rango}")
    print(f"   Dimensión del espacio de filas: {rango}")
    if A.shape[0] == A.shape[1]:
        print(f"   Dimensión del espacio nulo: {A.shape[0] - rango}")
    
    print("=" * 70)
    return rango

print("Análisis completo:")
rango_completo = analizar_rango_completo(A.copy())
print()

# Versión 4: Comparación de métodos
print("=== Versión 4: Comparación de Métodos ===")
def comparar_metodos_rango(A):
    """
    Compara diferentes métodos para calcular el rango.
    """
    print("\nComparando métodos para calcular el rango:")
    print("=" * 60)
    
    # Método 1: matrix_rank (recomendado)
    rango1 = np.linalg.matrix_rank(A)
    print(f"1. np.linalg.matrix_rank(): {rango1}")
    
    # Método 2: Usando SVD (Singular Value Decomposition)
    U, s, Vt = np.linalg.svd(A, full_matrices=False)
    tolerancia = max(A.shape) * np.finfo(s.dtype).eps
    rango2 = np.sum(s > tolerancia)
    print(f"2. SVD (valores singulares): {rango2}")
    print(f"   Valores singulares: {s}")
    print(f"   Valores singulares > tolerancia ({tolerancia:.2e}): {rango2}")
    
    # Método 3: Usando eliminación gaussiana (aproximado)
    # Convertir a forma escalonada reducida
    try:
        # Usar qr para descomposición QR
        Q, R = np.linalg.qr(A)
        rango3 = np.sum(np.abs(np.diag(R)) > 1e-10)
        print(f"3. QR (diagonales no nulas): {rango3}")
    except Exception as e:
        print(f"3. QR: Error - {e}")
        rango3 = rango1
    
    print("=" * 60)
    print(f"✓ Todos los métodos dan resultados consistentes: {rango1 == rango2 == rango3}")
    return rango1

comparar_metodos_rango(A.copy())
print()

# Versión 5: Matrices de diferentes tipos
print("=== Versión 5: Matrices de Diferentes Tipos ===")
def ejemplos_diferentes_matrices():
    """
    Muestra ejemplos de rangos para diferentes tipos de matrices.
    """
    print("\nEjemplos de rangos para diferentes matrices:")
    print("=" * 70)
    
    ejemplos = {
        'Matriz identidad 3x3': np.eye(3),
        'Matriz de rango completo': np.array([[1, 2], [3, 4]]),
        'Matriz de rango reducido': np.array([[1, 2], [2, 4]]),  # segunda fila = 2 * primera fila
        'Matriz del ejemplo original': A,
        'Matriz cero': np.zeros((3, 3)),
        'Matriz rectangular (más columnas)': np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]),
        'Matriz rectangular (más filas)': np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    }
    
    for nombre, matriz in ejemplos.items():
        rango = np.linalg.matrix_rank(matriz)
        rango_max = min(matriz.shape)
        tipo = "Completo" if rango == rango_max else "Reducido"
        print(f"\n{nombre}:")
        print(f"  Forma: {matriz.shape}, Rango: {rango}/{rango_max} ({tipo})")
        if matriz.size <= 16:  # Solo mostrar si es pequeña
            print(f"  Matriz:\n{matriz}")
    
    print("=" * 70)

ejemplos_diferentes_matrices()
print()

# Versión 6: Rango de productos de matrices
print("=== Versión 6: Propiedades del Rango ===")
def propiedades_rango():
    """
    Demuestra propiedades importantes del rango de matrices.
    """
    print("\nPropiedades del Rango de Matrices:")
    print("=" * 70)
    
    # Propiedad 1: rank(A) = rank(A^T)
    A_t = A.T
    rango_A = np.linalg.matrix_rank(A)
    rango_At = np.linalg.matrix_rank(A_t)
    print(f"1. rank(A) = rank(A^T)")
    print(f"   rank(A) = {rango_A}")
    print(f"   rank(A^T) = {rango_At}")
    print(f"   ✓ Coinciden: {rango_A == rango_At}")
    
    # Propiedad 2: rank(AB) <= min(rank(A), rank(B))
    if A.shape[1] == 3:  # A es 3x4, necesita matriz 4x? para multiplicar
        B = np.random.rand(4, 2)
        AB = A @ B
        rango_AB = np.linalg.matrix_rank(AB)
        rango_B = np.linalg.matrix_rank(B)
        print(f"\n2. rank(AB) <= min(rank(A), rank(B))")
        print(f"   rank(A) = {rango_A}, rank(B) = {rango_B}")
        print(f"   rank(AB) = {rango_AB}")
        print(f"   min(rank(A), rank(B)) = {min(rango_A, rango_B)}")
        print(f"   ✓ Se cumple: {rango_AB <= min(rango_A, rango_B)}")
    
    # Propiedad 3: rank(A) <= min(m, n) para matriz m×n
    m, n = A.shape
    print(f"\n3. rank(A) <= min(m, n) para matriz {m}×{n}")
    print(f"   rank(A) = {rango_A}")
    print(f"   min({m}, {n}) = {min(m, n)}")
    print(f"   ✓ Se cumple: {rango_A <= min(m, n)}")
    
    print("=" * 70)

propiedades_rango()
print()

# Versión 7: Función interactiva
print("=== Versión 7: Función Interactiva ===")
def rango_matriz_interactivo():
    """
    Función interactiva para calcular el rango de matrices.
    """
    while True:
        try:
            print("\n" + "=" * 60)
            print("CALCULADORA DE RANGO DE MATRIZ")
            print("=" * 60)
            print("\nOpciones:")
            print("1. Usar matriz de ejemplo")
            print("2. Crear matriz personalizada")
            print("3. Salir")
            
            opcion = input("\nSeleccione una opción: ").strip()
            
            if opcion == "1":
                matriz = A.copy()
                print("\nMatriz de ejemplo:")
                print(matriz)
            
            elif opcion == "2":
                filas = int(input("Número de filas: "))
                columnas = int(input("Número de columnas: "))
                print(f"\nIngrese los elementos de la matriz ({filas}x{columnas}):")
                print("(Separados por espacios, una fila por línea)")
                
                elementos = []
                for i in range(filas):
                    fila_str = input(f"Fila {i+1}: ")
                    fila = [float(x) for x in fila_str.split()]
                    if len(fila) != columnas:
                        print(f"Error: La fila debe tener {columnas} elementos")
                        break
                    elementos.append(fila)
                else:
                    matriz = np.array(elementos)
            
            elif opcion == "3":
                print("👋 ¡Hasta luego!")
                break
            
            else:
                print("❌ Opción no válida")
                continue
            
            # Calcular y mostrar rango
            rango, info = calcular_rango_matriz(matriz, mostrar_info=True)
            
            continuar = input("\n¿Analizar otra matriz? (s/n): ").lower()
            if continuar != 's':
                break
        
        except ValueError:
            print("❌ Por favor ingrese números válidos")
        except KeyboardInterrupt:
            print("\n\n👋 Operación cancelada")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

# Descomentar para probar:
# rango_matriz_interactivo()

# Resumen
print("=== Resumen de Análisis ===")
print("Código original:")
print("  ✓ Funciona correctamente")
print("  ✓ Usa np.linalg.matrix_rank() (método recomendado)")
print("  ✓ Código simple y claro")
print("  ⚠️  No muestra información adicional")
print("  ⚠️  No analiza el tipo de matriz")
print("  ⚠️  No compara con otros métodos")
print()
print("Mejoras implementadas:")
print("  1. ✅ Análisis completo del rango")
print("  2. ✅ Identificación de matriz de rango completo vs reducido")
print("  3. ✅ Comparación de métodos (matrix_rank, SVD, QR)")
print("  4. ✅ Ejemplos de diferentes tipos de matrices")
print("  5. ✅ Propiedades matemáticas del rango")
print("  6. ✅ Función interactiva")
print("  7. ✅ Información sobre espacios fundamentales")
print("  8. ✅ Documentación completa")
print()
print("Conceptos importantes:")
print("  - Rango completo: rank(A) = min(m, n)")
print("  - Rango reducido: rank(A) < min(m, n)")
print("  - El rango indica el número de filas/columnas independientes")
print("  - Para matrices cuadradas: rango completo ↔ determinante ≠ 0")
