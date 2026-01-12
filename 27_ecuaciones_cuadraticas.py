# Archivo: 27_ecuaciones_cuadraticas.py
# Descripción: Resolver ecuaciones cuadráticas Ax² + Bx + C = 0

import math
import cmath
import numpy as np
import matplotlib.pyplot as plt

print("=== Ecuaciones Cuadráticas ===\n")
print("Forma general: Ax² + Bx + C = 0, donde A ≠ 0\n")

# Versión 1: Original
print("=== Versión 1: Original ===")
def ecuacion_cuadratica_original(a, b, c):
    """
    Versión original para resolver ecuaciones cuadráticas.
    Solo retorna soluciones reales.
    """
    condicional = b**2 - (4*a*c)
    if condicional > 0:
        x1 = (-b + math.sqrt(condicional))/(2*a)
        x2 = (-b - math.sqrt(condicional))/(2*a)
        return (x1, x2)
    elif condicional == 0:
        x1 = -b / (2*a)
        return (x1,)
    else:
        return tuple()

# Pruebas del código original
print("Pruebas del código original:")
print(f"x² + 8x + 12 = 0: {ecuacion_cuadratica_original(1, 8, 12)}")
print(f"x² + 2x + 1 = 0: {ecuacion_cuadratica_original(1, 2, 1)}")
print(f"3x² - 8x + 6 = 0: {ecuacion_cuadratica_original(3, -8, 6)}")  # Corregido: -8 en lugar de 8
print()

# Versión 2: Optimizada con números complejos
print("=== Versión 2: Optimizada (con Números Complejos) ===")
def ecuacion_cuadratica_completa(a, b, c, solo_reales=False):
    """
    Resuelve ecuaciones cuadráticas, incluyendo soluciones complejas.
    
    Parámetros:
    - a, b, c: Coeficientes de la ecuación Ax² + Bx + C = 0
    - solo_reales: Si True, retorna solo soluciones reales (tuple vacío si son complejas)
    
    Retorna:
    - Tupla con las soluciones (puede ser 0, 1 o 2 soluciones)
    """
    # Validar que a != 0
    if a == 0:
        raise ValueError("El coeficiente 'a' no puede ser cero (no es una ecuación cuadrática)")
    
    # Calcular discriminante
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        # Dos soluciones reales distintas
        raiz = math.sqrt(discriminante)
        x1 = (-b + raiz) / (2*a)
        x2 = (-b - raiz) / (2*a)
        return (x1, x2)
    elif discriminante == 0:
        # Una solución real (raíz doble)
        x1 = -b / (2*a)
        return (x1,)
    else:
        # Dos soluciones complejas
        if solo_reales:
            return tuple()
        raiz = cmath.sqrt(discriminante)
        x1 = (-b + raiz) / (2*a)
        x2 = (-b - raiz) / (2*a)
        return (x1, x2)

# Pruebas versión optimizada
print("Pruebas versión optimizada:")
print(f"x² + 8x + 12 = 0: {ecuacion_cuadratica_completa(1, 8, 12)}")
print(f"x² + 2x + 1 = 0: {ecuacion_cuadratica_completa(1, 2, 1)}")
print(f"3x² - 8x + 6 = 0: {ecuacion_cuadratica_completa(3, -8, 6)}")
print(f"x² + 1 = 0 (solo complejas): {ecuacion_cuadratica_completa(1, 0, 1)}")
print()

