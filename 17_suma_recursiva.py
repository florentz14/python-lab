# Archivo: 17_suma_recursiva.py
# Descripción: Suma recursiva de números naturales (suma de Gauss)

print("=== Suma Recursiva (Suma de Gauss) ===\n")

# Versión 1: Original (con correcciones menores)
print("=== Versión 1: Original (Mejorada) ===")
def suma_recursiva_original(num_items):
    """
    Calcula la suma recursiva: n + (n-1) + (n-2) + ... + 1
    Versión basada en el código original.
    """
    suma = 0
    # Caso base
    if num_items == 1:
        suma = 1
    # Caso general
    else:
        suma = num_items + suma_recursiva_original(num_items - 1)
    return suma

# Ejemplos
for n in [4, 5, 10]:
    resultado = suma_recursiva_original(n)
    print(f"suma_recursiva({n}) = {resultado}")
print()

# Versión 2: Optimizada (caso base mejorado)
print("=== Versión 2: Optimizada (Caso Base Mejorado) ===")
def suma_recursiva_optimizada(num_items):
    """
    Versión optimizada con caso base más eficiente.
    """
    # Caso base: si es 0 o negativo, retornar 0
    if num_items <= 0:
        return 0
    if num_items == 1:
        return 1
    # Caso general
    return num_items + suma_recursiva_optimizada(num_items - 1)

for n in [4, 5, 10]:
    resultado = suma_recursiva_optimizada(n)
    print(f"suma_recursiva({n}) = {resultado}")
print()

# Versión 3: Iterativa (más eficiente)
print("=== Versión 3: Iterativa (Más Eficiente) ===")
def suma_iterativa(num_items):
    """
    Versión iterativa usando un bucle.
    Más eficiente en memoria que la recursiva.
    """
    if num_items <= 0:
        return 0
    
    suma = 0
    for i in range(1, num_items + 1):
        suma += i
    return suma

for n in [4, 5, 10]:
    resultado = suma_iterativa(n)
    print(f"suma_iterativa({n}) = {resultado}")
print()

# Versión 4: Fórmula de Gauss (más eficiente)
print("=== Versión 4: Fórmula de Gauss (O(1)) ===")
def suma_gauss(num_items):
    """
    Usa la fórmula de Gauss: n(n+1)/2
    Complejidad O(1) - la más eficiente.
    """
    if num_items <= 0:
        return 0
    return num_items * (num_items + 1) // 2

for n in [4, 5, 10]:
    resultado = suma_gauss(n)
    print(f"suma_gauss({n}) = {resultado}")
print()

# Versión 5: Con validación correcta de errores
print("=== Versión 5: Con Validación Correcta ===")
def suma_recursiva_con_validacion(num_items):
    """
    Versión con validación correcta de números negativos.
    """
    if num_items < 0:
        raise ValueError("El número debe ser positivo o cero")
    if num_items == 0:
        return 0
    if num_items == 1:
        return 1
    return num_items + suma_recursiva_con_validacion(num_items - 1)

def run_mejorado():
    """
    Versión mejorada del run() con manejo correcto de errores.
    """
    while True:
        try:
            numero = int(input('Ingrese un número positivo (o 0 para salir): '))
            if numero < 0:
                print('El número debe ser positivo o cero')
                continue
            if numero == 0:
                print('Saliendo...')
                break
            resultado = suma_recursiva_con_validacion(numero)
            print(f'La suma es: {resultado}')
        except ValueError as e:
            print(f'Error: {e}. Por favor ingrese un número entero válido.')
        except RecursionError:
            print('Error: Número demasiado grande para recursión. Use la versión iterativa.')
            break
        except KeyboardInterrupt:
            print('\nSaliendo...')
            break

# Descomentar para probar interactivamente:
# run_mejorado()

# Versión 6: Con límite de recursión seguro
print("=== Versión 6: Con Límite de Recursión Seguro ===")
import sys

def suma_recursiva_segura(num_items, limite=1000):
    """
    Versión con límite de recursión para evitar stack overflow.
    """
    if num_items < 0:
        raise ValueError("El número debe ser positivo o cero")
    if num_items > limite:
        raise ValueError(f"Número demasiado grande. Use la versión iterativa o fórmula de Gauss.")
    if num_items == 0:
        return 0
    if num_items == 1:
        return 1
    return num_items + suma_recursiva_segura(num_items - 1, limite)

try:
    resultado = suma_recursiva_segura(100)
    print(f"suma_recursiva_segura(100) = {resultado}")
except ValueError as e:
    print(f"Error: {e}")
print()

