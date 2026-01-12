# Archivo: 44_algoritmos_strings.py
# Descripción: Algoritmos Avanzados de Strings

print("=== Algoritmos Avanzados de Strings ===\n")

# =============================================================================
# 1. ALGORITMO RABIN-KARP (String Matching)
# =============================================================================
print("=== 1. Algoritmo Rabin-Karp ===")

def rabin_karp(texto, patron, base=256, primo=101):
    """
    Búsqueda de patrón usando algoritmo Rabin-Karp (rolling hash).
    Complejidad: O(n + m) promedio, O(n * m) peor caso
    """
    n = len(texto)
    m = len(patron)
    
    if m == 0:
        return [0]
    if m > n:
        return []
    
    # Calcular hash del patrón y primera ventana del texto
    hash_patron = 0
    hash_ventana = 0
    h = 1  # h = base^(m-1) % primo
    
    # Calcular h
    for i in range(m - 1):
        h = (h * base) % primo
    
    # Calcular hash inicial
    for i in range(m):
        hash_patron = (base * hash_patron + ord(patron[i])) % primo
        hash_ventana = (base * hash_ventana + ord(texto[i])) % primo
    
    ocurrencias = []
    
    # Deslizar la ventana sobre el texto
    for i in range(n - m + 1):
        # Verificar hash
        if hash_patron == hash_ventana:
            # Verificar caracteres (por si hay colisión de hash)
            if texto[i:i+m] == patron:
                ocurrencias.append(i)
        
        # Calcular hash de la siguiente ventana
        if i < n - m:
            hash_ventana = (base * (hash_ventana - ord(texto[i]) * h) + ord(texto[i + m])) % primo
            # Asegurar que hash_ventana sea positivo
            if hash_ventana < 0:
                hash_ventana = hash_ventana + primo
    
    return ocurrencias

# Ejemplo
texto_rk = "GEEKS FOR GEEKS"
patron_rk = "GEEK"

print(f"Texto: '{texto_rk}'")
print(f"Patrón: '{patron_rk}'")
ocurrencias_rk = rabin_karp(texto_rk, patron_rk)
print(f"Ocurrencias (Rabin-Karp): {ocurrencias_rk}")
print()

# =============================================================================
# 2. ALGORITMO Z-ALGORITHM (Z-Array)
# =============================================================================
print("=== 2. Algoritmo Z-Algorithm ===")

def construir_z_array(cadena):
    """
    Construye el array Z para una cadena.
    Z[i] = longitud del prefijo más largo que empieza en i y es también prefijo de la cadena.
    Complejidad: O(n)
    """
    n = len(cadena)
    z = [0] * n
    
    # z[0] es siempre n (todo el string)
    z[0] = n
    
    l, r = 0, 0  # ventana [l, r] que coincide con el prefijo
    
    for i in range(1, n):
        if i <= r:
            # Podemos usar información previa
            z[i] = min(r - i + 1, z[i - l])
        
        # Intentar extender
        while i + z[i] < n and cadena[z[i]] == cadena[i + z[i]]:
            z[i] += 1
        
        # Actualizar ventana
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    
    return z

def z_algorithm_busqueda(texto, patron):
    """
    Busca el patrón en el texto usando Z-algorithm.
    Complejidad: O(n + m) donde n=len(texto), m=len(patron)
    """
    m = len(patron)
    if m == 0:
        return [0]
    
    # Crear cadena combinada: patron + $ + texto
    combinado = patron + "$" + texto
    z = construir_z_array(combinado)
    
    # Buscar ocurrencias (donde z[i] == len(patron))
    ocurrencias = []
    for i in range(m + 1, len(combinado)):
        if z[i] == m:
            ocurrencias.append(i - m - 1)  # Ajustar índice
    
    return ocurrencias

# Ejemplo
texto_z = "ABABDABACDABABCABCABAB"
patron_z = "ABABCABAB"

print(f"Texto: '{texto_z}'")
print(f"Patrón: '{patron_z}'")
ocurrencias_z = z_algorithm_busqueda(texto_z, patron_z)
print(f"Ocurrencias (Z-Algorithm): {ocurrencias_z}")

# Ejemplo de Z-array
cadena_z = "aabxaabxcaabxaabxay"
z_array = construir_z_array(cadena_z)
print(f"\nCadena: '{cadena_z}'")
print(f"Z-array: {z_array}")
print()

# =============================================================================
# 3. LONGEST COMMON SUBSTRING (Subcadena Común Más Larga)
# =============================================================================
print("=== 3. Subcadena Común Más Larga ===")

def longest_common_substring(X, Y):
    """
    Encuentra la subcadena común más larga entre dos strings.
    Complejidad: O(m * n) donde m=len(X), n=len(Y)
    """
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    longitud_maxima = 0
    posicion_maxima = 0
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > longitud_maxima:
                    longitud_maxima = dp[i][j]
                    posicion_maxima = i
    
    # Reconstruir la subcadena
    subcadena = X[posicion_maxima - longitud_maxima:posicion_maxima]
    
    return longitud_maxima, subcadena

# Ejemplo
str1_lcs = "ABCDGH"
str2_lcs = "ACDGHR"

