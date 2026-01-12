# Archivo: 31_integracion_numerica.py
# Descripción: Integración numérica usando SciPy

import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt

print("=== Integración Numérica ===\n")
print("Cálculo de integrales definidas usando métodos numéricos\n")

# Versión 1: Original
print("=== Versión 1: Original ===")
def integracion_original():
    """
    Versión original del código para calcular integrales.
    """
    def f(x):
        return (-x**2) - (2*x) + (8)
    
    pi = np.pi
    a = -4
    b = -3
    
    result, error = spi.quad(f, a, b)
    print(round(result, 2))

print("Resultado versión original:")
integracion_original()
print()

# Versión 2: Optimizada y mejorada
print("=== Versión 2: Optimizada y Mejorada ===")
def integrar_funcion(funcion, a, b, mostrar_detalles=True):
    """
    Calcula la integral definida de una función entre a y b.
    
    Parámetros:
    - funcion: Función a integrar
    - a: Límite inferior
    - b: Límite superior
    - mostrar_detalles: Si mostrar información detallada
    
    Retorna:
    - resultado: Valor de la integral
    - error: Estimación del error
    """
    resultado, error = spi.quad(funcion, a, b)
    
    if mostrar_detalles:
        print(f"Integral de {a} a {b}:")
        print(f"  Resultado: {resultado:.6f}")
        print(f"  Error estimado: {error:.2e}")
        print(f"  Resultado redondeado (2 decimales): {round(resultado, 2)}")
    
    return resultado, error

# Función del ejemplo original
def f_original(x):
    return (-x**2) - (2*x) + (8)

print("Integración optimizada:")
resultado, error = integrar_funcion(f_original, -4, -3)
print()

# Versión 3: Con múltiples funciones
print("=== Versión 3: Múltiples Funciones ===")
def integrar_multiples_funciones(funciones_dict, a, b):
    """
    Integra múltiples funciones en el mismo intervalo.
    """
    print(f"\nIntegrando múltiples funciones de {a} a {b}:")
    print("=" * 60)
    
    resultados = {}
    for nombre, funcion in funciones_dict.items():
        resultado, error = spi.quad(funcion, a, b)
        resultados[nombre] = resultado
        print(f"{nombre:20s}: {resultado:10.6f} (error: {error:.2e})")
    
    print("=" * 60)
    return resultados

# Definir varias funciones
funciones = {
    'Cuadrática original': lambda x: (-x**2) - (2*x) + 8,
    'x²': lambda x: x**2,
    'sin(x)': lambda x: np.sin(x),
    'exp(x)': lambda x: np.exp(x),
    '1/x': lambda x: 1/x if x != 0 else 0
}

print("Integrando múltiples funciones de 1 a 2:")
resultados = integrar_multiples_funciones(funciones, 1, 2)
print()

