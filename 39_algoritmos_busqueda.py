# Archivo: 39_algoritmos_busqueda.py
# Descripción: Algoritmos de búsqueda - Búsqueda lineal, binaria, y en strings

import time
import random

print("=== Algoritmos de Búsqueda ===\n")

# =============================================================================
# 1. BÚSQUEDA LINEAL (Linear Search)
# =============================================================================
print("=== 1. BÚSQUEDA LINEAL (Linear Search) ===")

def busqueda_lineal(lista, objetivo):
    """
    Búsqueda lineal - busca elemento por elemento.
    Complejidad: O(n) en el peor caso
    Funciona con listas no ordenadas
    """
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice
    return -1

def busqueda_lineal_optimizada(lista, objetivo):
    """
    Búsqueda lineal con optimización temprana.
    """
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice
        # Si la lista está ordenada y encontramos un elemento mayor, podemos parar
        if lista[indice] > objetivo:
            return -1
    return -1

# Ejemplo
lista_ejemplo = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(f"Lista: {lista_ejemplo}")
resultado = busqueda_lineal(lista_ejemplo, 5)
print(f"Búsqueda lineal de 5: índice {resultado}")
print(f"Elemento encontrado: {lista_ejemplo[resultado] if resultado != -1 else 'No encontrado'}")

# Búsqueda de todas las ocurrencias
def busqueda_lineal_todas(lista, objetivo):
    """Encuentra todas las ocurrencias de un elemento."""
    indices = []
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            indices.append(indice)
    return indices

print(f"Todas las ocurrencias de 5: {busqueda_lineal_todas(lista_ejemplo, 5)}")
print()

# =============================================================================
# 2. BÚSQUEDA BINARIA (Binary Search)
# =============================================================================
print("=== 2. BÚSQUEDA BINARIA (Binary Search) ===")

def busqueda_binaria(lista, objetivo):
    """
    Búsqueda binaria - divide y vencerás.
    Complejidad: O(log n)
    REQUIERE lista ordenada
    """
    if not lista:
        return -1
    
    izquierda = 0
    derecha = len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return -1

def busqueda_binaria_recursiva(lista, objetivo, izquierda=0, derecha=None):
    """
    Búsqueda binaria usando recursión.
    """
    if derecha is None:
        derecha = len(lista) - 1
    
    if izquierda > derecha:
        return -1
    
    medio = (izquierda + derecha) // 2
    
    if lista[medio] == objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, derecha)
    else:
        return busqueda_binaria_recursiva(lista, objetivo, izquierda, medio - 1)

def busqueda_binaria_primera_ocurrencia(lista, objetivo):
    """
    Búsqueda binaria que encuentra la primera ocurrencia.
    Útil para listas con elementos duplicados.
    """
    izquierda = 0
    derecha = len(lista) - 1
    resultado = -1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if lista[medio] == objetivo:
            resultado = medio
            derecha = medio - 1  # Continuar buscando a la izquierda
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return resultado

def busqueda_binaria_ultima_ocurrencia(lista, objetivo):
    """Búsqueda binaria que encuentra la última ocurrencia."""
    izquierda = 0
    derecha = len(lista) - 1
    resultado = -1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if lista[medio] == objetivo:
            resultado = medio
            izquierda = medio + 1  # Continuar buscando a la derecha
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return resultado

# Ejemplo
lista_ordenada = sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
print(f"Lista ordenada: {lista_ordenada}")
resultado = busqueda_binaria(lista_ordenada, 5)
print(f"Búsqueda binaria de 5: índice {resultado}")
print(f"Primera ocurrencia de 5: {busqueda_binaria_primera_ocurrencia(lista_ordenada, 5)}")
print(f"Última ocurrencia de 5: {busqueda_binaria_ultima_ocurrencia(lista_ordenada, 5)}")
print()

# =============================================================================
# 3. BÚSQUEDA EN STRINGS
# =============================================================================
print("=== 3. BÚSQUEDA EN STRINGS ===")

def busqueda_bruta_texto(texto, patron):
    """
    Búsqueda de patrón en texto (fuerza bruta).
    Complejidad: O(n*m) donde n=len(texto), m=len(patron)
    """
    n = len(texto)
    m = len(patron)
    
    if m == 0:
        return 0
    if m > n:
        return -1
    
    for i in range(n - m + 1):
        j = 0
        while j < m and texto[i + j] == patron[j]:
            j += 1
        if j == m:
            return i
    
    return -1

