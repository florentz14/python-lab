# Archivo: 25_sistemas_ecuaciones_lineales.py
# Descripción: Resolver sistemas de ecuaciones lineales usando álgebra lineal

import numpy as np
import fractions
from fractions import Fraction

# Configurar numpy para mostrar fracciones
np.set_printoptions(formatter={'all': lambda x: str(
    fractions.Fraction(x).limit_denominator())})

print("=== Sistemas de Ecuaciones Lineales ===\n")

# Versión 1: Original
print("=== Versión 1: Original ===")
def resolver_sistema_original(A, b):
    """
    Versión original del código para resolver sistemas de ecuaciones lineales.
    """
    try:
        # Calculamos el determinante
        determinante = np.linalg.det(A)
        print(f'El determinante es: {determinante}')
        print()
        
        # Matriz no singular
        if determinante != 0:
            print('Solución del sistema:')
            x = np.linalg.solve(A, b)
            print(x)
            print()

            print('Comprobamos que A * x = b')
            print(np.matmul(A, x))
        else:
            print('La matriz es singular')
    except Exception as e:
        print(f'Ha ocurrido una excepción: {e}')

# Datos de prueba del código original
A = np.array([[7, -5, 0], [5, -17, 5], [0, 5, -7]])
b = np.array([9, 0, 5])

print("Sistema de ecuaciones:")
print("Matriz A:")
print(A)
print("\nVector b (términos independientes):")
print(b)
print("\nResolviendo sistema...")
resolver_sistema_original(A.copy(), b.copy())
print()

# Versión 2: Optimizada y mejorada
print("=== Versión 2: Optimizada y Mejorada ===")
def resolver_sistema_mejorado(A, b, mostrar_proceso=True, tolerancia=1e-10):
    """
    Resuelve un sistema de ecuaciones lineales Ax = b de manera mejorada.
    
    Parámetros:
    - A: Matriz de coeficientes (numpy array)
    - b: Vector de términos independientes (numpy array)
    - mostrar_proceso: Si mostrar el proceso paso a paso
    - tolerancia: Tolerancia para considerar si el determinante es cero
    
    Retorna:
    - x: Vector solución, o None si no hay solución única
    - info: Diccionario con información sobre la solución
    """
    try:
        # Validar dimensiones
        if A.shape[0] != A.shape[1]:
            raise ValueError("La matriz A debe ser cuadrada")
        
        if A.shape[0] != b.shape[0]:
            raise ValueError("Las dimensiones de A y b no coinciden")
        
        # Calcular determinante
        determinante = np.linalg.det(A)
        
        if mostrar_proceso:
            print(f'Determinante: {determinante:.6f}')
        
        # Verificar si la matriz es singular
        if abs(determinante) < tolerancia:
            if mostrar_proceso:
                print('⚠️  La matriz es singular (determinante ≈ 0)')
                print('   El sistema puede tener infinitas soluciones o ninguna solución')
            return None, {'singular': True, 'determinante': determinante}
        
        # Resolver el sistema
        x = np.linalg.solve(A, b)
        
        # Verificar la solución
        b_verificacion = np.dot(A, x)
        error = np.linalg.norm(b - b_verificacion)
        
        info = {
            'singular': False,
            'determinante': determinante,
            'solucion': x,
            'error': error,
            'verificacion_correcta': error < tolerancia
        }
        
        if mostrar_proceso:
            print(f'\n✅ Solución del sistema:')
            print(x)
            print(f'\n✅ Verificación: A * x = b')
            print(f'   Calculado: {b_verificacion}')
            print(f'   Esperado:  {b}')
            print(f'   Error: {error:.2e}')
            
            if error < tolerancia:
                print('   ✓ La solución es correcta')
            else:
                print('   ⚠️  Hay un error significativo en la verificación')
        
        return x, info
        
    except np.linalg.LinAlgError as e:
        if mostrar_proceso:
            print(f'❌ Error en álgebra lineal: {e}')
        return None, {'error': str(e)}
    except Exception as e:
        if mostrar_proceso:
            print(f'❌ Error: {e}')
        return None, {'error': str(e)}

# Probar versión mejorada
print("Resolviendo con versión mejorada:")
x, info = resolver_sistema_mejorado(A.copy(), b.copy())
print()

# Versión 3: Con múltiples sistemas
print("=== Versión 3: Múltiples Sistemas ===")
def resolver_multiples_sistemas(A, B):
    """
    Resuelve múltiples sistemas Ax = b para cada columna de B.
    
    Parámetros:
    - A: Matriz de coeficientes
    - B: Matriz donde cada columna es un vector b diferente
    
    Retorna:
    - X: Matriz solución donde cada columna es una solución
    """
    try:
        X = np.linalg.solve(A, B)
        return X
    except np.linalg.LinAlgError as e:
        print(f'Error: {e}')
        return None

# Ejemplo con múltiples sistemas
print("Ejemplo: Resolver múltiples sistemas")
B_multiple = np.array([[9, 12], [0, 0], [5, 6]]).T  # Dos sistemas diferentes
print(f"Matriz B con múltiples sistemas:\n{B_multiple.T}")
X_multiple = resolver_multiples_sistemas(A.copy(), B_multiple)
if X_multiple is not None:
    print(f"\nSoluciones (cada columna es una solución):\n{X_multiple}")
print()