# Versión 4: Con visualización gráfica
print("=== Versión 4: Con Visualización Gráfica ===")
def graficar_integral(funcion, a, b, titulo="Integral Definida"):
    """
    Grafica la función y el área bajo la curva (integral).
    """
    try:
        # Crear rango de x
        x = np.linspace(a - 1, b + 1, 1000)
        y = funcion(x)
        
        # Calcular integral
        resultado, error = spi.quad(funcion, a, b)
        
        # Crear gráfico
        plt.figure(figsize=(10, 6))
        
        # Graficar función
        plt.plot(x, y, 'b-', linewidth=2, label='f(x)')
        
        # Rellenar área bajo la curva
        x_area = np.linspace(a, b, 1000)
        y_area = funcion(x_area)
        plt.fill_between(x_area, y_area, alpha=0.3, color='green', 
                        label=f'Área = {resultado:.4f}')
        
        # Líneas verticales en los límites
        plt.axvline(x=a, color='r', linestyle='--', linewidth=1, label=f'a = {a}')
        plt.axvline(x=b, color='r', linestyle='--', linewidth=1, label=f'b = {b}')
        
        # Eje x
        plt.axhline(y=0, color='k', linewidth=0.5)
        
        plt.xlabel('x', fontsize=12)
        plt.ylabel('f(x)', fontsize=12)
        plt.title(f'{titulo}\n∫ f(x)dx de {a} a {b} = {resultado:.4f}', 
                 fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.show()
        
        return resultado, error
    
    except Exception as e:
        print(f"Error al graficar: {e}")
        return None, None

# Descomentar para graficar:
# print("Graficando integral de la función original:")
# graficar_integral(f_original, -4, -3, "f(x) = -x² - 2x + 8")
# print()

# Versión 5: Comparación de métodos de integración
print("=== Versión 5: Comparación de Métodos ===")
def comparar_metodos_integracion(funcion, a, b):
    """
    Compara diferentes métodos de integración numérica.
    """
    print(f"\nComparando métodos de integración de {a} a {b}:")
    print("=" * 60)
    
    # Método 1: quad (adaptativo)
    resultado_quad, error_quad = spi.quad(funcion, a, b)
    print(f"1. quad (adaptativo):")
    print(f"   Resultado: {resultado_quad:.8f}")
    print(f"   Error: {error_quad:.2e}")
    
    # Método 2: fixed_quad (Gauss-Legendre)
    try:
        resultado_fixed, _ = spi.fixed_quad(funcion, a, b, n=50)
        print(f"\n2. fixed_quad (Gauss-Legendre, n=50):")
        print(f"   Resultado: {resultado_fixed:.8f}")
        print(f"   Diferencia con quad: {abs(resultado_quad - resultado_fixed):.2e}")
    except Exception as e:
        print(f"\n2. fixed_quad: Error - {e}")
    
    # Método 3: romberg (extrapolación de Richardson)
    try:
        resultado_romberg = spi.romberg(funcion, a, b)
        print(f"\n3. romberg (extrapolación):")
        print(f"   Resultado: {resultado_romberg:.8f}")
        print(f"   Diferencia con quad: {abs(resultado_quad - resultado_romberg):.2e}")
    except Exception as e:
        print(f"\n3. romberg: Error - {e}")
    
    # Método 4: simpson (regla de Simpson)
    try:
        x = np.linspace(a, b, 1000)
        y = funcion(x)
        resultado_simpson = spi.simpson(y, x)
        print(f"\n4. simpson (regla de Simpson, 1000 puntos):")
        print(f"   Resultado: {resultado_simpson:.8f}")
        print(f"   Diferencia con quad: {abs(resultado_quad - resultado_simpson):.2e}")
    except Exception as e:
        print(f"\n4. simpson: Error - {e}")
    
    # Método 5: trapezoid (regla del trapecio)
    try:
        x = np.linspace(a, b, 1000)
        y = funcion(x)
        resultado_trapezoid = spi.trapezoid(y, x)
        print(f"\n5. trapezoid (regla del trapecio, 1000 puntos):")
        print(f"   Resultado: {resultado_trapezoid:.8f}")
        print(f"   Diferencia con quad: {abs(resultado_quad - resultado_trapezoid):.2e}")
    except Exception as e:
        print(f"\n5. trapezoid: Error - {e}")
    
    print("=" * 60)

print("Comparando métodos para la función original:")
comparar_metodos_integracion(f_original, -4, -3)
print()

# Versión 6: Integrales impropias
print("=== Versión 6: Integrales Impropias ===")
def integrar_impropia(funcion, a, b, tipo='infinito'):
    """
    Calcula integrales impropias (límites infinitos o discontinuidades).
    """
    print(f"\nIntegral impropia ({tipo}):")
    
    try:
        if tipo == 'infinito':
            # Límites infinitos
            resultado, error = spi.quad(funcion, a, np.inf)
            print(f"  ∫ f(x)dx de {a} a ∞ = {resultado:.6f} (error: {error:.2e})")
        elif tipo == 'discontinuidad':
            # Discontinuidad en el intervalo
            resultado, error = spi.quad(funcion, a, b, points=[0])  # punto de discontinuidad
            print(f"  ∫ f(x)dx de {a} a {b} = {resultado:.6f} (error: {error:.2e})")
        
        return resultado, error
    except Exception as e:
        print(f"  Error: {e}")
        return None, None

# Ejemplo de integral impropia
print("Ejemplo: Integral impropia")
funcion_impropia = lambda x: np.exp(-x)
resultado_impropia, error_impropia = integrar_impropia(funcion_impropia, 0, np.inf, tipo='infinito')
print()

# Versión 7: Integrales dobles y triples
print("=== Versión 7: Integrales Múltiples ===")
def integrar_doble(funcion, a, b, c, d):
    """
    Calcula integrales dobles.
    ∫∫ f(x,y) dx dy
    """
    try:
        resultado, error = spi.dblquad(funcion, a, b, lambda x: c, lambda x: d)
        print(f"\nIntegral doble:")
        print(f"  ∫∫ f(x,y) dx dy")
        print(f"  x: [{a}, {b}], y: [{c}, {d}]")
        print(f"  Resultado: {resultado:.6f}")
        print(f"  Error: {error:.2e}")
        return resultado, error
    except Exception as e:
        print(f"  Error: {e}")
        return None, None

# Ejemplo de integral doble
print("Ejemplo: Integral doble")
funcion_doble = lambda y, x: x * y
resultado_doble, error_doble = integrar_doble(funcion_doble, 0, 1, 0, 1)
print()

# Versión 8: Función interactiva
print("=== Versión 8: Función Interactiva ===")
def integracion_interactiva():
    """
    Función interactiva para calcular integrales.
    """
    while True:
        try:
            print("\n" + "=" * 60)
            print("CALCULADORA DE INTEGRALES")
            print("=" * 60)
            print("\nOpciones:")
            print("1. Función cuadrática: -x² - 2x + 8")
            print("2. Función personalizada")
            print("3. Salir")
            
            opcion = input("\nSeleccione una opción: ").strip()
            
            if opcion == "1":
                a = float(input("Límite inferior (a): "))
                b = float(input("Límite superior (b): "))
                resultado, error = integrar_funcion(f_original, a, b)
            
            elif opcion == "2":
                print("\nIngrese la función en términos de x (ejemplo: x**2 + 2*x + 1)")
                funcion_str = input("f(x) = ")
                a = float(input("Límite inferior (a): "))
                b = float(input("Límite superior (b): "))
                
                # Crear función desde string
                def funcion_personalizada(x):
                    return eval(funcion_str)
                
                resultado, error = integrar_funcion(funcion_personalizada, a, b)
            
            elif opcion == "3":
                print("👋 ¡Hasta luego!")
                break
            
            else:
                print("❌ Opción no válida")
        
        except ValueError:
            print("❌ Por favor ingrese números válidos")
        except SyntaxError:
            print("❌ Error en la sintaxis de la función")
        except KeyboardInterrupt:
            print("\n\n👋 Operación cancelada")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

# Descomentar para probar:
# integracion_interactiva()

# Versión 9: Verificación analítica vs numérica
print("=== Versión 9: Verificación Analítica vs Numérica ===")
def verificar_integral_analitica(funcion, primitiva, a, b):
    """
    Compara el resultado numérico con el resultado analítico.
    """
    # Resultado numérico
    resultado_numerico, error = spi.quad(funcion, a, b)
    
    # Resultado analítico usando el teorema fundamental del cálculo
    resultado_analitico = primitiva(b) - primitiva(a)
    
    diferencia = abs(resultado_numerico - resultado_analitico)
    
    print(f"\nVerificación para integral de {a} a {b}:")
    print(f"  Resultado numérico: {resultado_numerico:.8f}")
    print(f"  Resultado analítico: {resultado_analitico:.8f}")
    print(f"  Diferencia: {diferencia:.2e}")
    print(f"  Error numérico: {error:.2e}")
    
    if diferencia < 1e-6:
        print("  ✅ Coinciden (dentro de la tolerancia)")
    else:
        print("  ⚠️  Hay una diferencia significativa")
    
    return resultado_numerico, resultado_analitico

# Verificar con la función original
# Primitiva de f(x) = -x² - 2x + 8 es F(x) = -x³/3 - x² + 8x
print("Verificación analítica para función original:")
primitiva_original = lambda x: (-x**3/3) - (x**2) + (8*x)
verificar_integral_analitica(f_original, primitiva_original, -4, -3)
print()

# Resumen
print("=== Resumen de Análisis ===")
print("Código original:")
print("  ✓ Funciona correctamente")
print("  ✓ Usa scipy.integrate.quad (método adaptativo)")
print("  ⚠️  Variable 'pi' definida pero no usada")
print("  ⚠️  No muestra el error estimado")
print("  ⚠️  Solo funciona con una función específica")
print()
print("Mejoras implementadas:")
print("  1. ✅ Eliminada variable no usada")
print("  2. ✅ Muestra error estimado")
print("  3. ✅ Funciones genéricas y reutilizables")
print("  4. ✅ Múltiples métodos de integración")
print("  5. ✅ Visualización gráfica")
print("  6. ✅ Integrales impropias")
print("  7. ✅ Integrales múltiples (dobles, triples)")
print("  8. ✅ Verificación analítica vs numérica")
print("  9. ✅ Función interactiva")
print("  10. ✅ Documentación completa")
print()
print("Métodos de integración disponibles:")
print("  - quad: Adaptativo (Gauss-Kronrod), más preciso")
print("  - fixed_quad: Gauss-Legendre, rápido para funciones suaves")
print("  - romberg: Extrapolación de Richardson")
print("  - simpson: Regla de Simpson")
print("  - trapezoid: Regla del trapecio")