def busqueda_bruta_todas(texto, patron):
    """Encuentra todas las ocurrencias del patrón."""
    n = len(texto)
    m = len(patron)
    ocurrencias = []
    
    if m == 0:
        return [0]
    if m > n:
        return []
    
    for i in range(n - m + 1):
        j = 0
        while j < m and texto[i + j] == patron[j]:
            j += 1
        if j == m:
            ocurrencias.append(i)
    
    return ocurrencias

# Ejemplo
texto = "abracadabra"
patron = "abra"
print(f"Texto: '{texto}'")
print(f"Patrón: '{patron}'")
resultado = busqueda_bruta_texto(texto, patron)
print(f"Primera ocurrencia: índice {resultado}")
print(f"Todas las ocurrencias: {busqueda_bruta_todas(texto, patron)}")
print()

# =============================================================================
# 4. ALGORITMO KMP (Knuth-Morris-Pratt)
# =============================================================================
print("=== 4. ALGORITMO KMP (Knuth-Morris-Pratt) ===")

def construir_tabla_lps(patron):
    """
    Construye la tabla de Longest Proper Prefix which is also Suffix (LPS).
    """
    m = len(patron)
    lps = [0] * m
    longitud = 0
    i = 1
    
    while i < m:
        if patron[i] == patron[longitud]:
            longitud += 1
            lps[i] = longitud
            i += 1
        else:
            if longitud != 0:
                longitud = lps[longitud - 1]
            else:
                lps[i] = 0
                i += 1
    
    return lps

