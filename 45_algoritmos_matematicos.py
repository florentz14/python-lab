# Archivo: 45_algoritmos_matematicos.py
# Descripción: Algoritmos Matemáticos

print("=== Algoritmos Matemáticos ===\n")

# =============================================================================
# 1. TRIÁNGULO DE PASCAL
# =============================================================================
print("=== 1. Triángulo de Pascal ===")

def triangulo_pascal_filas(n):
    """
    Genera las primeras n filas del Triángulo de Pascal.
    Cada número es la suma de los dos números directamente arriba.
    Complejidad: O(n²)
    """
    triangulo = []
    
    for i in range(n):
        fila = [1] * (i + 1)
        
        # Llenar valores intermedios
        for j in range(1, i):
            fila[j] = triangulo[i-1][j-1] + triangulo[i-1][j]
        
        triangulo.append(fila)
    
    return triangulo

def triangulo_pascal_imprimir(n):
    """Imprime el Triángulo de Pascal de forma visual."""
    triangulo = triangulo_pascal_filas(n)
    
    # Encontrar el ancho máximo para centrar
    ancho_maximo = len(' '.join(map(str, triangulo[-1])))
    
    for fila in triangulo:
        fila_str = ' '.join(map(str, fila))
        print(fila_str.center(ancho_maximo))

def triangulo_pascal_coeficiente(n, k):
    """
    Calcula el coeficiente binomial C(n, k) usando el Triángulo de Pascal.
    Equivale a n! / (k! * (n-k)!)
    """
    if k > n or k < 0:
        return 0
    
    # Usar propiedad: C(n, k) = C(n, n-k)
    if k > n - k:
        k = n - k
    
    resultado = 1
    for i in range(k):
        resultado = resultado * (n - i) // (i + 1)
    
    return resultado

def triangulo_pascal_fila_n(n):
    """Genera solo la fila n del Triángulo de Pascal (optimizado)."""
    fila = [1]
    
    for k in range(n):
        siguiente = fila[k] * (n - k) // (k + 1)
        fila.append(siguiente)
    
    return fila

# Ejemplo
print("Triángulo de Pascal (10 filas):")
triangulo_pascal_imprimir(10)

print(f"\nCoeficiente binomial C(5, 2) = {triangulo_pascal_coeficiente(5, 2)}")
print(f"Fila 5 del Triángulo de Pascal: {triangulo_pascal_fila_n(5)}")
print()

# =============================================================================
# 2. ALGORITMO DE EUCLIDES (Máximo Común Divisor)
# =============================================================================
print("=== 2. Algoritmo de Euclides (MCD) ===")

