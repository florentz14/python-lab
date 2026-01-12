# Archivo: 32_potenciacion.py
# Descripción: Potenciación matemática - Calcular base^exponente

print("=== Potenciación Matemática ===\n")
print("Calcular base^exponente\n")

# Versión 1: Original
print("=== Versión 1: Original ===")
def potenciacion_original(base, exponente):
    """
    Versión original del código para calcular potencias.
    """
    acumular = 1
    for i in range(exponente):
        acumular = acumular * base
    return acumular

# Ejemplos
print("Ejemplos versión original:")
for base, exp in [(2, 3), (5, 2), (3, 4)]:
    resultado = potenciacion_original(base, exp)
    print(f"  {base}^{exp} = {resultado}")
print()

# Versión 2: Optimizada (usando operador **)
print("=== Versión 2: Optimizada (operador **) ===")
def potenciacion_operador(base, exponente):
    """
    Versión usando el operador ** de Python.
    Más eficiente y conciso.
    """
    return base ** exponente

print("Ejemplos con operador **:")
for base, exp in [(2, 3), (5, 2), (3, 4), (2, 10)]:
    resultado = potenciacion_operador(base, exp)
    print(f"  {base}^{exp} = {resultado}")
print()

# Versión 3: Con validación y manejo de casos especiales
print("=== Versión 3: Con Validación ===")
def potenciacion_segura(base, exponente):
    """
    Calcula potencia con validación y manejo de casos especiales.
    """
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    
    # Caso base: cualquier número elevado a 1 es el mismo número
    if exponente == 1:
        return base
    
    # Exponente negativo
    if exponente < 0:
        return 1 / (base ** abs(exponente))
    
    # Caso general
    return base ** exponente

print("Ejemplos con validación:")
for base, exp in [(2, 0), (5, 1), (2, -3), (3, 4)]:
    resultado = potenciacion_segura(base, exp)
    print(f"  {base}^{exp} = {resultado}")
print()