def kmp_busqueda(texto, patron):
    """
    Búsqueda de patrón usando algoritmo KMP.
    Complejidad: O(n + m)
    Más eficiente que fuerza bruta para patrones largos
    """
    n = len(texto)
    m = len(patron)
    
    if m == 0:
        return 0
    if m > n:
        return -1
    
    lps = construir_tabla_lps(patron)
    
    i = 0  # Índice para texto
    j = 0  # Índice para patrón
    
    while i < n:
        if texto[i] == patron[j]:
            i += 1
            j += 1
        
        if j == m:
            return i - j  # Patrón encontrado
        elif i < n and texto[i] != patron[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return -1

def kmp_busqueda_todas(texto, patron):
    """KMP que encuentra todas las ocurrencias."""
    n = len(texto)
    m = len(patron)
    ocurrencias = []
    
    if m == 0:
        return [0]
    if m > n:
        return []
    
    lps = construir_tabla_lps(patron)
    
    i = 0
    j = 0
    
    while i < n:
        if texto[i] == patron[j]:
            i += 1
            j += 1
        
        if j == m:
            ocurrencias.append(i - j)
            j = lps[j - 1]
        elif i < n and texto[i] != patron[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return ocurrencias

# Ejemplo
texto_kmp = "ABABDABACDABABCABCABAB"
patron_kmp = "ABABCABAB"
print(f"Texto: '{texto_kmp}'")
print(f"Patrón: '{patron_kmp}'")
resultado_kmp = kmp_busqueda(texto_kmp, patron_kmp)
print(f"KMP - Primera ocurrencia: índice {resultado_kmp}")
print(f"KMP - Todas las ocurrencias: {kmp_busqueda_todas(texto_kmp, patron_kmp)}")
print()

# =============================================================================
# 5. COMPARACIÓN DE EFICIENCIA
# =============================================================================
print("=== 5. COMPARACIÓN DE EFICIENCIA ===")

def comparar_busquedas_lista(lista, objetivo, ordenada=False):
    """Compara búsqueda lineal vs binaria."""
    if ordenada:
        lista = sorted(lista)
    
    print(f"\nBuscando {objetivo} en lista de {len(lista)} elementos ({'ordenada' if ordenada else 'no ordenada'}):")
    
    # Búsqueda lineal
    inicio = time.time()
    resultado_lineal = busqueda_lineal(lista, objetivo)
    tiempo_lineal = time.time() - inicio
    
    # Búsqueda binaria (solo si está ordenada)
    if ordenada:
        inicio = time.time()
        resultado_binaria = busqueda_binaria(lista, objetivo)
        tiempo_binaria = time.time() - inicio
        
        print(f"  Búsqueda lineal: {tiempo_lineal*1000:.4f} ms (índice: {resultado_lineal})")
        print(f"  Búsqueda binaria: {tiempo_binaria*1000:.4f} ms (índice: {resultado_binaria})")
        print(f"  Mejora: {tiempo_lineal/tiempo_binaria:.2f}x más rápido" if tiempo_binaria > 0 else "")
    else:
        print(f"  Búsqueda lineal: {tiempo_lineal*1000:.4f} ms (índice: {resultado_lineal})")
        print(f"  (Búsqueda binaria requiere lista ordenada)")

# Comparación con diferentes tamaños
for tamaño in [100, 1000, 10000]:
    lista_grande = list(range(tamaño))
    objetivo = tamaño // 2
    comparar_busquedas_lista(lista_grande, objetivo, ordenada=True)

print()

def comparar_busquedas_texto(texto, patron):
    """Compara búsqueda bruta vs KMP."""
    print(f"\nBuscando '{patron}' en texto de {len(texto)} caracteres:")
    
    # Fuerza bruta
    inicio = time.time()
    resultado_bruta = busqueda_bruta_texto(texto, patron)
    tiempo_bruta = time.time() - inicio
    
    # KMP
    inicio = time.time()
    resultado_kmp = kmp_busqueda(texto, patron)
    tiempo_kmp = time.time() - inicio
    
    print(f"  Fuerza bruta: {tiempo_bruta*1000:.4f} ms (índice: {resultado_bruta})")
    print(f"  KMP: {tiempo_kmp*1000:.4f} ms (índice: {resultado_kmp})")
    if tiempo_kmp > 0:
        print(f"  Mejora: {tiempo_bruta/tiempo_kmp:.2f}x más rápido")

# Comparación con texto largo
texto_largo = "AB" * 1000 + "CD" * 1000
patron_largo = "ABCD" * 10
comparar_busquedas_texto(texto_largo, patron_largo)

print()

# =============================================================================
# 6. BÚSQUEDA EN LISTA ORDENADA (funciones útiles)
# =============================================================================
print("=== 6. FUNCIONES ÚTILES PARA LISTAS ORDENADAS ===")

def encontrar_posicion_insercion(lista, objetivo):
    """
    Encuentra la posición donde se debería insertar un elemento
    para mantener la lista ordenada (bisect_left).
    """
    izquierda = 0
    derecha = len(lista)
    
    while izquierda < derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio
    
    return izquierda

def contar_ocurrencias(lista_ordenada, objetivo):
    """
    Cuenta cuántas veces aparece un elemento en una lista ordenada.
    Usa búsqueda binaria para eficiencia O(log n).
    """
    primera = busqueda_binaria_primera_ocurrencia(lista_ordenada, objetivo)
    if primera == -1:
        return 0
    
    ultima = busqueda_binaria_ultima_ocurrencia(lista_ordenada, objetivo)
    return ultima - primera + 1

# Ejemplo
lista_con_duplicados = [1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6]
print(f"Lista: {lista_con_duplicados}")
print(f"Posición para insertar 3: {encontrar_posicion_insercion(lista_con_duplicados, 3)}")
print(f"Cantidad de 5s: {contar_ocurrencias(lista_con_duplicados, 5)}")
print()

# Resumen
print("=== RESUMEN ===")
print("""
Algoritmos de búsqueda implementados:

1. Búsqueda Lineal (O(n)):
   - Funciona con listas no ordenadas
   - Simple y directa
   - Útil para listas pequeñas o no ordenadas

2. Búsqueda Binaria (O(log n)):
   - REQUIERE lista ordenada
   - Muy eficiente para listas grandes
   - Variantes: primera/última ocurrencia

3. Búsqueda en Strings:
   - Fuerza bruta: O(n*m)
   - KMP: O(n+m) - más eficiente para patrones largos

4. Funciones útiles:
   - Posición de inserción
   - Conteo de ocurrencias en lista ordenada

Recomendaciones:
- Usar búsqueda lineal para listas pequeñas (< 100 elementos)
- Usar búsqueda binaria para listas grandes y ordenadas
- Usar KMP para búsquedas repetidas de patrones en texto largo
""")