# Versión 7: Comparación visual del proceso
print("=== Versión 7: Visualización del Proceso Recursivo ===")
def suma_recursiva_visual(num_items, nivel=0):
    """
    Versión que muestra visualmente el proceso recursivo.
    """
    indentacion = "  " * nivel
    print(f"{indentacion}Llamando suma_recursiva({num_items})")
    
    if num_items <= 0:
        print(f"{indentacion}  Caso base: retornando 0")
        return 0
    if num_items == 1:
        print(f"{indentacion}  Caso base: retornando 1")
        return 1
    
    resultado_parcial = suma_recursiva_visual(num_items - 1, nivel + 1)
    resultado = num_items + resultado_parcial
    print(f"{indentacion}  {num_items} + suma_recursiva({num_items-1}) = {num_items} + {resultado_parcial} = {resultado}")
    return resultado

print("Proceso recursivo para n=4:")
suma_recursiva_visual(4)
print()

# Versión 8: Suma con rango personalizado
print("=== Versión 8: Suma con Rango Personalizado ===")
def suma_rango(inicio, fin):
    """
    Suma todos los números desde inicio hasta fin (inclusive).
    """
    if inicio > fin:
        return 0
    if inicio == fin:
        return inicio
    # Usar fórmula de Gauss para el rango
    suma_hasta_fin = fin * (fin + 1) // 2
    suma_hasta_inicio_menos_uno = (inicio - 1) * inicio // 2 if inicio > 0 else 0
    return suma_hasta_fin - suma_hasta_inicio_menos_uno

print(f"Suma del 5 al 10: {suma_rango(5, 10)}")
print(f"Suma del 1 al 100: {suma_rango(1, 100)}")
print()

# Versión 9: Comparación de eficiencia
print("=== Versión 9: Comparación de Eficiencia ===")
import time

def comparar_metodos(n):
    """
    Compara el tiempo de ejecución de diferentes métodos.
    """
    print(f"\nComparando métodos para n={n}:")
    
    # Método 1: Recursivo
    inicio = time.time()
    try:
        resultado1 = suma_recursiva_optimizada(n)
        tiempo1 = time.time() - inicio
        print(f"  Recursivo: {resultado1} en {tiempo1*1000:.4f} ms")
    except RecursionError:
        print(f"  Recursivo: Error - número demasiado grande")
        tiempo1 = float('inf')
    
    # Método 2: Iterativo
    inicio = time.time()
    resultado2 = suma_iterativa(n)
    tiempo2 = time.time() - inicio
    print(f"  Iterativo: {resultado2} en {tiempo2*1000:.4f} ms")
    
    # Método 3: Gauss
    inicio = time.time()
    resultado3 = suma_gauss(n)
    tiempo3 = time.time() - inicio
    print(f"  Gauss: {resultado3} en {tiempo3*1000:.4f} ms")
    
    print(f"  Todos dan el mismo resultado: {resultado2 == resultado3}")

comparar_metodos(100)
comparar_metodos(1000)
print()

# Versión 10: Ejemplos prácticos
print("=== Versión 10: Ejemplos Prácticos ===")
print("Fórmula: Suma de 1 a n = n(n+1)/2")
print("\nEjemplos:")
for n in [1, 4, 5, 10, 100]:
    resultado_gauss = suma_gauss(n)
    resultado_iterativo = suma_iterativa(n)
    print(f"  n={n:3d}: {resultado_gauss:6d} (Gauss) = {resultado_iterativo:6d} (Iterativo)")

print("\nVerificación de la fórmula:")
print("  n=4: 4(4+1)/2 = 4*5/2 = 20/2 = 10 ✓")
print("  n=10: 10(10+1)/2 = 10*11/2 = 110/2 = 55 ✓")
print()

# Resumen de problemas encontrados y mejoras
print("=== Resumen de Problemas y Mejoras ===")
print("Problemas en el código original:")
print("  1. RecursionError no se lanza por números negativos")
print("  2. No valida correctamente números negativos")
print("  3. El caso base podría simplificarse")
print("  4. Falta manejo de KeyboardInterrupt")
print("  5. No hay opción clara para salir del bucle")
print()
print("Mejoras implementadas:")
print("  1. Validación correcta con ValueError para números negativos")
print("  2. Versión iterativa (más eficiente en memoria)")
print("  3. Fórmula de Gauss (complejidad O(1))")
print("  4. Manejo correcto de errores")
print("  5. Límite de recursión seguro")
print("  6. Visualización del proceso recursivo")
print("  7. Comparación de eficiencia entre métodos")
print("  8. Versión con rango personalizado")
