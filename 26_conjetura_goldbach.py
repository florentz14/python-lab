# Archivo: 26_conjetura_goldbach.py
# Descripción: Conjetura de Goldbach - Todo número par mayor que 2 se puede expresar como suma de dos números primos

import math

print("=== Conjetura de Goldbach ===\n")
print("Todo número par mayor que 2 se puede expresar como suma de dos números primos.\n")

# Versión 1: Original
print("=== Versión 1: Original ===")
def es_primo_original(n):
    """
    Versión original de verificación de números primos.
    Complejidad: O(n)
    """
    if n < 2:
        return False
    for i in range(2, n):  # Se excluye el 1 y el mismo número
        if n % i == 0:
            return False
    return True

def goldbach_original(num):
    """
    Versión original del algoritmo de Goldbach.
    """
    if num % 2 == 0 and num > 2:  # Condición para verificar que el número sea par y mayor que 2
        encontrado = False
        for a in range(2, num):
            if es_primo_original(a):
                # Se toma num(14) y se le resta el primer número primo a(3) y si el resultado b(11) es un número primo, se forma una pareja (a,b)
                b = num - a
                if es_primo_original(b):
                    encontrado = True
                    if a <= b:  # Condición para evitar que se repitan las parejas
                        print("Primos", a, b)  # Mostrar en pantalla las parejas
        
        if not encontrado:
            print("No se ha encontrado ninguna pareja")
    else:
        print("No es un numero valido")

print("Versión original definida.\n")

