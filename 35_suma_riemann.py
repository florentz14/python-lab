# Archivo: 35_suma_riemann.py
# Descripción: Sumas de Riemann para aproximar integrales

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

print("=== Sumas de Riemann ===\n")
print("Aproximación numérica de integrales usando sumas de Riemann\n")

# Versión 1: Original
print("=== Versión 1: Original ===")
def suma_riemann_original():
    """
    Versión original del código para calcular sumas de Riemann.
    """
    # Definir la función a integrar
    def f(x):
        return (-x**2) + ((3*x)/2) + 4
    
    # Definir el intervalo [a, b]
    pi = np.pi  # No se usa
    a = -1.38
    b = 2.88
    
    # Definir el número de subintervalos
    n = 1000
    
    # Calcular el ancho de cada subintervalo
    dx = (b - a) / n
    
    # Calcular la suma de Riemann izquierda
    left_sum = 0
    for i in range(n):
        left_sum += f(a + i*dx)
    
    # Calcular la suma de Riemann superior (derecha)
    upper_sum = 0
    for i in range(1, n+1):
        upper_sum += f(a + i*dx)
    
    # Calcular la suma de Riemann punto medio
    mid_sum = 0
    for i in range(n):
        mid_sum += f(a + (i+0.5)*dx)
    
    # Multiplicar por el ancho del subintervalo
    left_sum *= dx
    upper_sum *= dx
    mid_sum *= dx
    
    # Imprimir los resultados
    print("Suma de Riemann izquierda:", left_sum)
    print("Suma de Riemann superior:", upper_sum)
    print("Suma de Riemann punto medio:", mid_sum)

print("Ejecutando versión original:")
suma_riemann_original()
print()

# Versión 2: Optimizada (vectorizada con NumPy)
print("=== Versión 2: Optimizada (Vectorizada) ===")
def f(x):
    """Función a integrar: -x² + (3x/2) + 4"""
    return (-x**2) + ((3*x)/2) + 4

def suma_riemann_vectorizada(funcion, a, b, n, metodo='punto_medio'):
    """
    Calcula suma de Riemann usando NumPy vectorizado (más eficiente).
    
    Parámetros:
    - funcion: Función a integrar
    - a, b: Límites de integración
    - n: Número de subintervalos
    - metodo: 'izquierda', 'derecha', 'punto_medio'
    
    Retorna:
    - Aproximación de la integral
    """
    dx = (b - a) / n
    
    if metodo == 'izquierda':
        x = np.linspace(a, b - dx, n)
    elif metodo == 'derecha':
        x = np.linspace(a + dx, b, n)
    elif metodo == 'punto_medio':
        x = np.linspace(a + dx/2, b - dx/2, n)
    else:
        raise ValueError("Método debe ser 'izquierda', 'derecha' o 'punto_medio'")
    
    # Evaluar función vectorizada
    valores = funcion(x)
    suma = np.sum(valores)
    
    return suma * dx

# Parámetros del ejemplo
a = -1.38
b = 2.88
n = 1000

print(f"Sumas de Riemann (vectorizadas) para f(x) de {a} a {b} con {n} subintervalos:")
left = suma_riemann_vectorizada(f, a, b, n, 'izquierda')
right = suma_riemann_vectorizada(f, a, b, n, 'derecha')
mid = suma_riemann_vectorizada(f, a, b, n, 'punto_medio')

print(f"  Suma izquierda: {left:.6f}")
print(f"  Suma derecha: {right:.6f}")
print(f"  Suma punto medio: {mid:.6f}")
print()

# Versión 3: Con comparación con valor exacto
print("=== Versión 3: Con Comparación con Valor Exacto ===")
def suma_riemann_con_exacto(funcion, a, b, n, mostrar_detalles=True):
    """
    Calcula sumas de Riemann y compara con el valor exacto.
    """
    # Calcular aproximaciones
    left = suma_riemann_vectorizada(funcion, a, b, n, 'izquierda')
    right = suma_riemann_vectorizada(funcion, a, b, n, 'derecha')
    mid = suma_riemann_vectorizada(funcion, a, b, n, 'punto_medio')
    
    # Calcular valor exacto usando scipy
    valor_exacto, error_exacto = spi.quad(funcion, a, b)
    
    # Calcular errores
    error_left = abs(left - valor_exacto)
    error_right = abs(right - valor_exacto)
    error_mid = abs(mid - valor_exacto)
    
    if mostrar_detalles:
        print(f"\nIntegral de {a} a {b} con {n} subintervalos:")
        print("=" * 60)
        print(f"Suma de Riemann izquierda:  {left:12.6f} (error: {error_left:.2e})")
        print(f"Suma de Riemann derecha:    {right:12.6f} (error: {error_right:.2e})")
        print(f"Suma de Riemann punto medio: {mid:12.6f} (error: {error_mid:.2e})")
        print(f"Valor exacto:                {valor_exacto:12.6f}")
        print("=" * 60)
        print(f"\nMejor aproximación: {'Punto medio' if error_mid < min(error_left, error_right) else 'Izquierda' if error_left < error_right else 'Derecha'}")
    
    return {
        'izquierda': left,
        'derecha': right,
        'punto_medio': mid,
        'exacto': valor_exacto,
        'errores': {'izquierda': error_left, 'derecha': error_right, 'punto_medio': error_mid}
    }

