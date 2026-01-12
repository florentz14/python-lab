# Archivo: 14_raiz_cuadrada.py
# Descripción: Encontrar la raíz cuadrada de un número

import math

print("=== Encontrar Raíz Cuadrada ===\n")

# Versión 1: Original (con prints en el bucle)
print("=== Versión 1: Original (con prints en bucle) ===")
def raiz_cuadrada_original(objetivo):
    """
    Encuentra la raíz cuadrada exacta de un número.
    Versión original que imprime cada iteración.
    """
    respuesta = 0
    
    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1
    
    if respuesta**2 == objetivo:
        print(f'La raíz cuadrada de {objetivo} es {respuesta}')
        return respuesta
    else:
        print(f'{objetivo} no tiene una raíz cuadrada exacta')
        return None

# Ejemplo (comentado para no mostrar todos los prints)
# resultado = raiz_cuadrada_original(16)
print("Nota: Esta versión imprime cada número en el bucle\n")

# Versión 2: Optimizada (sin prints innecesarios)
print("=== Versión 2: Optimizada (sin prints en bucle) ===")
def raiz_cuadrada_optimizada(objetivo):
    """
    Versión optimizada sin prints en el bucle.
    Más eficiente y limpia.
    """
    if objetivo < 0:
        return None
    
    respuesta = 0
    
    while respuesta**2 < objetivo:
        respuesta += 1
    
    if respuesta**2 == objetivo:
        print(f'La raíz cuadrada de {objetivo} es {respuesta}')
        return respuesta
    else:
        print(f'{objetivo} no tiene una raíz cuadrada exacta')
        return None

# Ejemplos
numeros = [16, 25, 36, 49, 30]
for num in numeros:
    print(f"\nProbando con {num}:")
    raiz_cuadrada_optimizada(num)

print()

# Versión 3: Con entrada de usuario (mejorada)
print("=== Versión 3: Con Entrada de Usuario ===")
def raiz_cuadrada_input():
    """
    Versión interactiva mejorada con manejo de errores.
    """
    try:
        objetivo = int(input('Escoge un entero: '))
        
        if objetivo < 0:
            print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
            return None
        
        respuesta = 0
        while respuesta**2 < objetivo:
            respuesta += 1
        
        if respuesta**2 == objetivo:
            print(f'La raíz cuadrada de {objetivo} es {respuesta}')
            return respuesta
        else:
            print(f'{objetivo} no tiene una raíz cuadrada exacta')
            return None
    except ValueError:
        print("Error: Por favor ingresa un número entero válido.")
        return None

# Descomentar para probar interactivamente:
# raiz_cuadrada_input()

# Versión 4: Usando math.sqrt()
print("=== Versión 4: Usando math.sqrt() ===")
def raiz_cuadrada_math(objetivo):
    """
    Versión usando la función math.sqrt().
    Más eficiente y precisa.
    """
    if objetivo < 0:
        return None
    
    raiz = math.sqrt(objetivo)
    
    # Verificar si es un número entero
    if raiz == int(raiz):
        print(f'La raíz cuadrada de {objetivo} es {int(raiz)}')
        return int(raiz)
    else:
        print(f'{objetivo} no tiene una raíz cuadrada exacta (raíz aproximada: {raiz:.2f})')
        return None

for num in [16, 25, 30]:
    print(f"\nProbando con {num}:")
    raiz_cuadrada_math(num)

print()

# Versión 5: Método de búsqueda binaria (más eficiente)
print("=== Versión 5: Búsqueda Binaria (Más Eficiente) ===")
def raiz_cuadrada_binaria(objetivo):
    """
    Encuentra la raíz cuadrada usando búsqueda binaria.
    Mucho más eficiente para números grandes.
    """
    if objetivo < 0:
        return None
    if objetivo == 0:
        return 0
    if objetivo == 1:
        return 1
    
    izquierda = 0
    derecha = objetivo
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        cuadrado = medio * medio
        
        if cuadrado == objetivo:
            print(f'La raíz cuadrada de {objetivo} es {medio}')
            return medio
        elif cuadrado < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    print(f'{objetivo} no tiene una raíz cuadrada exacta')
    return None