def euclides_mcd(a, b):
    """
    Calcula el Máximo Común Divisor usando algoritmo de Euclides.
    Complejidad: O(log min(a, b))
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)

def euclides_mcd_recursivo(a, b):
    """Versión recursiva del algoritmo de Euclides."""
    if b == 0:
        return abs(a)
    return euclides_mcd_recursivo(b, a % b)

def euclides_mcm(a, b):
    """
    Calcula el Mínimo Común Múltiplo usando MCD.
    MCM(a, b) = |a * b| / MCD(a, b)
    """
    mcd = euclides_mcd(a, b)
    return abs(a * b) // mcd if mcd != 0 else 0

def euclides_extendido(a, b):
    """
    Algoritmo de Euclides extendido.
    Encuentra x, y tal que: a*x + b*y = MCD(a, b)
    Retorna: (mcd, x, y)
    """
    if a == 0:
        return abs(b), 0, 1 if b >= 0 else -1
    
    mcd, x1, y1 = euclides_extendido(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    
    return mcd, x, y

# Ejemplo
a_euclides = 48
b_euclides = 18

print(f"a = {a_euclides}, b = {b_euclides}")
print(f"MCD (iterativo): {euclides_mcd(a_euclides, b_euclides)}")
print(f"MCD (recursivo): {euclides_mcd_recursivo(a_euclides, b_euclides)}")
print(f"MCM: {euclides_mcm(a_euclides, b_euclides)}")

mcd_ext, x, y = euclides_extendido(a_euclides, b_euclides)
print(f"Euclides extendido: {mcd_ext} = {a_euclides}*{x} + {b_euclides}*{y}")
print()

# =============================================================================
# 3. CRIBA DE ERATÓSTENES (Números Primos)
# =============================================================================
print("=== 3. Criba de Eratóstenes ===")

def criba_eratostenes(n):
    """
    Encuentra todos los números primos hasta n usando la Criba de Eratóstenes.
    Complejidad: O(n log log n)
    """
    if n < 2:
        return []
    
    # Inicializar: todos son primos
    es_primo = [True] * (n + 1)
    es_primo[0] = es_primo[1] = False
    
    # Criba
    for i in range(2, int(n**0.5) + 1):
        if es_primo[i]:
            # Marcar múltiplos de i como no primos
            for j in range(i * i, n + 1, i):
                es_primo[j] = False
    
    # Recolectar primos
    primos = [i for i in range(2, n + 1) if es_primo[i]]
    return primos

def es_primo_optimizado(n):
    """
    Verifica si un número es primo (optimizado).
    Complejidad: O(√n)
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

# Ejemplo
limite_criba = 50
primos = criba_eratostenes(limite_criba)
print(f"Números primos hasta {limite_criba}: {primos}")
print(f"Total: {len(primos)} primos")

numero_test = 97
print(f"\n¿{numero_test} es primo? {es_primo_optimizado(numero_test)}")
print()

# =============================================================================
# 4. EXPONENCIACIÓN MODULAR (Fast Exponentiation)
# =============================================================================
print("=== 4. Exponenciación Modular Rápida ===")

def exponenciacion_modular(base, exponente, modulo):
    """
    Calcula (base^exponente) mod modulo de forma eficiente.
    Complejidad: O(log exponente)
    """
    resultado = 1
    base = base % modulo
    
    while exponente > 0:
        if exponente % 2 == 1:
            resultado = (resultado * base) % modulo
        exponente = exponente >> 1  # Dividir por 2
        base = (base * base) % modulo
    
    return resultado

# Ejemplo
base_exp = 3
exp_exp = 100
mod_exp = 7

resultado = exponenciacion_modular(base_exp, exp_exp, mod_exp)
print(f"({base_exp}^{exp_exp}) mod {mod_exp} = {resultado}")
print(f"Verificación: {pow(base_exp, exp_exp, mod_exp)} (función built-in)")
print()

# =============================================================================
# 5. NÚMEROS DE FIBONACCI (Fórmula de Binet y Matriz)
# =============================================================================
print("=== 5. Números de Fibonacci (Métodos Matemáticos) ===")

import math

def fibonacci_binet(n):
    """
    Calcula el n-ésimo número de Fibonacci usando la fórmula de Binet.
    Complejidad: O(1) (pero con errores de precisión para n grandes)
    """
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return int((phi**n - psi**n) / math.sqrt(5))