resultados = suma_riemann_con_exacto(f, a, b, n)
print()

# Versión 4: Análisis de convergencia
print("=== Versión 4: Análisis de Convergencia ===")
def analizar_convergencia(funcion, a, b, n_valores=[10, 50, 100, 500, 1000, 5000]):
    """
    Analiza cómo converge la aproximación con diferentes números de subintervalos.
    """
    print(f"\nAnálisis de convergencia de {a} a {b}:")
    print("=" * 70)
    print(f"{'n':<8} {'Izquierda':<15} {'Derecha':<15} {'Punto Medio':<15} {'Error Punto Medio':<15}")
    print("-" * 70)
    
    valor_exacto, _ = spi.quad(funcion, a, b)
    
    for n in n_valores:
        left = suma_riemann_vectorizada(funcion, a, b, n, 'izquierda')
        right = suma_riemann_vectorizada(funcion, a, b, n, 'derecha')
        mid = suma_riemann_vectorizada(funcion, a, b, n, 'punto_medio')
        error_mid = abs(mid - valor_exacto)
        
        print(f"{n:<8} {left:<15.6f} {right:<15.6f} {mid:<15.6f} {error_mid:<15.2e}")
    
    print("-" * 70)
    print(f"{'Exacto':<8} {'-':<15} {'-':<15} {valor_exacto:<15.6f} {'-':<15}")
    print("=" * 70)

analizar_convergencia(f, a, b)
print()