for num in [16, 25, 100, 144]:
    print(f"\nProbando con {num}:")
    raiz_cuadrada_binaria(num)

print()

# Versión 6: Con aproximación decimal
print("=== Versión 6: Con Aproximación Decimal ===")
def raiz_cuadrada_aproximada(objetivo, precision=0.001):
    """
    Encuentra la raíz cuadrada con aproximación decimal.
    """
    if objetivo < 0:
        return None
    
    if objetivo == 0:
        return 0.0
    
    respuesta = 0.0
    incremento = precision
    
    while respuesta * respuesta < objetivo:
        respuesta += incremento
    
    if abs(respuesta * respuesta - objetivo) < precision:
        print(f'La raíz cuadrada aproximada de {objetivo} es {respuesta:.3f}')
        return respuesta
    else:
        raiz_exacta = math.sqrt(objetivo)
        print(f'La raíz cuadrada aproximada de {objetivo} es {raiz_exacta:.3f}')
        return raiz_exacta

for num in [16, 25, 30]:
    print(f"\nProbando con {num}:")
    raiz_cuadrada_aproximada(num)

print()

# Versión 7: Encontrar todas las raíces cuadradas en un rango
print("=== Versión 7: Encontrar Raíces en un Rango ===")
def encontrar_raices_cuadradas_en_rango(limite_superior):
    """
    Encuentra todos los números que tienen raíz cuadrada exacta
    hasta un límite superior.
    """
    raices_encontradas = []
    
    for i in range(limite_superior + 1):
        raiz = math.sqrt(i)
        if raiz == int(raiz):
            raices_encontradas.append((i, int(raiz)))
    
    print(f"Números con raíz cuadrada exacta hasta {limite_superior}:")
    for numero, raiz in raices_encontradas:
        print(f"  {numero} = {raiz}²")
    
    return raices_encontradas

encontrar_raices_cuadradas_en_rango(50)

print()

# Versión 8: Comparación de eficiencia
print("=== Versión 8: Comparación de Métodos ===")
def comparar_metodos(objetivo):
    """
    Compara los diferentes métodos para encontrar la raíz cuadrada.
    """
    import time
    
    print(f"\nComparando métodos para {objetivo}:")
    
    # Método 1: Bucle simple
    inicio = time.time()
    respuesta1 = 0
    while respuesta1**2 < objetivo:
        respuesta1 += 1
    tiempo1 = time.time() - inicio
    
    # Método 2: math.sqrt()
    inicio = time.time()
    raiz2 = math.sqrt(objetivo)
    tiempo2 = time.time() - inicio
    
    # Método 3: Búsqueda binaria
    inicio = time.time()
    if objetivo >= 0:
        izq, der = 0, objetivo
        respuesta3 = 0
        while izq <= der:
            medio = (izq + der) // 2
            if medio * medio == objetivo:
                respuesta3 = medio
                break
            elif medio * medio < objetivo:
                izq = medio + 1
            else:
                der = medio - 1
    tiempo3 = time.time() - inicio
    
    print(f"  Bucle simple: {tiempo1*1000:.4f} ms")
    print(f"  math.sqrt(): {tiempo2*1000:.4f} ms")
    print(f"  Búsqueda binaria: {tiempo3*1000:.4f} ms")

comparar_metodos(10000)

print()

# Resumen de mejoras
print("=== Resumen de Mejoras ===")
print("Mejoras implementadas:")
print("  1. Eliminación de prints innecesarios en el bucle")
print("  2. Manejo de números negativos")
print("  3. Uso de math.sqrt() para mayor eficiencia")
print("  4. Búsqueda binaria para números grandes")
print("  5. Versión con aproximación decimal")
print("  6. Manejo de errores en entrada de usuario")
print("  7. Comparación de métodos de eficiencia")
