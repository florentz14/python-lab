# Archivo: 30_fibonacci.py
# Descripción: Secuencia de Fibonacci

print("=== Secuencia de Fibonacci ===\n")
print("F(0) = 0")
print("F(1) = 1")
print("F(n) = F(n-1) + F(n-2) para n > 1\n")
print("Secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...\n")

# Versión 1: Recursiva básica (ineficiente)
print("=== Versión 1: Recursiva Básica (Ineficiente) ===")
def fibonacci_recursivo_naive(n):
    """
    Calcula el n-ésimo número de Fibonacci usando recursión simple.
    Complejidad: O(2^n) - MUY INEFICIENTE
    No recomendado para valores grandes de n.
    """
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursivo_naive(n - 1) + fibonacci_recursivo_naive(n - 2)

# Ejemplos (solo números pequeños por eficiencia)
print("Ejemplos recursivos (solo números pequeños):")
for n in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    resultado = fibonacci_recursivo_naive(n)
    print(f"  F({n}) = {resultado}")
print()

# Versión 2: Recursiva con memorización (eficiente)
print("=== Versión 2: Recursiva con Memorización (Eficiente) ===")
cache_fibonacci = {0: 0, 1: 1}

def fibonacci_recursivo_memo(n):
    """
    Calcula el n-ésimo número de Fibonacci usando recursión con memorización.
    Complejidad: O(n)
    """
    if n < 0:
        return None
    
    if n in cache_fibonacci:
        return cache_fibonacci[n]
    
    resultado = fibonacci_recursivo_memo(n - 1) + fibonacci_recursivo_memo(n - 2)
    cache_fibonacci[n] = resultado
    return resultado

# Ejemplos
print("Ejemplos recursivos con memorización:")
for n in [0, 1, 5, 10, 20, 30, 40]:
    resultado = fibonacci_recursivo_memo(n)
    print(f"  F({n}) = {resultado}")
print()

# Versión 3: Iterativa (más eficiente)
print("=== Versión 3: Iterativa (Más Eficiente) ===")
def fibonacci_iterativo(n):
    """
    Calcula el n-ésimo número de Fibonacci usando iteración.
    Complejidad: O(n)
    Más eficiente en memoria que la recursiva.
    """
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Ejemplos
print("Ejemplos iterativos:")
for n in [0, 1, 5, 10, 20, 30, 40, 50]:
    resultado = fibonacci_iterativo(n)
    print(f"  F({n}) = {resultado}")
print()

# Versión 4: Generador (eficiente en memoria)
print("=== Versión 4: Generador (Eficiente en Memoria) ===")
def fibonacci_generador(limite=None):
    """
    Genera números de Fibonacci uno a la vez.
    Útil cuando solo necesitas algunos números o no quieres calcular todos.
    """
    a, b = 0, 1
    contador = 0
    
    while limite is None or contador < limite:
        yield a
        a, b = b, a + b
        contador += 1

# Ejemplos con generador
print("Primeros 15 números de Fibonacci (usando generador):")
fib_gen = fibonacci_generador(15)
secuencia = list(fib_gen)
print(f"  {secuencia}")
print()

# Versión 5: Lista completa
print("=== Versión 5: Lista Completa ===")
def fibonacci_lista(n):
    """
    Genera una lista con los primeros n números de Fibonacci.
    """
    if n < 0:
        return []
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    
    fib_list = [0, 1]
    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    
    return fib_list

# Ejemplos
print("Listas de Fibonacci:")
for n in [5, 10, 15]:
    lista = fibonacci_lista(n)
    print(f"  Primeros {n+1} números: {lista}")
print()

# Versión 6: Fórmula de Binet (aproximación)
print("=== Versión 6: Fórmula de Binet (Aproximación) ===")
import math

def fibonacci_binet(n):
    """
    Calcula el n-ésimo número de Fibonacci usando la fórmula de Binet.
    F(n) = (φ^n - ψ^n) / √5
    donde φ = (1 + √5) / 2 (número áureo)
    y ψ = (1 - √5) / 2
    
    Es una aproximación, más precisa para valores grandes de n.
    """
    if n < 0:
        return None
    
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2  # Número áureo
    psi = (1 - sqrt5) / 2
    
    resultado = (phi**n - psi**n) / sqrt5
    return round(resultado)

# Ejemplos
print("Ejemplos con fórmula de Binet:")
for n in [0, 1, 5, 10, 20, 30]:
    resultado = fibonacci_binet(n)
    resultado_exacto = fibonacci_iterativo(n)
    print(f"  F({n}) = {resultado} (exacto: {resultado_exacto})")
print()

# Versión 7: Con validación y límites
print("=== Versión 7: Con Validación y Límites ===")
def fibonacci_seguro(n, limite=1000):
    """
    Calcula Fibonacci con validación y límites.
    """
    if n < 0:
        print("❌ Error: El índice debe ser >= 0")
        return None
    
    if n > limite:
        print(f"⚠️  Advertencia: n={n} es muy grande, puede tardar o causar overflow")
    
    return fibonacci_iterativo(n)

# Versión 8: Comparación de eficiencia
print("=== Versión 8: Comparación de Eficiencia ===")
import time