# Versión 5: Visualización gráfica
print("=== Versión 5: Visualización Gráfica ===")
def graficar_suma_riemann(funcion, a, b, n=20, metodo='punto_medio'):
    """
    Grafica la suma de Riemann.
    """
    try:
        dx = (b - a) / n
        x_continuo = np.linspace(a, b, 1000)
        y_continuo = funcion(x_continuo)
        
        # Crear puntos para las barras
        if metodo == 'izquierda':
            x_barras = np.linspace(a, b - dx, n)
            x_etiquetas = x_barras
        elif metodo == 'derecha':
            x_barras = np.linspace(a + dx, b, n)
            x_etiquetas = x_barras
        else:  # punto_medio
            x_barras = np.linspace(a + dx/2, b - dx/2, n)
            x_etiquetas = x_barras
        
        y_barras = funcion(x_barras)
        
        # Crear gráfico
        plt.figure(figsize=(12, 6))
        
        # Graficar función continua
        plt.plot(x_continuo, y_continuo, 'b-', linewidth=2, label='f(x)')
        
        # Graficar barras
        for i in range(n):
            x_inicio = a + i * dx
            x_fin = a + (i + 1) * dx
            plt.bar(x_etiquetas[i], y_barras[i], width=dx, alpha=0.3, 
                   color='green', edgecolor='black', align='center')
            if metodo in ['izquierda', 'derecha']:
                plt.plot([x_inicio, x_fin], [y_barras[i], y_barras[i]], 
                        'r-', linewidth=1)
        
        # Ejes
        plt.axhline(y=0, color='k', linewidth=0.5)
        plt.axvline(x=a, color='r', linestyle='--', linewidth=1, label=f'a = {a}')
        plt.axvline(x=b, color='r', linestyle='--', linewidth=1, label=f'b = {b}')
        
        # Calcular aproximación
        aproximacion = suma_riemann_vectorizada(funcion, a, b, n, metodo)
        
        plt.xlabel('x', fontsize=12)
        plt.ylabel('f(x)', fontsize=12)
        plt.title(f'Suma de Riemann ({metodo.replace("_", " ").title()}) - n={n}\nAproximación: {aproximacion:.6f}', 
                 fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.show()
        
        return aproximacion
    
    except Exception as e:
        print(f"Error al graficar: {e}")
        return None

# Descomentar para graficar:
# print("Graficando suma de Riemann (punto medio, n=20):")
# graficar_suma_riemann(f, a, b, n=20, metodo='punto_medio')
# print()

# Versión 6: Regla del trapecio y Simpson
print("=== Versión 6: Regla del Trapecio y Simpson ===")
def regla_trapecio(funcion, a, b, n):
    """
    Aproximación usando la regla del trapecio.
    """
    dx = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = funcion(x)
    
    # Trapecio: (f(a) + f(b))/2 + sum(f(x_i)) para i=1 a n-1
    suma = (y[0] + y[-1]) / 2 + np.sum(y[1:-1])
    return suma * dx

def regla_simpson(funcion, a, b, n):
    """
    Aproximación usando la regla de Simpson.
    n debe ser par.
    """
    if n % 2 != 0:
        n += 1  # Hacer n par
    
    dx = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = funcion(x)
    
    # Simpson: (dx/3) * [f(a) + f(b) + 4*sum(f(impares)) + 2*sum(f(pares))]
    suma = y[0] + y[-1]
    suma += 4 * np.sum(y[1:-1:2])  # Índices impares
    suma += 2 * np.sum(y[2:-1:2])  # Índices pares (excepto primero y último)
    
    return (dx / 3) * suma

print(f"\nComparación de métodos para integral de {a} a {b} (n={n}):")
valor_exacto, _ = spi.quad(f, a, b)

left = suma_riemann_vectorizada(f, a, b, n, 'izquierda')
right = suma_riemann_vectorizada(f, a, b, n, 'derecha')
mid = suma_riemann_vectorizada(f, a, b, n, 'punto_medio')
trapecio = regla_trapecio(f, a, b, n)
simpson = regla_simpson(f, a, b, n)

print("=" * 70)
print(f"{'Método':<20} {'Aproximación':<20} {'Error':<20}")
print("-" * 70)
print(f"{'Riemann izquierda':<20} {left:<20.6f} {abs(left - valor_exacto):<20.2e}")
print(f"{'Riemann derecha':<20} {right:<20.6f} {abs(right - valor_exacto):<20.2e}")
print(f"{'Riemann punto medio':<20} {mid:<20.6f} {abs(mid - valor_exacto):<20.2e}")
print(f"{'Regla del trapecio':<20} {trapecio:<20.6f} {abs(trapecio - valor_exacto):<20.2e}")
print(f"{'Regla de Simpson':<20} {simpson:<20.6f} {abs(simpson - valor_exacto):<20.2e}")
print("-" * 70)
print(f"{'Valor exacto':<20} {valor_exacto:<20.6f} {'-':<20}")
print("=" * 70)
print()

# Versión 7: Función completa mejorada
print("=== Versión 7: Función Completa Mejorada ===")
def integrar_riemann_completo(funcion, a, b, n=1000, mostrar_detalles=True):
    """
    Función completa que calcula todas las aproximaciones de Riemann.
    """
    resultados = {}
    
    # Sumas de Riemann
    resultados['izquierda'] = suma_riemann_vectorizada(funcion, a, b, n, 'izquierda')
    resultados['derecha'] = suma_riemann_vectorizada(funcion, a, b, n, 'derecha')
    resultados['punto_medio'] = suma_riemann_vectorizada(funcion, a, b, n, 'punto_medio')
    
    # Otras aproximaciones
    resultados['trapecio'] = regla_trapecio(funcion, a, b, n)
    resultados['simpson'] = regla_simpson(funcion, a, b, n)
    
    # Valor exacto
    resultados['exacto'], _ = spi.quad(funcion, a, b)
    
    if mostrar_detalles:
        print(f"Integral aproximada de {a} a {b} (n={n} subintervalos):")
        print("=" * 70)
        for metodo, valor in resultados.items():
            if metodo != 'exacto':
                error = abs(valor - resultados['exacto'])
                print(f"{metodo.capitalize():<15} {valor:12.6f} (error: {error:.2e})")
        print("-" * 70)
        print(f"{'Exacto':<15} {resultados['exacto']:12.6f}")
        print("=" * 70)
    
    return resultados

print("Análisis completo:")
resultados_completos = integrar_riemann_completo(f, a, b, n=1000)
print()

# Resumen
print("=== Resumen de Análisis ===")
print("Código original:")
print("  ✓ Funciona correctamente")
print("  ✓ Implementa tres métodos de Riemann")
print("  ⚠️  Variable 'pi' definida pero no usada")
print("  ⚠️  Usa bucles (puede vectorizarse con NumPy)")
print("  ⚠️  No compara con valor exacto")
print("  ⚠️  No muestra errores de aproximación")
print("  ⚠️  No analiza convergencia")
print()
print("Mejoras implementadas:")
print("  1. ✅ Eliminada variable no usada")
print("  2. ✅ Versión vectorizada con NumPy (más eficiente)")
print("  3. ✅ Comparación con valor exacto")
print("  4. ✅ Cálculo de errores de aproximación")
print("  5. ✅ Análisis de convergencia")
print("  6. ✅ Visualización gráfica")
print("  7. ✅ Regla del trapecio y Simpson")
print("  8. ✅ Función completa mejorada")
print("  9. ✅ Documentación completa")
print()
print("Métodos de aproximación:")
print("  - Riemann izquierda: f(x_i) en el extremo izquierdo")
print("  - Riemann derecha: f(x_i) en el extremo derecho")
print("  - Riemann punto medio: f(x_i) en el centro (más preciso)")
print("  - Regla del trapecio: Promedio de izquierda y derecha")
print("  - Regla de Simpson: Aproximación cuadrática (más precisa)")