# Versión 3: Con análisis completo
print("=== Versión 3: Con Análisis Completo ===")
def analizar_ecuacion_cuadratica(a, b, c):
    """
    Analiza una ecuación cuadrática completamente.
    """
    print("=" * 60)
    print(f"ANÁLISIS DE LA ECUACIÓN: {a}x² + {b}x + {c} = 0")
    print("=" * 60)
    
    # Validar
    if a == 0:
        print("❌ Error: No es una ecuación cuadrática (a = 0)")
        return None
    
    # Discriminante
    discriminante = b**2 - 4*a*c
    print(f"\n1. Discriminante (Δ = b² - 4ac):")
    print(f"   Δ = {b}² - 4({a})({c}) = {discriminante}")
    
    # Tipo de soluciones
    print(f"\n2. Tipo de soluciones:")
    if discriminante > 0:
        print("   ✓ Dos soluciones reales distintas")
        print("   → La parábola corta al eje X en dos puntos")
    elif discriminante == 0:
        print("   ✓ Una solución real (raíz doble)")
        print("   → La parábola toca al eje X en un punto (vértice)")
    else:
        print("   ⚠️  Dos soluciones complejas conjugadas")
        print("   → La parábola no corta al eje X (no tiene raíces reales)")
    
    # Soluciones
    print(f"\n3. Soluciones:")
    soluciones = ecuacion_cuadratica_completa(a, b, c)
    if soluciones:
        if len(soluciones) == 2:
            print(f"   x₁ = {soluciones[0]}")
            print(f"   x₂ = {soluciones[1]}")
            if discriminante > 0:
                print(f"\n   Verificación:")
                print(f"   x₁ + x₂ = {soluciones[0] + soluciones[1]} (debería ser -b/a = {-b/a})")
                print(f"   x₁ · x₂ = {soluciones[0] * soluciones[1]} (debería ser c/a = {c/a})")
        else:
            print(f"   x = {soluciones[0]} (raíz doble)")
    else:
        print("   No hay soluciones reales")
    
    # Vértice de la parábola
    print(f"\n4. Vértice de la parábola:")
    x_vertice = -b / (2*a)
    y_vertice = a*x_vertice**2 + b*x_vertice + c
    print(f"   V = ({x_vertice:.4f}, {y_vertice:.4f})")
    
    # Concavidad
    print(f"\n5. Concavidad:")
    if a > 0:
        print("   ↑ Parábola abre hacia arriba (a > 0)")
    else:
        print("   ↓ Parábola abre hacia abajo (a < 0)")
    
    print("=" * 60)
    return soluciones

# Ejemplos de análisis
print("Análisis de ejemplos:")
analizar_ecuacion_cuadratica(1, 8, 12)
print()
analizar_ecuacion_cuadratica(1, 2, 1)
print()

# Versión 4: Graficar ecuación cuadrática
print("=== Versión 4: Graficar Ecuación Cuadrática ===")
def graficar_ecuacion_cuadratica(a, b, c, x_min=-10, x_max=10, mostrar_raices=True):
    """
    Grafica una ecuación cuadrática y marca las raíces si existen.
    """
    try:
        # Crear rango de x
        x = np.linspace(x_min, x_max, 1000)
        y = a*x**2 + b*x + c
        
        # Crear gráfico
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'b-', linewidth=2, label=f'{a}x² + {b}x + {c} = 0')
        
        # Ejes
        plt.axhline(y=0, color='k', linewidth=0.5, linestyle='--')
        plt.axvline(x=0, color='k', linewidth=0.5, linestyle='--')
        
        # Marcar raíces
        if mostrar_raices:
            soluciones = ecuacion_cuadratica_completa(a, b, c, solo_reales=True)
            if soluciones:
                for sol in soluciones:
                    if isinstance(sol, (int, float)) and x_min <= sol <= x_max:
                        plt.plot(sol, 0, 'ro', markersize=10, label=f'Raíz: x = {sol:.2f}')
        
        # Vértice
        x_vertice = -b / (2*a)
        y_vertice = a*x_vertice**2 + b*x_vertice + c
        if x_min <= x_vertice <= x_max:
            plt.plot(x_vertice, y_vertice, 'go', markersize=8, label=f'Vértice: ({x_vertice:.2f}, {y_vertice:.2f})')
        
        plt.xlabel('x', fontsize=12)
        plt.ylabel('y', fontsize=12)
        plt.title(f'Gráfica de {a}x² + {b}x + {c} = 0', fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"Error al graficar: {e}")

# Descomentar para graficar:
# print("Graficando x² + 8x + 12 = 0")
# graficar_ecuacion_cuadratica(1, 8, 12)
# print()

# Versión 5: Resolver múltiples ecuaciones
print("=== Versión 5: Resolver Múltiples Ecuaciones ===")
def resolver_multiples_ecuaciones(ecuaciones):
    """
    Resuelve múltiples ecuaciones cuadráticas.
    
    Parámetros:
    - ecuaciones: Lista de tuplas (a, b, c)
    """
    resultados = []
    for i, (a, b, c) in enumerate(ecuaciones, 1):
        print(f"\nEcuación {i}: {a}x² + {b}x + {c} = 0")
        try:
            soluciones = ecuacion_cuadratica_completa(a, b, c)
            resultados.append((a, b, c, soluciones))
            if soluciones:
                if len(soluciones) == 2:
                    print(f"  Soluciones: x₁ = {soluciones[0]:.4f}, x₂ = {soluciones[1]:.4f}")
                else:
                    print(f"  Solución: x = {soluciones[0]:.4f} (raíz doble)")
            else:
                print(f"  Sin soluciones reales")
        except Exception as e:
            print(f"  Error: {e}")
            resultados.append((a, b, c, None))
    
    return resultados

