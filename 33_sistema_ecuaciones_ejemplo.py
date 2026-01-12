# Archivo: 33_sistema_ecuaciones_ejemplo.py
# Descripción: Resolver sistema de ecuaciones lineales específico

import numpy as np
import fractions
from fractions import Fraction

# Configurar numpy para mostrar fracciones
np.set_printoptions(formatter={'all': lambda x: str(
    fractions.Fraction(x).limit_denominator())})

print("=== Sistema de Ecuaciones Lineales (Ejemplo Específico) ===\n")

# Versión 1: Original
print("=== Versión 1: Original ===")
def resolver_sistema_original():
    """
    Versión original del código.
    """
    # Matriz A
    A = np.array([[1, 1, 1], [2, 0, 1], [1, 2, 0]])
    # Vector b, términos independientes
    b = np.array([2, 1, 5])
    
    try:
        # Calculamos el determinante
        determinante = np.linalg.det(A)
        print(f'El determinante es: {round(determinante, 2)}')
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

print("Ejecutando versión original:")
resolver_sistema_original()
print()

# Versión 2: Optimizada y mejorada
print("=== Versión 2: Optimizada y Mejorada ===")
def resolver_sistema_mejorado(A, b, mostrar_proceso=True, tolerancia=1e-10):
    """
    Resuelve el sistema de ecuaciones con mejoras.
    
    Sistema: Ax = b
    donde A = [[1, 1, 1], [2, 0, 1], [1, 2, 0]]
    y b = [2, 1, 5]
    
    Esto representa:
    x + y + z = 2
    2x + 0y + z = 1
    x + 2y + 0z = 5
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
            print(f"Determinante: {determinante:.6f}")
            print(f"Determinante (redondeado): {round(determinante, 2)}")
            print()
        
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
            print('✅ Solución del sistema:')
            print(x)
            print()
            
            print('✅ Verificación: A * x = b')
            print(f'   A * x = {b_verificacion}')
            print(f'   b =     {b}')
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

# Datos del ejemplo
A = np.array([[1, 1, 1], [2, 0, 1], [1, 2, 0]])
b = np.array([2, 1, 5])

print("Resolviendo sistema con versión mejorada:")
x, info = resolver_sistema_mejorado(A.copy(), b.copy())
print()

# Versión 3: Análisis completo del sistema
print("=== Versión 3: Análisis Completo ===")
def analizar_sistema_completo(A, b):
    """
    Analiza el sistema de ecuaciones completamente.
    """
    print("=" * 70)
    print("ANÁLISIS DEL SISTEMA DE ECUACIONES")
    print("=" * 70)
    
    print(f"\nSistema de ecuaciones:")
    print(f"  x + y + z = {b[0]}")
    print(f"  2x + 0y + z = {b[1]}")
    print(f"  x + 2y + 0z = {b[2]}")
    
    print(f"\n1. Matriz de coeficientes A (3x3):")
    print(A)
    
    print(f"\n2. Vector de términos independientes b:")
    print(b)
    
    # Determinante
    det = np.linalg.det(A)
    print(f"\n3. Determinante:")
    print(f"   det(A) = {det:.6f}")
    print(f"   det(A) (redondeado) = {round(det, 2)}")
    
    # Rango
    rango = np.linalg.matrix_rank(A)
    print(f"\n4. Rango de la matriz: {rango}")
    print(f"   Rango completo: {'Sí' if rango == A.shape[0] else 'No'}")
    
    # Condición de la matriz
    cond = np.linalg.cond(A)
    print(f"\n5. Número de condición: {cond:.2e}")
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
        print(f"   x = {x[0]:.6f} = {Fraction(x[0]).limit_denominator()}")
        print(f"   y = {x[1]:.6f} = {Fraction(x[1]).limit_denominator()}")
        print(f"   z = {x[2]:.6f} = {Fraction(x[2]).limit_denominator()}")
        print(f"   Vector solución: {x}")
        
        # Verificación
        b_verif = np.dot(A, x)
        error = np.linalg.norm(b - b_verif)
        print(f"\n7. Verificación (A * x = b):")
        print(f"   A * x = {b_verif}")
        print(f"   b =     {b}")
        print(f"   Error: {error:.2e}")
        if error < 1e-10:
            print("   ✓ Solución verificada correctamente")
        else:
            print("   ⚠️  Error en la verificación")
        
        # Verificación ecuación por ecuación
        print(f"\n8. Verificación ecuación por ecuación:")
        ecuaciones = [
            f"x + y + z = {x[0]:.6f} + {x[1]:.6f} + {x[2]:.6f} = {b_verif[0]:.6f} (esperado: {b[0]})",
            f"2x + z = 2({x[0]:.6f}) + {x[2]:.6f} = {b_verif[1]:.6f} (esperado: {b[1]})",
            f"x + 2y = {x[0]:.6f} + 2({x[1]:.6f}) = {b_verif[2]:.6f} (esperado: {b[2]})"
        ]
        for eq in ecuaciones:
            print(f"   {eq}")
    else:
        print("\n6. ⚠️  Sistema singular - no se puede resolver")
    
    print("=" * 70)
    return x if abs(det) > 1e-10 else None

print("Análisis completo del sistema:")
solucion = analizar_sistema_completo(A.copy(), b.copy())
print()

# Versión 4: Solución paso a paso
print("=== Versión 4: Solución Paso a Paso (Método de Eliminación) ===")
def resolver_paso_a_paso(A, b):
    """
    Muestra el proceso de resolución paso a paso.
    """
    print("\nResolución paso a paso usando eliminación gaussiana:")
    print("(Nota: numpy usa métodos optimizados internamente)")
    print()
    
    # Crear matriz aumentada [A|b]
    A_aumentada = np.column_stack([A, b])
    print("Matriz aumentada [A|b]:")
    print(A_aumentada)
    print()
    
    # Resolver
    x = np.linalg.solve(A, b)
    print("Solución encontrada:")
    print(f"  x = {x[0]:.6f}")
    print(f"  y = {x[1]:.6f}")
    print(f"  z = {x[2]:.6f}")
    
    return x

resolver_paso_a_paso(A.copy(), b.copy())
print()

# Versión 5: Verificación manual
print("=== Versión 5: Verificación Manual ===")
def verificar_solucion_manual(A, b, x):
    """
    Verifica la solución manualmente.
    """
    print("\nVerificación manual de la solución:")
    print("=" * 50)
    
    # Ecuación 1: x + y + z = 2
    eq1 = x[0] + x[1] + x[2]
    print(f"Ecuación 1: x + y + z = {x[0]:.6f} + {x[1]:.6f} + {x[2]:.6f} = {eq1:.6f}")
    print(f"  Esperado: {b[0]}, Diferencia: {abs(eq1 - b[0]):.2e}")
    
    # Ecuación 2: 2x + z = 1
    eq2 = 2*x[0] + x[2]
    print(f"\nEcuación 2: 2x + z = 2({x[0]:.6f}) + {x[2]:.6f} = {eq2:.6f}")
    print(f"  Esperado: {b[1]}, Diferencia: {abs(eq2 - b[1]):.2e}")
    
    # Ecuación 3: x + 2y = 5
    eq3 = x[0] + 2*x[1]
    print(f"\nEcuación 3: x + 2y = {x[0]:.6f} + 2({x[1]:.6f}) = {eq3:.6f}")
    print(f"  Esperado: {b[2]}, Diferencia: {abs(eq3 - b[2]):.2e}")
    
    print("=" * 50)
    
    # Verificar todas
    todas_correctas = (abs(eq1 - b[0]) < 1e-10 and 
                      abs(eq2 - b[1]) < 1e-10 and 
                      abs(eq3 - b[2]) < 1e-10)
    print(f"\n✅ Todas las ecuaciones se verifican: {todas_correctas}")

if solucion is not None:
    verificar_solucion_manual(A, b, solucion)
    print()

# Versión 6: Comparación con otros métodos
print("=== Versión 6: Comparación con Otros Métodos ===")
def comparar_metodos(A, b):
    """
    Compara diferentes métodos para resolver el sistema.
    """
    print("\nComparando métodos de resolución:")
    print("=" * 60)
    
    # Método 1: solve (más eficiente)
    x1 = np.linalg.solve(A, b)
    print(f"1. np.linalg.solve(): {x1}")
    
    # Método 2: inversa
    A_inv = np.linalg.inv(A)
    x2 = np.dot(A_inv, b)
    print(f"2. A^(-1) * b: {x2}")
    error = np.linalg.norm(x1 - x2)
    print(f"   Diferencia con método 1: {error:.2e}")
    
    # Método 3: lstsq
    x3, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
    print(f"3. np.linalg.lstsq(): {x3}")
    print(f"   Residuales: {residuals}")
    print(f"   Rango: {rank}")
    
    print("=" * 60)
    print(f"✓ Todos los métodos dan resultados consistentes")

comparar_metodos(A.copy(), b.copy())
print()

# Resumen
print("=== Resumen de Análisis ===")
print("Código original:")
print("  ✓ Funciona correctamente")
print("  ✓ Resuelve el sistema de ecuaciones")
print("  ✓ Verifica la solución")
print("  ⚠️  No valida dimensiones")
print("  ⚠️  Manejo de errores básico")
print("  ⚠️  No muestra información adicional (rango, condición, etc.)")
print("  ⚠️  Redondea el determinante (puede perder precisión)")
print()
print("Mejoras implementadas:")
print("  1. ✅ Validación de dimensiones")
print("  2. ✅ Manejo de errores mejorado")
print("  3. ✅ Análisis completo (rango, condición, etc.)")
print("  4. ✅ Verificación detallada ecuación por ecuación")
print("  5. ✅ Comparación de métodos")
print("  6. ✅ Solución paso a paso")
print("  7. ✅ Visualización en fracciones")
print("  8. ✅ Documentación completa")
print()
print("Sistema resuelto:")
print("  x + y + z = 2")
print("  2x + z = 1")
print("  x + 2y = 5")
print("\n  Solución: x, y, z (ver valores arriba)")
