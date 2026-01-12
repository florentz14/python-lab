# Archivo: 29_factorial.py
# Descripción: Cálculo de factorial de un número

import math
import sys

print("=== Cálculo de Factorial ===\n")
print("n! = n × (n-1) × (n-2) × ... × 2 × 1\n")
print("Ejemplo: 5! = 5 × 4 × 3 × 2 × 1 = 120\n")

# Versión 1: Recursiva básica
print("=== Versión 1: Recursiva Básica ===")
def factorial_recursivo(n):
    """
    Calcula el factorial usando recursión.
    Complejidad: O(n)
    """
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)

# Ejemplos
print("Ejemplos recursivos:")
for n in [0, 1, 5, 7, 10]:
    resultado = factorial_recursivo(n)
    print(f"  {n}! = {resultado}")
print()

# Versión 2: Iterativa
print("=== Versión 2: Iterativa ===")
def factorial_iterativo(n):
    """
    Calcula el factorial usando un bucle.
    Complejidad: O(n)
    Más eficiente en memoria que la recursiva.
    """
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Ejemplos
print("Ejemplos iterativos:")
for n in [0, 1, 5, 7, 10]:
    resultado = factorial_iterativo(n)
    print(f"  {n}! = {resultado}")
print()

# Versión 3: Usando math.factorial (más eficiente)
print("=== Versión 3: Usando math.factorial ===")
def factorial_math(n):
    """
    Calcula el factorial usando la biblioteca math.
    Implementación optimizada en C, muy eficiente.
    """
    if n < 0:
        return None
    try:
        return math.factorial(n)
    except ValueError:
        return None

# Ejemplos
print("Ejemplos con math.factorial:")
for n in [0, 1, 5, 7, 10, 20]:
    resultado = factorial_math(n)
    print(f"  {n}! = {resultado}")
print()

# Versión 4: Con validación y límites
print("=== Versión 4: Con Validación y Límites ===")
def factorial_seguro(n, limite_recursion=1000):
    """
    Calcula factorial con validación y límite de recursión.
    """
    if n < 0:
        print("❌ Error: El factorial no está definido para números negativos")
        return None
    
    if n > limite_recursion:
        print(f"⚠️  Advertencia: Número muy grande, usando método iterativo")
        return factorial_iterativo(n)
    
    # Usar math.factorial si está disponible
    try:
        return math.factorial(n)
    except (ValueError, OverflowError):
        # Si falla, usar método iterativo
        return factorial_iterativo(n)

# Pruebas
print("Ejemplos con validación:")
for n in [-1, 0, 5, 100, 170]:
    resultado = factorial_seguro(n)
    if resultado is not None:
        print(f"  {n}! = {resultado}")
    else:
        print(f"  {n}! = Error")
print()

# Versión 5: Con caché (memorización)
print("=== Versión 5: Con Caché (Memorización) ===")
cache_factorial = {}

def factorial_con_cache(n):
    """
    Calcula factorial usando caché para evitar cálculos repetidos.
    """
    if n < 0:
        return None
    
    if n in cache_factorial:
        return cache_factorial[n]
    
    if n == 0 or n == 1:
        cache_factorial[n] = 1
        return 1
    
    resultado = n * factorial_con_cache(n - 1)
    cache_factorial[n] = resultado
    return resultado

# Ejemplos con caché
print("Ejemplos con caché:")
for n in [5, 5, 7, 5, 10]:  # 5 se repite
    resultado = factorial_con_cache(n)
    print(f"  {n}! = {resultado}")
print(f"  Caché: {cache_factorial}")
print()

# Versión 6: Gamma function para números no enteros
print("=== Versión 6: Función Gamma (Extensión) ===")
def factorial_gamma(n):
    """
    Calcula factorial usando la función gamma.
    Permite calcular factorial de números no enteros.
    Γ(n+1) = n!
    """
    if n < 0:
        return None
    try:
        return math.gamma(n + 1)
    except (ValueError, OverflowError):
        return None

print("Ejemplos con función gamma:")
for n in [5, 5.5, 10, 2.5]:
    resultado = factorial_gamma(n)
    if resultado is not None:
        print(f"  {n}! ≈ {resultado:.4f}")
print()