print(f"String 1: '{str1_lcs}'")
print(f"String 2: '{str2_lcs}'")
longitud, subcadena = longest_common_substring(str1_lcs, str2_lcs)
print(f"Longitud: {longitud}")
print(f"Subcadena: '{subcadena}'")
print()

# =============================================================================
# 4. EDIT DISTANCE (Levenshtein Distance)
# =============================================================================
print("=== 4. Distancia de Edición (Levenshtein) ===")

def edit_distance(str1, str2):
    """
    Calcula la distancia de edición (Levenshtein) entre dos strings.
    Es el número mínimo de operaciones (insertar, eliminar, sustituir) necesarias.
    Complejidad: O(m * n)
    """
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Casos base
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Llenar la tabla
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],      # Eliminar
                    dp[i][j-1],      # Insertar
                    dp[i-1][j-1]     # Sustituir
                )
    
    return dp[m][n]

# Ejemplo
palabra1 = "kitten"
palabra2 = "sitting"

print(f"Palabra 1: '{palabra1}'")
print(f"Palabra 2: '{palabra2}'")
distancia = edit_distance(palabra1, palabra2)
print(f"Distancia de edición: {distancia}")
print(f"Operaciones necesarias para convertir '{palabra1}' en '{palabra2}'")
print()

# =============================================================================
# 5. LONGEST PALINDROMIC SUBSTRING (Subcadena Palindrómica Más Larga)
# =============================================================================
print("=== 5. Subcadena Palindrómica Más Larga ===")

def longest_palindromic_substring(s):
    """
    Encuentra la subcadena palindrómica más larga usando expansión desde centro.
    Complejidad: O(n²)
    """
    if not s:
        return ""
    
    def expandir_desde_centro(izquierda, derecha):
        while izquierda >= 0 and derecha < len(s) and s[izquierda] == s[derecha]:
            izquierda -= 1
            derecha += 1
        return s[izquierda + 1:derecha]
    
    subcadena_max = ""
    
    for i in range(len(s)):
        # Palíndromo de longitud impar
        pal1 = expandir_desde_centro(i, i)
        # Palíndromo de longitud par
        pal2 = expandir_desde_centro(i, i + 1)
        
        # Actualizar máximo
        if len(pal1) > len(subcadena_max):
            subcadena_max = pal1
        if len(pal2) > len(subcadena_max):
            subcadena_max = pal2
    
    return subcadena_max

# Ejemplo
cadena_pal = "babad"
print(f"Cadena: '{cadena_pal}'")
palindromo_max = longest_palindromic_substring(cadena_pal)
print(f"Subcadena palindrómica más larga: '{palindromo_max}'")
print()

# =============================================================================
# 6. ANAGRAMAS Y PERMUTACIONES
# =============================================================================
print("=== 6. Anagramas y Permutaciones ===")

def son_anagramas(str1, str2):
    """Verifica si dos strings son anagramas."""
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)

def contar_anagramas(lista_palabras):
    """Agrupa palabras que son anagramas."""
    grupos = {}
    for palabra in lista_palabras:
        clave = ''.join(sorted(palabra))
        if clave not in grupos:
            grupos[clave] = []
        grupos[clave].append(palabra)
    return grupos

def encontrar_permutaciones(s):
    """Encuentra todas las permutaciones de un string."""
    if len(s) <= 1:
        return [s]
    
    permutaciones = []
    for i, char in enumerate(s):
        resto = s[:i] + s[i+1:]
        for perm in encontrar_permutaciones(resto):
            permutaciones.append(char + perm)
    
    return permutaciones

# Ejemplo
palabra1_anag = "listen"
palabra2_anag = "silent"
print(f"'{palabra1_anag}' y '{palabra2_anag}' son anagramas: {son_anagramas(palabra1_anag, palabra2_anag)}")

lista_anagramas = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(f"\nLista: {lista_anagramas}")
grupos = contar_anagramas(lista_anagramas)
print("Grupos de anagramas:")
for grupo in grupos.values():
    print(f"  {grupo}")

cadena_perm = "abc"
print(f"\nPermutaciones de '{cadena_perm}':")
permutaciones = encontrar_permutaciones(cadena_perm)
print(f"  {permutaciones}")
print()

# Resumen
print("=== RESUMEN ===")
print("""
Algoritmos avanzados de strings implementados:

1. Rabin-Karp:
   - Búsqueda de patrón usando rolling hash
   - Complejidad: O(n + m) promedio
   - Útil para múltiples patrones

2. Z-Algorithm:
   - Construcción de Z-array
   - Búsqueda eficiente de patrones
   - Complejidad: O(n + m)

3. Longest Common Substring:
   - Encuentra la subcadena común más larga
   - Complejidad: O(m * n)

4. Edit Distance (Levenshtein):
   - Distancia entre dos strings
   - Operaciones: insertar, eliminar, sustituir
   - Complejidad: O(m * n)

5. Longest Palindromic Substring:
   - Encuentra el palíndromo más largo
   - Complejidad: O(n²)

6. Anagramas y Permutaciones:
   - Detección de anagramas
   - Agrupación de anagramas
   - Generación de permutaciones

Aplicaciones:
- Búsqueda de texto (grep, editores)
- Corrección ortográfica
- Comparación de secuencias biológicas
- Análisis de texto y NLP
""")