# Ejemplo
print("Resolviendo múltiples ecuaciones:")
ecuaciones_ejemplo = [
    (1, 8, 12),
    (1, 2, 1),
    (3, -8, 6),
    (1, 0, -4),  # x² - 4 = 0
    (2, -5, 2)   # 2x² - 5x + 2 = 0
]
resolver_multiples_ecuaciones(ecuaciones_ejemplo)
print()

# Versión 6: Función interactiva
print("=== Versión 6: Función Interactiva ===")
def ecuacion_cuadratica_interactiva():
    """
    Función interactiva para resolver ecuaciones cuadráticas.
    """
    while True:
        try:
            print("\n" + "=" * 50)
            print("RESOLVER ECUACIÓN CUADRÁTICA")
            print("=" * 50)
            print("Forma: Ax² + Bx + C = 0\n")
            
            a = float(input("Ingrese el coeficiente A (A ≠ 0): "))
            if a == 0:
                print("❌ Error: A no puede ser cero")
                continue
            
            b = float(input("Ingrese el coeficiente B: "))
            c = float(input("Ingrese el coeficiente C: "))
            
            print(f"\nEcuación: {a}x² + {b}x + {c} = 0")
            
            soluciones = ecuacion_cuadratica_completa(a, b, c)
            
            if soluciones:
                if len(soluciones) == 2:
                    print(f"\n✅ Dos soluciones:")
                    print(f"   x₁ = {soluciones[0]}")
                    print(f"   x₂ = {soluciones[1]}")
                else:
                    print(f"\n✅ Una solución (raíz doble):")
                    print(f"   x = {soluciones[0]}")
            else:
                print("\n⚠️  No hay soluciones reales (soluciones complejas)")
                soluciones_complejas = ecuacion_cuadratica_completa(a, b, c, solo_reales=False)
                print(f"   x₁ = {soluciones_complejas[0]}")
                print(f"   x₂ = {soluciones_complejas[1]}")
            
            continuar = input("\n¿Resolver otra ecuación? (s/n): ").lower()
            if continuar != 's':
                break
        
        except ValueError:
            print("❌ Error: Por favor ingrese números válidos")
        except KeyboardInterrupt:
            print("\n\n👋 Operación cancelada")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

# Descomentar para probar:
# ecuacion_cuadratica_interactiva()

# Versión 7: Comparación y verificación
print("=== Versión 7: Verificación de Soluciones ===")
def verificar_soluciones(a, b, c, soluciones):
    """
    Verifica que las soluciones sean correctas.
    """
    print(f"\nVerificando soluciones para {a}x² + {b}x + {c} = 0:")
    print(f"Soluciones encontradas: {soluciones}")
    
    if not soluciones:
        print("No hay soluciones reales para verificar")
        return
    
    for i, x in enumerate(soluciones, 1):
        resultado = a*x**2 + b*x + c
        print(f"  x_{i} = {x}")
        print(f"  Verificación: {a}({x})² + {b}({x}) + {c} = {resultado}")
        if abs(resultado) < 1e-10:
            print(f"  ✅ Correcto (error: {abs(resultado):.2e})")
        else:
            print(f"  ⚠️  Error: {abs(resultado):.2e}")

# Verificar ejemplos
print("Verificando soluciones de los ejemplos:")
verificar_soluciones(1, 8, 12, ecuacion_cuadratica_completa(1, 8, 12))
verificar_soluciones(1, 2, 1, ecuacion_cuadratica_completa(1, 2, 1))
print()

# Resumen
print("=== Resumen de Análisis ===")
print("Código original:")
print("  ✓ Funciona correctamente para soluciones reales")
print("  ✓ Retorna tuplas apropiadas")
print("  ⚠️  No maneja números complejos")
print("  ⚠️  No valida que a != 0")
print("  ⚠️  Error en ejemplo: (3, 8, 6) debería ser (3, -8, 6)")
print("  ⚠️  No hay análisis adicional")
print()
print("Mejoras implementadas:")
print("  1. ✅ Soporte para números complejos")
print("  2. ✅ Validación de entrada (a != 0)")
print("  3. ✅ Análisis completo (discriminante, vértice, concavidad)")
print("  4. ✅ Graficación de ecuaciones")
print("  5. ✅ Verificación de soluciones")
print("  6. ✅ Resolución de múltiples ecuaciones")
print("  7. ✅ Función interactiva")
print("  8. ✅ Documentación completa")
print()
print("Fórmula cuadrática:")
print("  x = (-b ± √(b² - 4ac)) / 2a")
print("\nDiscriminante (Δ = b² - 4ac):")
print("  Δ > 0: Dos soluciones reales distintas")
print("  Δ = 0: Una solución real (raíz doble)")
print("  Δ < 0: Dos soluciones complejas conjugadas")