# Versión 2: Optimizada (mejor eficiencia)
print("=== Versión 2: Optimizada ===")
def es_primo_optimizado(n):
    """
    Versión optimizada de verificación de números primos.
    Complejidad: O(√n) - mucho más eficiente
    
    Solo verifica divisores hasta √n porque si n tiene un divisor mayor que √n,
    también tiene uno menor que √n.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:  # Números pares mayores que 2 no son primos
        return False
    
    # Solo verificar divisores impares hasta √n
    limite = int(math.sqrt(n)) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return False
    return True

def goldbach_optimizado(num, mostrar_proceso=True):
    """
    Versión optimizada del algoritmo de Goldbach.
    
    Optimizaciones:
    1. Función es_primo más eficiente (O(√n) vs O(n))
    2. Solo recorre hasta num/2 (evita duplicados)
    3. Verifica que b >= a antes de calcular
    
    Retorna lista de tuplas (primo1, primo2)
    """
    if num % 2 != 0 or num <= 2:
        if mostrar_proceso:
            print("❌ No es un número válido (debe ser par y mayor que 2)")
        return []
    
    parejas = []
    limite = num // 2 + 1  # Solo necesitamos hasta la mitad
    
    for a in range(2, limite):
        if es_primo_optimizado(a):
            b = num - a
            if b >= a and es_primo_optimizado(b):  # Verificar que b >= a y es primo
                parejas.append((a, b))
                if mostrar_proceso:
                    print(f"  {a} + {b} = {num}")
    
    if mostrar_proceso:
        if parejas:
            print(f"\n✅ Se encontraron {len(parejas)} pareja(s) de números primos")
        else:
            print("\n⚠️  No se encontró ninguna pareja (esto no debería pasar según la conjetura)")
    
    return parejas

# Prueba con ejemplo
print("Ejemplo: Número 14")
goldbach_optimizado(14)
print()

# Versión 3: Con caché de primos (más eficiente para múltiples llamadas)
print("=== Versión 3: Con Caché de Primos ===")
class GoldbachCaché:
    """
    Clase que mantiene un caché de números primos para mayor eficiencia
    cuando se verifican múltiples números.
    """
    
    def __init__(self):
        self.primos_cache = {2: True}
        self.max_verificado = 2
    
    def es_primo_cached(self, n):
        """
        Verifica si un número es primo usando caché.
        """
        if n < 2:
            return False
        if n in self.primos_cache:
            return self.primos_cache[n]
        
        # Si no está en caché, calcular y guardar
        if n > self.max_verificado:
            # Verificar todos los números hasta n
            for i in range(self.max_verificado + 1, n + 1):
                self.primos_cache[i] = es_primo_optimizado(i)
            self.max_verificado = n
        
        return self.primos_cache.get(n, False)
    
    def goldbach(self, num, mostrar_proceso=True):
        """
        Encuentra parejas de Goldbach usando caché.
        """
        if num % 2 != 0 or num <= 2:
            if mostrar_proceso:
                print("❌ No es un número válido")
            return []
        
        parejas = []
        limite = num // 2 + 1
        
        for a in range(2, limite):
            if self.es_primo_cached(a):
                b = num - a
                if b >= a and self.es_primo_cached(b):
                    parejas.append((a, b))
                    if mostrar_proceso:
                        print(f"  {a} + {b} = {num}")
        
        if mostrar_proceso and parejas:
            print(f"\n✅ {len(parejas)} pareja(s) encontrada(s)")
        
        return parejas

# Ejemplo de uso con caché
print("Ejemplo con caché: Números 14, 20, 28")
cache_goldbach = GoldbachCaché()
for num in [14, 20, 28]:
    print(f"\nNúmero {num}:")
    cache_goldbach.goldbach(num)
print()

# Versión 4: Con validación y entrada interactiva mejorada
print("=== Versión 4: Interactiva Mejorada ===")
def goldbach_interactivo():
    """
    Versión interactiva mejorada con validación y manejo de errores.
    """
    while True:
        try:
            num = int(input("\nIngrese un número par mayor que 2 (o 0 para salir): "))
            
            if num == 0:
                print("👋 ¡Hasta luego!")
                break
            
            if num % 2 != 0:
                print(f"⚠️  {num} no es un número par")
                continue
            
            if num <= 2:
                print(f"⚠️  {num} debe ser mayor que 2")
                continue
            
            print(f"\n🔍 Buscando parejas de primos para {num}:")
            parejas = goldbach_optimizado(num, mostrar_proceso=True)
            
            if parejas:
                print(f"\n📊 Resumen: {len(parejas)} pareja(s) encontrada(s)")
                respuesta = input("\n¿Verificar otro número? (s/n): ").lower()
                if respuesta != 's':
                    break
        
        except ValueError:
            print("❌ Por favor ingrese un número entero válido")
        except KeyboardInterrupt:
            print("\n\n👋 Operación cancelada. ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

# Descomentar para probar:
# goldbach_interactivo()

# Versión 5: Analizar rango de números
print("=== Versión 5: Analizar Rango de Números ===")
def analizar_rango_goldbach(inicio, fin):
    """
    Analiza la conjetura de Goldbach para un rango de números pares.
    """
    if inicio % 2 != 0:
        inicio += 1
    if fin % 2 != 0:
        fin -= 1
    
    print(f"\nAnalizando números pares del {inicio} al {fin}:")
    print("-" * 60)
    
    resultados = {}
    for num in range(inicio, fin + 1, 2):
        if num > 2:
            parejas = goldbach_optimizado(num, mostrar_proceso=False)
            resultados[num] = len(parejas)
            print(f"Número {num:4d}: {len(parejas):2d} pareja(s) - Ejemplo: {parejas[0] if parejas else 'N/A'}")
    
    print("-" * 60)
    print(f"Total analizado: {len(resultados)} números")
    promedio = sum(resultados.values()) / len(resultados) if resultados else 0
    print(f"Promedio de parejas por número: {promedio:.2f}")
    
    return resultados

# Ejemplo de análisis de rango
print("Análisis de números del 4 al 30:")
analizar_rango_goldbach(4, 30)
print()

# Versión 6: Verificación estadística
print("=== Versión 6: Verificación Estadística ===")
def verificar_conjetura_goldbach(limite_superior=1000):
    """
    Verifica la conjetura de Goldbach hasta un límite superior.
    """
    print(f"\n🔬 Verificando la Conjetura de Goldbach hasta {limite_superior}")
    print("=" * 60)
    
    numeros_sin_pareja = []
    total_verificados = 0
    
    for num in range(4, limite_superior + 1, 2):
        total_verificados += 1
        parejas = goldbach_optimizado(num, mostrar_proceso=False)
        if not parejas:
            numeros_sin_pareja.append(num)
    
    print(f"\n📊 Resultados:")
    print(f"  Números verificados: {total_verificados}")
    print(f"  Números con parejas: {total_verificados - len(numeros_sin_pareja)}")
    print(f"  Números sin parejas: {len(numeros_sin_pareja)}")
    
    if numeros_sin_pareja:
        print(f"\n⚠️  ¡ALERTA! Se encontraron números sin parejas:")
        print(f"   {numeros_sin_pareja}")
        print("   Esto contradiría la conjetura de Goldbach")
    else:
        print(f"\n✅ Todos los números pares verificados tienen al menos una pareja")
        print("   La conjetura se cumple para el rango analizado")
    
    print("=" * 60)
    return len(numeros_sin_pareja) == 0

# Verificar hasta 100 (para no tardar mucho)
print("Verificación rápida (hasta 100):")
verificar_conjetura_goldbach(100)
print()

# Versión 7: Comparación de eficiencia
print("=== Versión 7: Comparación de Eficiencia ===")
import time

def comparar_eficiencia(num):
    """
    Compara el tiempo de ejecución de diferentes versiones.
    """
    print(f"\nComparando eficiencia para número {num}:")
    
    # Versión original
    inicio = time.time()
    goldbach_original(num)
    tiempo_original = time.time() - inicio
    
    # Versión optimizada
    inicio = time.time()
    goldbach_optimizado(num, mostrar_proceso=False)
    tiempo_optimizado = time.time() - inicio
    
    print(f"\n⏱️  Tiempos:")
    print(f"  Original:  {tiempo_original*1000:.4f} ms")
    print(f"  Optimizada: {tiempo_optimizado*1000:.4f} ms")
    if tiempo_original > 0:
        mejora = tiempo_original / tiempo_optimizado
        print(f"  Mejora: {mejora:.2f}x más rápido")

comparar_eficiencia(100)
print()

# Resumen y mejoras
print("=== Resumen de Análisis ===")
print("Problemas en el código original:")
print("1. ⚠️  Función es_primo es O(n) - puede ser O(√n)")
print("2. ⚠️  Recorre todo el rango (2, num) - puede optimizarse a (2, num//2+1)")
print("3. ⚠️  No hay manejo de errores para input")
print("4. ⚠️  La variable 'encontrado' no se usa correctamente (siempre será True si hay parejas)")
print("5. ⚠️  No retorna resultados, solo imprime")
print()
print("Mejoras implementadas:")
print("1. ✅ Función es_primo optimizada a O(√n)")
print("2. ✅ Bucle optimizado (solo hasta num//2)")
print("3. ✅ Manejo completo de errores")
print("4. ✅ Retorna lista de parejas")
print("5. ✅ Versión con caché para múltiples verificaciones")
print("6. ✅ Análisis de rangos y estadísticas")
print("7. ✅ Verificación de la conjetura")
print("8. ✅ Comparación de eficiencia")
print("9. ✅ Documentación completa")

# Ejemplos prácticos
print("\n=== Ejemplos Prácticos ===")
ejemplos = [14, 20, 28, 50, 100]
print("Ejemplos de números y sus parejas de Goldbach:")
for num in ejemplos:
    print(f"\nNúmero {num}:")
    parejas = goldbach_optimizado(num, mostrar_proceso=True)