# Versión 4: Mostrar en fracciones
print("=== Versión 4: Mostrar Solución en Fracciones ===")
def resolver_sistema_fracciones(A, b):
    """
    Resuelve el sistema y muestra la solución en fracciones.
    """
    try:
        x = np.linalg.solve(A, b)
        
        print("Solución en decimales:")
        print(x)
        
        print("\nSolución en fracciones:")
        for i, valor in enumerate(x):
            frac = Fraction(valor).limit_denominator()
            print(f"  x[{i}] = {frac} = {float(frac):.6f}")
        
        return x
    except Exception as e:
        print(f'Error: {e}')
        return None

print("Resolviendo y mostrando en fracciones:")
resolver_sistema_fracciones(A.copy(), b.copy())
print()

# Versión 5: Análisis completo del sistema
print("=== Versión 5: Análisis Completo ===")
def analizar_sistema_completo(A, b):
    """
    Realiza un análisis completo del sistema de ecuaciones.
    """
    print("=" * 60)
    print("ANÁLISIS DEL SISTEMA DE ECUACIONES")
    print("=" * 60)
    
    print(f"\n1. Matriz de coeficientes A ({A.shape[0]}x{A.shape[1]}):")
    print(A)
    
    print(f"\n2. Vector de términos independientes b:")
    print(b)
    
    # Determinante
    det = np.linalg.det(A)
    print(f"\n3. Determinante: {det:.6f}")
    
    # Rango
    rango = np.linalg.matrix_rank(A)
    print(f"4. Rango de la matriz: {rango}")
    
    # Condición de la matriz
    cond = np.linalg.cond(A)
    print(f"5. Número de condición: {cond:.2e}")
    if cond > 1e12:
        print("   ⚠️  Matriz mal condicionada (puede haber errores numéricos)")
    elif cond > 1e8:
        print("   ⚠️  Matriz moderadamente mal condicionada")
    else:
        print("   ✓ Matriz bien condicionada")
    
    # Solución
    if abs(det) > 1e-10:
        x = np.linalg.solve(A, b)
        print(f"\n6. Solución del sistema:")
        print(x)
        
        # Verificación
        b_verif = np.dot(A, x)
        error = np.linalg.norm(b - b_verif)
        print(f"\n7. Verificación (A * x = b):")
        print(f"   Error: {error:.2e}")
        if error < 1e-10:
            print("   ✓ Solución verificada correctamente")
        else:
            print("   ⚠️  Error en la verificación")
    else:
        print("\n6. ⚠️  Sistema singular - no se puede resolver")
    
    print("=" * 60)

analizar_sistema_completo(A.copy(), b.copy())
print()

# Versión 6: Sistemas con comentarios
print("=== Versión 6: Sistema del Código Original ===")
# Matriz A del código original
A_original = np.array([[7, -5, 0], [5, -17, 5], [0, 5, -7]])
# Vector b del código original
b_original = np.array([9, 0, 5])

# También hay comentarios sobre otra matriz B y vector d
B_comentado = np.array([[10, -5, -5], [5, -12, 3], [5, 3, -8]])
d_comentado = np.array([12, 0, 6])

print("Sistema original (A, b):")
x1, info1 = resolver_sistema_mejorado(A_original, b_original, mostrar_proceso=True)

print("\nSistema comentado (B, d):")
x2, info2 = resolver_sistema_mejorado(B_comentado, d_comentado, mostrar_proceso=True)
print()

# Versión 7: Función interactiva
print("=== Versión 7: Ejemplos y Comparación ===")
def comparar_metodos(A, b):
    """
    Compara diferentes métodos para resolver el sistema.
    """
    print(f"\nComparando métodos para el sistema Ax = b")
    print(f"Matriz A:\n{A}")
    print(f"Vector b: {b}\n")
    
    # Método 1: solve (más eficiente para sistemas cuadrados)
    try:
        x1 = np.linalg.solve(A, b)
        print(f"1. np.linalg.solve(): {x1}")
    except Exception as e:
        print(f"1. np.linalg.solve(): Error - {e}")
        x1 = None
    
    # Método 2: inversa (menos eficiente, pero más intuitivo)
    try:
        A_inv = np.linalg.inv(A)
        x2 = np.dot(A_inv, b)
        print(f"2. A^(-1) * b: {x2}")
        if x1 is not None:
            error = np.linalg.norm(x1 - x2)
            print(f"   Diferencia con método 1: {error:.2e}")
    except Exception as e:
        print(f"2. A^(-1) * b: Error - {e}")
    
    # Método 3: lstsq (para sistemas sobredeterminados)
    try:
        x3, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
        print(f"3. np.linalg.lstsq(): {x3}")
        print(f"   Residuales: {residuals}")
    except Exception as e:
        print(f"3. np.linalg.lstsq(): Error - {e}")

comparar_metodos(A.copy(), b.copy())
print()

# Resumen
print("=== Resumen ===")
print("El código original:")
print("  ✓ Resuelve correctamente sistemas de ecuaciones lineales")
print("  ✓ Verifica la solución")
print("  ⚠️  No valida dimensiones")
print("  ⚠️  Manejo de errores básico")
print("  ⚠️  No muestra información adicional")
print()
print("Mejoras implementadas:")
print("  1. ✅ Validación de dimensiones")
print("  2. ✅ Manejo de errores mejorado")
print("  3. ✅ Análisis completo (rango, condición, etc.)")
print("  4. ✅ Visualización en fracciones")
print("  5. ✅ Múltiples sistemas simultáneos")
print("  6. ✅ Comparación de métodos")
print("  7. ✅ Documentación completa")
print("  8. ✅ Verificación de solución mejorada")