# Versión 4: Exponenciación rápida (algoritmo eficiente)
print("=== Versión 4: Exponenciación Rápida (Binary Exponentiation) ===")
def potenciacion_rapida(base, exponente):
    """
    Algoritmo de exponenciación rápida usando divide y vencerás.
    Complejidad: O(log n) en lugar de O(n)
    Eficiente para exponentes grandes.
    """
    if exponente == 0:
        return 1
    if exponente < 0:
        return 1 / potenciacion_rapida(base, -exponente)
    if exponente == 1:
        return base
    
    # Si el exponente es par: base^n = (base^(n/2))^2
    # Si el exponente es impar: base^n = base * base^(n-1)
    if exponente % 2 == 0:
        mitad = potenciacion_rapida(base, exponente // 2)
        return mitad * mitad
    else:
        return base * potenciacion_rapida(base, exponente - 1)

print("Ejemplos exponenciación rápida:")
for base, exp in [(2, 8), (3, 7), (5, 10), (2, 20)]:
    resultado = potenciacion_rapida(base, exp)
    resultado_operador = base ** exp
    print(f"  {base}^{exp} = {resultado} (verificación: {resultado_operador})")
print()

# Versión 5: Exponenciación rápida iterativa
print("=== Versión 5: Exponenciación Rápida Iterativa ===")
def potenciacion_rapida_iterativa(base, exponente):
    """
    Versión iterativa de exponenciación rápida.
    Más eficiente en memoria que la recursiva.
    """
    if exponente < 0:
        return 1 / potenciacion_rapida_iterativa(base, -exponente)
    
    resultado = 1
    potencia_actual = base
    
    while exponente > 0:
        if exponente % 2 == 1:
            resultado *= potencia_actual
        potencia_actual *= potencia_actual
        exponente //= 2
    
    return resultado

print("Ejemplos exponenciación rápida iterativa:")
for base, exp in [(2, 8), (3, 7), (5, 10)]:
    resultado = potenciacion_rapida_iterativa(base, exp)
    print(f"  {base}^{exp} = {resultado}")
print()

# Versión 6: Usando math.pow y pow()
print("=== Versión 6: Usando math.pow y pow() ===")
import math

def potenciacion_math(base, exponente):
    """
    Usando math.pow (retorna float) y pow() (built-in).
    """
    resultado_math = math.pow(base, exponente)
    resultado_builtin = pow(base, exponente)
    return resultado_math, resultado_builtin

print("Comparación math.pow vs pow():")
for base, exp in [(2, 3), (5, 2), (3, 4)]:
    resultado_math, resultado_builtin = potenciacion_math(base, exp)
    print(f"  {base}^{exp}:")
    print(f"    math.pow: {resultado_math}")
    print(f"    pow(): {resultado_builtin}")
print()

# Versión 7: Con módulo (potenciación modular)
print("=== Versión 7: Potenciación Modular ===")
def potenciacion_modular(base, exponente, modulo):
    """
    Calcula (base^exponente) mod modulo de manera eficiente.
    Útil en criptografía y algoritmos.
    """
    if modulo == 0:
        raise ValueError("El módulo no puede ser cero")
    
    resultado = 1
    base = base % modulo
    
    while exponente > 0:
        if exponente % 2 == 1:
            resultado = (resultado * base) % modulo
        exponente = exponente >> 1
        base = (base * base) % modulo
    
    return resultado

print("Ejemplos de potenciación modular:")
for base, exp, mod in [(2, 10, 1000), (3, 7, 13), (5, 8, 17)]:
    resultado = potenciacion_modular(base, exp, mod)
    resultado_normal = (base ** exp) % mod
    print(f"  {base}^{exp} mod {mod} = {resultado} (verificación: {resultado_normal})")
print()

# Versión 8: Comparación de eficiencia
print("=== Versión 8: Comparación de Eficiencia ===")
import time

def comparar_metodos_potencia(base, exponente, veces=1000):
    """
    Compara el tiempo de ejecución de diferentes métodos.
    """
    print(f"\nComparando métodos para {base}^{exponente}:")
    
    # Método 1: Bucle original
    inicio = time.time()
    for _ in range(veces):
        resultado1 = potenciacion_original(base, exponente)
    tiempo_bucle = time.time() - inicio
    
    # Método 2: Operador **
    inicio = time.time()
    for _ in range(veces):
        resultado2 = base ** exponente
    tiempo_operador = time.time() - inicio
    
    # Método 3: Exponenciación rápida
    inicio = time.time()
    for _ in range(veces):
        resultado3 = potenciacion_rapida_iterativa(base, exponente)
    tiempo_rapida = time.time() - inicio
    
    # Método 4: pow()
    inicio = time.time()
    for _ in range(veces):
        resultado4 = pow(base, exponente)
    tiempo_pow = time.time() - inicio
    
    print(f"  Bucle original: {tiempo_bucle*1000:.4f} ms ({veces} iteraciones)")
    print(f"  Operador **: {tiempo_operador*1000:.4f} ms ({veces} iteraciones)")
    print(f"  Exponenciación rápida: {tiempo_rapida*1000:.4f} ms ({veces} iteraciones)")
    print(f"  pow(): {tiempo_pow*1000:.4f} ms ({veces} iteraciones)")
    
    # Verificar que todos dan el mismo resultado
    todos_iguales = (resultado1 == resultado2 == resultado3 == resultado4)
    print(f"  Todos dan el mismo resultado: {todos_iguales}")

comparar_metodos_potencia(2, 20, veces=1000)
comparar_metodos_potencia(3, 15, veces=1000)
print()

# Versión 9: Función interactiva mejorada
print("=== Versión 9: Función Interactiva Mejorada ===")
def potenciacion_interactiva():
    """
    Función interactiva mejorada para calcular potencias.
    """
    while True:
        try:
            print("\n" + "=" * 50)
            print("CALCULADORA DE POTENCIAS")
            print("=" * 50)
            
            base = float(input("Ingrese la base: "))
            exponente = float(input("Ingrese el exponente: "))
            
            resultado = base ** exponente
            
            print(f"\n✅ {base}^{exponente} = {resultado}")
            
            # Mostrar cálculo paso a paso para exponentes pequeños
            if exponente > 0 and exponente <= 10 and exponente == int(exponente):
                pasos = " × ".join(str(base) for _ in range(int(exponente)))
                print(f"   {base}^{int(exponente)} = {pasos} = {resultado}")
            
            # Información adicional
            if exponente < 0:
                print(f"   (Exponente negativo: 1 / {base}^{abs(exponente)})")
            
            continuar = input("\n¿Calcular otra potencia? (s/n): ").lower()
            if continuar != 's':
                break
        
        except ValueError:
            print("❌ Por favor ingrese números válidos")
        except OverflowError:
            print("❌ El resultado es demasiado grande")
        except KeyboardInterrupt:
            print("\n\n👋 Operación cancelada")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

# Descomentar para probar:
# potenciacion_interactiva()

# Versión 10: Tabla de potencias
print("=== Versión 10: Tabla de Potencias ===")
def tabla_potencias(base, limite=10):
    """
    Genera una tabla de potencias de una base.
    """
    print(f"\nTabla de potencias de {base}:")
    print("=" * 40)
    print(f"{'Exponente':<12} {'Resultado':<20}")
    print("-" * 40)
    
    for exp in range(limite + 1):
        try:
            resultado = base ** exp
            print(f"{exp:<12} {resultado:<20}")
        except OverflowError:
            print(f"{exp:<12} {'Muy grande':<20}")
    
    print("=" * 40)

tabla_potencias(2, 10)
print()

# Versión 11: Propiedades de las potencias
print("=== Versión 11: Propiedades de las Potencias ===")
def demostrar_propiedades():
    """
    Demuestra propiedades importantes de las potencias.
    """
    print("\nPropiedades de las Potencias:")
    print("=" * 60)
    
    # Propiedad 1: a^m * a^n = a^(m+n)
    a, m, n = 2, 3, 4
    izquierda = (a ** m) * (a ** n)
    derecha = a ** (m + n)
    print(f"1. a^m × a^n = a^(m+n)")
    print(f"   {a}^{m} × {a}^{n} = {a}^{m} × {a}^{n} = {izquierda}")
    print(f"   {a}^({m}+{n}) = {a}^{m+n} = {derecha}")
    print(f"   ✓ Coinciden: {izquierda == derecha}")
    
    # Propiedad 2: (a^m)^n = a^(m*n)
    a, m, n = 2, 3, 4
    izquierda = (a ** m) ** n
    derecha = a ** (m * n)
    print(f"\n2. (a^m)^n = a^(m×n)")
    print(f"   ({a}^{m})^{n} = {izquierda}")
    print(f"   {a}^({m}×{n}) = {a}^{m*n} = {derecha}")
    print(f"   ✓ Coinciden: {izquierda == derecha}")
    
    # Propiedad 3: a^0 = 1
    print(f"\n3. a^0 = 1 (para cualquier a ≠ 0)")
    for a in [2, 5, 10]:
        resultado = a ** 0
        print(f"   {a}^0 = {resultado}")
    
    # Propiedad 4: a^(-n) = 1 / a^n
    a, n = 2, 3
    izquierda = a ** (-n)
    derecha = 1 / (a ** n)
    print(f"\n4. a^(-n) = 1 / a^n")
    print(f"   {a}^(-{n}) = {izquierda}")
    print(f"   1 / {a}^{n} = 1 / {a**n} = {derecha}")
    print(f"   ✓ Coinciden: {abs(izquierda - derecha) < 1e-10}")
    
    print("=" * 60)

demostrar_propiedades()
print()

# Resumen
print("=== Resumen de Análisis ===")
print("Código original:")
print("  ✓ Funciona correctamente para exponentes positivos")
print("  ✓ Código claro y simple")
print("  ⚠️  No maneja exponentes negativos")
print("  ⚠️  No maneja exponente 0")
print("  ⚠️  No es eficiente para exponentes grandes (O(n))")
print("  ⚠️  No hay validación de entrada")
print()
print("Mejoras implementadas:")
print("  1. ✅ Manejo de exponentes negativos")
print("  2. ✅ Manejo de exponente 0")
print("  3. ✅ Exponenciación rápida (O(log n))")
print("  4. ✅ Validación de entrada")
print("  5. ✅ Múltiples métodos (operador **, pow(), math.pow)")
print("  6. ✅ Potenciación modular (útil en criptografía)")
print("  7. ✅ Comparación de eficiencia")
print("  8. ✅ Función interactiva mejorada")
print("  9. ✅ Tabla de potencias")
print("  10. ✅ Demostración de propiedades matemáticas")
print("  11. ✅ Documentación completa")
print()
print("Métodos recomendados:")
print("  - Operador ** o pow(): Para uso general (más eficiente)")
print("  - Exponenciación rápida: Para exponentes muy grandes")
print("  - Potenciación modular: Para operaciones con módulo")
