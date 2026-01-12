# Archivo: 16_palindromos.py
# Descripción: Verificar si una cadena es un palíndromo

import re
import string

print("=== Palíndromos en Python ===\n")

# Versión 1: Original
print("=== Versión 1: Original ===")
def es_palindromo(cadena):
    """
    Verifica si una cadena es un palíndromo.
    Elimina espacios y convierte a minúsculas.
    """
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

texto = "Anita lava la tina"
if es_palindromo(texto):
    print(f'"{texto}" es un palíndromo.')
else:
    print(f'"{texto}" no es un palíndromo.')
print()

# Versión 2: Mejorada (eliminar más caracteres especiales)
print("=== Versión 2: Eliminar Caracteres Especiales ===")
def es_palindromo_mejorado(cadena):
    """
    Versión mejorada que elimina todos los caracteres no alfanuméricos.
    """
    # Eliminar espacios y caracteres especiales, convertir a minúsculas
    cadena_limpia = re.sub(r'[^a-zA-Z0-9]', '', cadena).lower()
    return cadena_limpia == cadena_limpia[::-1]

textos_prueba = [
    "Anita lava la tina",
    "A man a plan a canal Panama",
    "No 'x' in Nixon",
    "¿Acaso hubo búhos acá?"
]

for texto in textos_prueba:
    resultado = es_palindromo_mejorado(texto)
    print(f'"{texto}" -> {"Es palíndromo" if resultado else "No es palíndromo"}')
print()

# Versión 3: Usando bucle (más eficiente para cadenas grandes)
print("=== Versión 3: Usando Bucle (Comparación Carácter por Carácter) ===")
def es_palindromo_bucle(cadena):
    """
    Compara caracteres desde ambos extremos usando un bucle.
    Más eficiente en memoria para cadenas grandes.
    """
    cadena_limpia = re.sub(r'[^a-zA-Z0-9]', '', cadena).lower()
    izquierda = 0
    derecha = len(cadena_limpia) - 1
    
    while izquierda < derecha:
        if cadena_limpia[izquierda] != cadena_limpia[derecha]:
            return False
        izquierda += 1
        derecha -= 1
    
    return True

texto = "Anita lava la tina"
print(f'"{texto}" -> {"Es palíndromo" if es_palindromo_bucle(texto) else "No es palíndromo"}')
print()

# Versión 4: Recursiva
print("=== Versión 4: Recursiva ===")
def es_palindromo_recursivo(cadena, izquierda=0, derecha=None):
    """
    Versión recursiva para verificar palíndromos.
    """
    cadena_limpia = re.sub(r'[^a-zA-Z0-9]', '', cadena).lower()
    if derecha is None:
        derecha = len(cadena_limpia) - 1
    
    if izquierda >= derecha:
        return True
    
    if cadena_limpia[izquierda] != cadena_limpia[derecha]:
        return False
    
    return es_palindromo_recursivo(cadena_limpia, izquierda + 1, derecha - 1)

texto = "Anita lava la tina"
print(f'"{texto}" -> {"Es palíndromo" if es_palindromo_recursivo(texto) else "No es palíndromo"}')
print()

# Versión 5: Verificar solo números
print("=== Versión 5: Palíndromos Numéricos ===")
def es_palindromo_numerico(numero):
    """
    Verifica si un número es palíndromo.
    """
    cadena = str(numero)
    return cadena == cadena[::-1]

numeros = [121, 12321, 123, 1234321, 12345]
for num in numeros:
    resultado = es_palindromo_numerico(num)
    print(f"{num} -> {'Es palíndromo' if resultado else 'No es palíndromo'}")
print()

# Versión 6: Encontrar todos los palíndromos en una lista
print("=== Versión 6: Filtrar Palíndromos de una Lista ===")
def filtrar_palindromos(lista_textos):
    """
    Filtra y retorna solo los palíndromos de una lista.
    """
    return [texto for texto in lista_textos if es_palindromo_mejorado(texto)]

textos = [
    "Anita lava la tina",
    "Hola mundo",
    "A man a plan a canal Panama",
    "Python",
    "Reconocer"
]

palindromos = filtrar_palindromos(textos)
print(f"Textos: {textos}")
print(f"Palíndromos encontrados: {palindromos}")
print()

# Versión 7: Generar palíndromos
print("=== Versión 7: Generar Palíndromo a partir de un Texto ===")
def generar_palindromo(texto):
    """
    Genera un palíndromo agregando el reverso del texto.
    """
    texto_limpio = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
    reverso = texto_limpio[::-1]
    return texto_limpio + reverso