def fibonacci_matriz(n):
    """
    Calcula el n-ésimo número de Fibonacci usando exponenciación de matrices.
    Complejidad: O(log n)
    """
    def multiplicar_matrices(A, B):
        return [
            [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
        ]
    
    def potencia_matriz_fib(M, n):
        if n == 1:
            return M
        if n % 2 == 0:
            mitad = potencia_matriz_fib(M, n // 2)
            return multiplicar_matrices(mitad, mitad)
        else:
            return multiplicar_matrices(M, potencia_matriz_fib(M, n - 1))
    
    if n <= 1:
        return n
    
    matriz_base = [[1, 1], [1, 0]]
    matriz_potencia = potencia_matriz_fib(matriz_base, n)
    return matriz_potencia[0][1]

# Ejemplo
n_fib_mate = 10
print(f"Fibonacci({n_fib_mate}):")
print(f"  Fórmula de Binet: {fibonacci_binet(n_fib_mate)}")
print(f"  Matriz: {fibonacci_matriz(n_fib_mate)}")
print()

# =============================================================================
# 6. FACTORIZACIÓN DE NÚMEROS
# =============================================================================
print("=== 6. Factorización de Números ===")

def factorizar(n):
    """
    Factoriza un número en sus factores primos.
    Complejidad: O(√n)
    """
    factores = []
    divisor = 2
    
    while divisor * divisor <= n:
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 1
    
    if n > 1:
        factores.append(n)
    
    return factores

def factores_unicos(n):
    """Obtiene los factores únicos de un número."""
    return list(set(factorizar(n)))

def contar_divisores(n):
    """Cuenta el número de divisores de n."""
    factores = factorizar(n)
    conteo = {}
    for factor in factores:
        conteo[factor] = conteo.get(factor, 0) + 1
    
    divisores = 1
    for exponente in conteo.values():
        divisores *= (exponente + 1)
    
    return divisores

# Ejemplo
numero_factorizar = 60
factores = factorizar(numero_factorizar)
factores_uni = factores_unicos(numero_factorizar)
divisores = contar_divisores(numero_factorizar)

print(f"Número: {numero_factorizar}")
print(f"Factores primos: {factores}")
print(f"Factores únicos: {factores_uni}")
print(f"Número de divisores: {divisores}")
print()

# =============================================================================
# 7. CONVERSIÓN DE BASES NUMÉRICAS
# =============================================================================
print("=== 7. Conversión de Bases Numéricas ===")

def convertir_base(n, base_destino, base_origen=10):
    """
    Convierte un número de base_origen a base_destino.
    """
    # Convertir a decimal primero
    if base_origen != 10:
        n_decimal = 0
        n_str = str(n)
        for i, digito in enumerate(reversed(n_str)):
            n_decimal += int(digito) * (base_origen ** i)
        n = n_decimal
    
    # Convertir de decimal a base_destino
    if base_destino == 10:
        return str(n)
    
    resultado = []
    n_actual = n
    
    while n_actual > 0:
        resto = n_actual % base_destino
        if resto < 10:
            resultado.append(str(resto))
        else:
            resultado.append(chr(ord('A') + resto - 10))
        n_actual //= base_destino
    
    return ''.join(reversed(resultado))

# Ejemplo
numero_conv = 255
print(f"Número en decimal: {numero_conv}")
print(f"Binario: {convertir_base(numero_conv, 2)}")
print(f"Octal: {convertir_base(numero_conv, 8)}")
print(f"Hexadecimal: {convertir_base(numero_conv, 16)}")
print()

# Resumen
print("=== RESUMEN ===")
print("""
Algoritmos matemáticos implementados:

1. Triángulo de Pascal:
   - Generación de filas
   - Coeficientes binomiales
   - Complejidad: O(n²)

2. Algoritmo de Euclides:
   - Máximo Común Divisor (MCD)
   - Mínimo Común Múltiplo (MCM)
   - Euclides extendido
   - Complejidad: O(log min(a, b))

3. Criba de Eratóstenes:
   - Encuentra todos los primos hasta n
   - Complejidad: O(n log log n)

4. Exponenciación Modular:
   - Potenciación rápida con módulo
   - Complejidad: O(log exponente)

5. Números de Fibonacci:
   - Fórmula de Binet
   - Exponenciación de matrices
   - Complejidad: O(log n)

6. Factorización:
   - Factores primos
   - Conteo de divisores
   - Complejidad: O(√n)

7. Conversión de Bases:
   - Decimal a cualquier base
   - Entre bases diferentes

Aplicaciones:
- Criptografía
- Teoría de números
- Combinatoria
- Álgebra computacional
""")