def comparar_metodos_fibonacci(n, veces=100):
    """
    Compara el tiempo de ejecución de diferentes métodos.
    """
    print(f"\nComparando métodos para F({n}):")
    
    # Limpiar caché
    cache_fibonacci.clear()
    cache_fibonacci.update({0: 0, 1: 1})
    
    # Método 1: Iterativo
    inicio = time.time()
    for _ in range(veces):
        resultado_iterativo = fibonacci_iterativo(n)
    tiempo_iterativo = time.time() - inicio
    
    # Método 2: Recursivo con memo
    inicio = time.time()
    for _ in range(veces):
        cache_fibonacci.clear()
        cache_fibonacci.update({0: 0, 1: 1})
        resultado_memo = fibonacci_recursivo_memo(n)
    tiempo_memo = time.time() - inicio
    
    # Método 3: Binet
    inicio = time.time()
    for _ in range(veces):
        resultado_binet = fibonacci_binet(n)
    tiempo_binet = time.time() - inicio
    
    print(f"  Iterativo: {tiempo_iterativo*1000:.4f} ms ({veces} iteraciones)")
    print(f"  Recursivo con memo: {tiempo_memo*1000:.4f} ms ({veces} iteraciones)")
    print(f"  Binet: {tiempo_binet*1000:.4f} ms ({veces} iteraciones)")
    print(f"  Todos dan el mismo resultado: {resultado_iterativo == resultado_memo == resultado_binet}")

# Comparar para diferentes valores
for n in [10, 20, 30]:
    comparar_metodos_fibonacci(n, veces=100)
print()

# Versión 9: Función interactiva
print("=== Versión 9: Función Interactiva ===")
def fibonacci_interactivo():
    """
    Función interactiva para calcular números de Fibonacci.
    """
    while True:
        try:
            print("\n" + "=" * 50)
            print("CALCULADORA DE FIBONACCI")
            print("=" * 50)
            print("\nOpciones:")
            print("1. Calcular F(n)")
            print("2. Mostrar secuencia hasta n")
            print("3. Salir")
            
            opcion = input("\nSeleccione una opción: ").strip()
            
            if opcion == "1":
                n = int(input("Ingrese el índice n (>= 0): "))
                if n < 0:
                    print("❌ El índice debe ser >= 0")
                    continue
                
                resultado = fibonacci_iterativo(n)
                print(f"\n✅ F({n}) = {resultado}")
            
            elif opcion == "2":
                n = int(input("Ingrese hasta qué índice mostrar (>= 0): "))
                if n < 0:
                    print("❌ El índice debe ser >= 0")
                    continue
                
                if n > 50:
                    respuesta = input(f"⚠️  Mostrar {n+1} números puede ser mucho. ¿Continuar? (s/n): ")
                    if respuesta.lower() != 's':
                        continue
                
                secuencia = fibonacci_lista(n)
                print(f"\nSecuencia de Fibonacci (F(0) a F({n})):")
                for i, valor in enumerate(secuencia):
                    print(f"  F({i}) = {valor}")
            
            elif opcion == "3":
                print("👋 ¡Hasta luego!")
                break
            
            else:
                print("❌ Opción no válida")
        
        except ValueError:
            print("❌ Por favor ingrese un número entero válido")
        except KeyboardInterrupt:
            print("\n\n👋 Operación cancelada")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

# Descomentar para probar:
# fibonacci_interactivo()

# Versión 10: Propiedades matemáticas
print("=== Versión 10: Propiedades de Fibonacci ===")
def propiedades_fibonacci(n=20):
    """
    Muestra algunas propiedades interesantes de la secuencia de Fibonacci.
    """
    fib_list = fibonacci_lista(n)
    
    print(f"\nPropiedades de Fibonacci (primeros {n+1} números):")
    print("=" * 60)
    
    # Suma de los primeros n números
    suma = sum(fib_list)
    print(f"1. Suma de F(0) a F({n}): {suma}")
    print(f"   F({n+2}) - 1 = {fibonacci_iterativo(n+2) - 1}")
    print(f"   Propiedad: Σ F(i) = F(n+2) - 1")
    
    # Número áureo
    if n >= 2:
        ratios = []
        for i in range(2, min(n+1, 15)):
            if fib_list[i-1] != 0:
                ratio = fib_list[i] / fib_list[i-1]
                ratios.append(ratio)
        
        print(f"\n2. Ratio F(n)/F(n-1) (aproxima al número áureo):")
        for i, ratio in enumerate(ratios[:10], 2):
            print(f"   F({i})/F({i-1}) = {ratio:.10f}")
        print(f"   Número áureo φ = {(1 + math.sqrt(5))/2:.10f}")
    
    # Números pares e impares
    pares = [x for x in fib_list if x % 2 == 0]
    impares = [x for x in fib_list if x % 2 == 1]
    print(f"\n3. Números pares: {len(pares)} (F(3k) son pares)")
    print(f"   Números impares: {len(impares)}")
    
    print("=" * 60)

propiedades_fibonacci(20)
print()

# Resumen
print("=== Resumen ===")
print("Métodos para calcular Fibonacci:")
print("  1. Recursivo naive: O(2^n) - MUY INEFICIENTE, solo para aprender")
print("  2. Recursivo con memo: O(n) - Buena, pero usa más memoria")
print("  3. Iterativo: O(n) - RECOMENDADO, eficiente y simple")
print("  4. Generador: O(n) - Útil para generar secuencias grandes")
print("  5. Fórmula de Binet: O(1) - Rápida pero aproximada")
print()
print("Aplicaciones:")
print("  - Modelado de crecimiento de poblaciones")
print("  - Algoritmos de optimización")
print("  - Arte y diseño (proporción áurea)")
print("  - Ciencias de la computación (estructuras de datos)")