texto = "Hola"
palindromo_generado = generar_palindromo(texto)
print(f'Texto: "{texto}"')
print(f'Palíndromo generado: "{palindromo_generado}"')
print()

# Versión 8: Verificar palíndromos en una frase (palabras individuales)
print("=== Versión 8: Palíndromos en Palabras Individuales ===")
def encontrar_palindromos_en_frase(frase):
    """
    Encuentra todas las palabras que son palíndromos en una frase.
    """
    palabras = re.findall(r'\b\w+\b', frase)
    palindromos = [palabra for palabra in palabras if es_palindromo_mejorado(palabra)]
    return palindromos

frase = "Anita lava la tina y reconocer es importante"
palindromos_encontrados = encontrar_palindromos_en_frase(frase)
print(f'Frase: "{frase}"')
print(f'Palíndromos encontrados: {palindromos_encontrados}')
print()

# Versión 9: Invertir texto (métodos diferentes)
print("=== Versión 9: Invertir Texto (Métodos Diferentes) ===")
def invertir_texto_slicing(texto):
    """Invertir usando slicing [::-1]"""
    return texto[::-1]

def invertir_texto_reversed(texto):
    """Invertir usando reversed() y join()"""
    return ''.join(reversed(texto))

def invertir_texto_bucle(texto):
    """Invertir usando un bucle"""
    invertido = ''
    for caracter in texto:
        invertido = caracter + invertido
    return invertido

def invertir_texto_recursivo(texto):
    """Invertir usando recursión"""
    if len(texto) <= 1:
        return texto
    return invertir_texto_recursivo(texto[1:]) + texto[0]

texto = "Hola"
print(f"Texto original: '{texto}'")
print(f"Slicing [::-1]: '{invertir_texto_slicing(texto)}'")
print(f"reversed() + join(): '{invertir_texto_reversed(texto)}'")
print(f"Bucle: '{invertir_texto_bucle(texto)}'")
print(f"Recursivo: '{invertir_texto_recursivo(texto)}'")
print()

# Versión 10: Comparación de eficiencia
print("=== Versión 10: Comparación de Eficiencia ===")
import time

def comparar_metodos(texto):
    """
    Compara el tiempo de ejecución de diferentes métodos.
    """
    # Método 1: Slicing
    inicio = time.time()
    resultado1 = texto.lower().replace(" ", "") == texto.lower().replace(" ", "")[::-1]
    tiempo1 = time.time() - inicio
    
    # Método 2: Bucle
    inicio = time.time()
    texto_limpio = texto.lower().replace(" ", "")
    izquierda, derecha = 0, len(texto_limpio) - 1
    resultado2 = True
    while izquierda < derecha:
        if texto_limpio[izquierda] != texto_limpio[derecha]:
            resultado2 = False
            break
        izquierda += 1
        derecha -= 1
    tiempo2 = time.time() - inicio
    
    print(f"Método slicing: {tiempo1*1000000:.2f} microsegundos")
    print(f"Método bucle: {tiempo2*1000000:.2f} microsegundos")
    print(f"Ambos dan el mismo resultado: {resultado1 == resultado2}")

texto_largo = "Anita lava la tina" * 100
print(f"Comparando métodos con texto largo ({len(texto_largo)} caracteres):")
comparar_metodos(texto_largo)
print()

# Ejemplos prácticos
print("=== Ejemplos Prácticos ===")
ejemplos = [
    "Anita lava la tina",
    "A man a plan a canal Panama",
    "Reconocer",
    "12321",
    "Hola mundo",
    "No 'x' in Nixon",
    "¿Acaso hubo búhos acá?"
]

print("Verificando palíndromos:")
for ejemplo in ejemplos:
    resultado = es_palindromo_mejorado(ejemplo)
    estado = "✓ ES" if resultado else "✗ NO ES"
    print(f"  {estado} palíndromo: '{ejemplo}'")
print()

# Resumen de mejoras
print("=== Resumen de Mejoras ===")
print("Mejoras implementadas:")
print("  1. Eliminación de caracteres especiales con regex")
print("  2. Método con bucle (más eficiente en memoria)")
print("  3. Versión recursiva")
print("  4. Soporte para palíndromos numéricos")
print("  5. Filtrado de palíndromos en listas")
print("  6. Generación de palíndromos")
print("  7. Búsqueda de palíndromos en frases")
print("  8. Múltiples métodos para invertir texto")
print("  9. Comparación de eficiencia entre métodos")
print("  10. Ejemplos prácticos con diferentes casos")