# Versión 7: Comparación de eficiencia
print("=== Versión 7: Comparación de Eficiencia ===")
import time

def comparar_metodos_factorial(n, veces=1000):
    """
    Compara el tiempo de ejecución de diferentes métodos.
    """
    print(f"\nComparando métodos para {n}!:")
    
    # Método 1: Recursivo
    inicio = time.time()
    for _ in range(veces):
        factorial_recursivo(n)
    tiempo_recursivo = time.time() - inicio
    
    # Método 2: Iterativo
    inicio = time.time()
    for _ in range(veces):
        factorial_iterativo(n)
    tiempo_iterativo = time.time() - inicio
    
    # Método 3: math.factorial
    inicio = time.time()
    for _ in range(veces):
        math.factorial(n)
    tiempo_math = time.time() - inicio
    
    print(f"  Recursivo: {tiempo_recursivo*1000:.4f} ms ({veces} iteraciones)")
    print(f"  Iterativo: {tiempo_iterativo*1000:.4f} ms ({veces} iteraciones)")
    print(f"  math.factorial: {tiempo_math*1000:.4f} ms ({veces} iteraciones)")
    
    # Verificar que todos dan el mismo resultado
    r1 = factorial_recursivo(n)
    r2 = factorial_iterativo(n)
    r3 = math.factorial(n)
    print(f"  Todos dan el mismo resultado: {r1 == r2 == r3}")

comparar_metodos_factorial(10, veces=1000)
print()

# Versión 8: Función interactiva
print("=== Versión 8: Función Interactiva ===")
def factorial_interactivo():
    """
    Función interactiva para calcular factoriales.
    """
    while True:
        try:
            print("\n" + "=" * 50)
            print("CALCULADORA DE FACTORIAL")
            print("=" * 50)
            print("\nIngrese un número entero no negativo (o 'salir' para terminar)")
            
            entrada = input("n = ").strip().lower()
            
            if entrada == 'salir':
                print("👋 ¡Hasta luego!")
                break
            
            n = int(entrada)
            
            if n < 0:
                print("❌ Error: El factorial no está definido para números negativos")
                continue
            
            if n > 170:
                print(f"⚠️  Advertencia: {n} es muy grande, el resultado puede ser impreciso")
            
            resultado = factorial_seguro(n)
            
            if resultado is not None:
                print(f"\n✅ {n}! = {resultado}")
                
                # Mostrar cálculo paso a paso para números pequeños
                if n <= 10:
                    pasos = " × ".join(str(i) for i in range(n, 0, -1))
                    print(f"   {n}! = {pasos} = {resultado}")
            else:
                print("❌ Error al calcular el factorial")
        
        except ValueError:
            print("❌ Por favor ingrese un número entero válido")
        except KeyboardInterrupt:
            print("\n\n👋 Operación cancelada")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

# Descomentar para probar:
# factorial_interactivo()

# Versión 9: Tabla de factoriales
print("=== Versión 9: Tabla de Factoriales ===")
def tabla_factoriales(limite=20):
    """
    Genera una tabla de factoriales.
    """
    print(f"\nTabla de Factoriales (0 a {limite}):")
    print("=" * 40)
    print(f"{'n':<5} {'n!':<30}")
    print("-" * 40)
    
    for n in range(limite + 1):
        try:
            resultado = math.factorial(n)
            print(f"{n:<5} {resultado:<30}")
        except OverflowError:
            print(f"{n:<5} {'Muy grande':<30}")
    
    print("=" * 40)

tabla_factoriales(20)
print()

# Resumen
print("=== Resumen ===")
print("Métodos para calcular factorial:")
print("  1. Recursivo: Fácil de entender, pero puede causar stack overflow")
print("  2. Iterativo: Más eficiente en memoria")
print("  3. math.factorial: Más eficiente (implementado en C)")
print("  4. Con caché: Útil para múltiples cálculos")
print("  5. Función Gamma: Extiende factorial a números no enteros")
print()
print("Límites:")
print("  - Python puede manejar factoriales muy grandes (hasta ~170! sin overflow)")
print("  - La recursión tiene límite (sys.getrecursionlimit())")
print("  - math.factorial es la opción más eficiente para uso general")
