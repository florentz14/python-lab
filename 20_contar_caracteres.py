# Archivo: 20_contar_caracteres.py
# Descripción: Contar caracteres en una cadena de texto

print("=== Contar Caracteres en una Cadena ===\n")

# Versión 1: Original
print("=== Versión 1: Original ===")
def contar_caracteres_original():
    """
    Versión original del código.
    Cuenta el número total de caracteres en una cadena.
    """
    palabra = input("Escribe una palabra o cadena de caracteres: ")
    total_caracteres = len(palabra)
    print("la cadena {}, tiene {} caracteres".format(palabra, total_caracteres))

# Descomentar para probar:
# contar_caracteres_original()

# Versión 2: Optimizada (f-strings)
print("=== Versión 2: Optimizada (f-strings) ===")
def contar_caracteres_optimizada():
    """
    Versión optimizada usando f-strings (más moderna y legible).
    """
    palabra = input("Escribe una palabra o cadena de caracteres: ")
    total_caracteres = len(palabra)
    print(f"La cadena '{palabra}', tiene {total_caracteres} caracteres")

# Descomentar para probar:
# contar_caracteres_optimizada()

# Versión 3: Con manejo de errores
print("=== Versión 3: Con Manejo de Errores ===")
def contar_caracteres_con_errores():
    """
    Versión con manejo de errores y validación.
    """
    try:
        palabra = input("Escribe una palabra o cadena de caracteres: ")
        if not palabra:
            print("Error: No se ingresó ninguna cadena")
            return
        
        total_caracteres = len(palabra)
        print(f"La cadena '{palabra}', tiene {total_caracteres} caracteres")
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario")
    except Exception as e:
        print(f"Error: {e}")

# Versión 4: Análisis completo de caracteres
print("=== Versión 4: Análisis Completo de Caracteres ===")
def analizar_caracteres_completo(cadena):
    """
    Análisis completo: total, letras, números, espacios, especiales, etc.
    """
    if not cadena:
        return None
    
    analisis = {
        'total': len(cadena),
        'letras': sum(1 for c in cadena if c.isalpha()),
        'mayusculas': sum(1 for c in cadena if c.isupper()),
        'minusculas': sum(1 for c in cadena if c.islower()),
        'numeros': sum(1 for c in cadena if c.isdigit()),
        'espacios': sum(1 for c in cadena if c.isspace()),
        'especiales': sum(1 for c in cadena if not c.isalnum() and not c.isspace())
    }
    
    return analisis

def mostrar_analisis_completo():
    """
    Función interactiva que muestra análisis completo.
    """
    cadena = input("Escribe una palabra o cadena de caracteres: ")
    analisis = analizar_caracteres_completo(cadena)
    
    if analisis:
        print(f"\nAnálisis de la cadena '{cadena}':")
        print(f"  Total de caracteres: {analisis['total']}")
        print(f"  Letras: {analisis['letras']} (Mayúsculas: {analisis['mayusculas']}, Minúsculas: {analisis['minusculas']})")
        print(f"  Números: {analisis['numeros']}")
        print(f"  Espacios: {analisis['espacios']}")
        print(f"  Caracteres especiales: {analisis['especiales']}")
    else:
        print("Error: Cadena vacía")

# Ejemplo de análisis completo
print("Ejemplo de análisis completo:")
cadena_ejemplo = "Hola Mundo 123!"
analisis = analizar_caracteres_completo(cadena_ejemplo)
if analisis:
    print(f"Cadena: '{cadena_ejemplo}'")
    print(f"  Total: {analisis['total']} caracteres")
    print(f"  Letras: {analisis['letras']}, Números: {analisis['numeros']}, Espacios: {analisis['espacios']}, Especiales: {analisis['especiales']}")
print()

# Versión 5: Contar caracteres sin espacios
print("=== Versión 5: Contar sin Espacios ===")
def contar_sin_espacios(cadena):
    """
    Cuenta caracteres excluyendo espacios.
    """
    total = len(cadena)
    sin_espacios = len(cadena.replace(" ", ""))
    return total, sin_espacios

def contar_caracteres_sin_espacios():
    """
    Función interactiva que cuenta con y sin espacios.
    """
    cadena = input("Escribe una palabra o cadena de caracteres: ")
    total, sin_espacios = contar_sin_espacios(cadena)
    print(f"La cadena '{cadena}' tiene:")
    print(f"  {total} caracteres (incluyendo espacios)")
    print(f"  {sin_espacios} caracteres (sin espacios)")

# Ejemplo
print("Ejemplo de contar con y sin espacios:")
cadena = "Hola Mundo"
total, sin_espacios = contar_sin_espacios(cadena)
print(f"'{cadena}': {total} caracteres totales, {sin_espacios} sin espacios")
print()

# Versión 6: Contar caracteres únicos
print("=== Versión 6: Contar Caracteres Únicos ===")
def contar_caracteres_unicos(cadena):
    """
    Cuenta cuántos caracteres únicos hay en la cadena.
    """
    caracteres_unicos = len(set(cadena))
    return caracteres_unicos

def mostrar_caracteres_unicos(cadena):
    """
    Muestra los caracteres únicos y su frecuencia.
    """
    from collections import Counter
    
    contador = Counter(cadena)
    caracteres_unicos = len(contador)
    
    print(f"Cadena: '{cadena}'")
    print(f"Total de caracteres: {len(cadena)}")
    print(f"Caracteres únicos: {caracteres_unicos}")
    print("Frecuencia de cada carácter:")
    for char, frecuencia in sorted(contador.items()):
        print(f"  '{char}': {frecuencia}")

print("Ejemplo de caracteres únicos:")
mostrar_caracteres_unicos("hola mundo")
print()

# Versión 7: Contar palabras
print("=== Versión 7: Contar Palabras ===")
def contar_palabras(cadena):
    """
    Cuenta el número de palabras en una cadena.
    """
    palabras = cadena.split()
    return len(palabras)

def analizar_texto_completo(cadena):
    """
    Análisis completo: caracteres y palabras.
    """
    total_caracteres = len(cadena)
    total_palabras = contar_palabras(cadena)
    caracteres_sin_espacios = len(cadena.replace(" ", ""))
    
    print(f"Análisis del texto: '{cadena}'")
    print(f"  Caracteres totales: {total_caracteres}")
    print(f"  Caracteres (sin espacios): {caracteres_sin_espacios}")
    print(f"  Palabras: {total_palabras}")
    if total_palabras > 0:
        print(f"  Promedio de caracteres por palabra: {caracteres_sin_espacios/total_palabras:.2f}")

print("Ejemplo de análisis de texto:")
analizar_texto_completo("Hola mundo desde Python")
print()

# Versión 8: Función reutilizable
print("=== Versión 8: Función Reutilizable ===")
def contar_caracteres(cadena):
    """
    Función reutilizable que solo cuenta y retorna.
    """
    return len(cadena)

def contar_caracteres_interactivo():
    """
    Versión interactiva que usa la función reutilizable.
    """
    while True:
        try:
            cadena = input("\nEscribe una palabra o cadena (o 'salir' para terminar): ")
            if cadena.lower() == 'salir':
                break
            
            total = contar_caracteres(cadena)
            print(f"La cadena '{cadena}' tiene {total} caracteres")
        except KeyboardInterrupt:
            print("\nSaliendo...")
            break

# Descomentar para probar:
# contar_caracteres_interactivo()

# Versión 9: Con validación de entrada
print("=== Versión 9: Con Validación ===")
def contar_caracteres_validado():
    """
    Versión con validación y mensajes claros.
    """
    while True:
        cadena = input("Escribe una palabra o cadena de caracteres: ").strip()
        
        if not cadena:
            print("Error: Por favor ingresa al menos un carácter.")
            continuar = input("¿Intentar de nuevo? (s/n): ").lower()
            if continuar != 's':
                break
            continue
        
        total = len(cadena)
        print(f"La cadena '{cadena}' tiene {total} caracteres")
        break

# Versión 10: Comparación de métodos
print("=== Versión 10: Comparación de Métodos ===")
def comparar_metodos(cadena):
    """
    Compara diferentes formas de contar caracteres.
    """
    print(f"\nComparando métodos para: '{cadena}'")
    
    # Método 1: len()
    metodo1 = len(cadena)
    print(f"  len(): {metodo1}")
    
    # Método 2: Bucle
    metodo2 = 0
    for _ in cadena:
        metodo2 += 1
    print(f"  Bucle: {metodo2}")
    
    # Método 3: sum()
    metodo3 = sum(1 for _ in cadena)
    print(f"  sum() con generator: {metodo3}")
    
    print(f"  Todos dan el mismo resultado: {metodo1 == metodo2 == metodo3}")

comparar_metodos("Hola Mundo")
print()

# Ejemplos prácticos
print("=== Ejemplos Prácticos ===")
ejemplos = [
    "Hola",
    "Python",
    "Hola Mundo",
    "123456",
    "¡Hola, mundo!",
    "",
    "   espacios   "
]

print("Contando caracteres en diferentes cadenas:")
for ejemplo in ejemplos:
    if ejemplo:
        total = len(ejemplo)
        print(f"  '{ejemplo}': {total} caracteres")
    else:
        print(f"  (cadena vacía): 0 caracteres")
print()

# Resumen y mejoras
print("=== Resumen de Análisis ===")
print("Código original:")
print("  ✓ Funciona correctamente")
print("  ✓ Código simple y claro")
print("  - Usa .format() en lugar de f-strings")
print("  - No valida entrada vacía")
print("  - No maneja errores")
print("  - Typo: 'progrma' debería ser 'programa'")
print()
print("Mejoras implementadas:")
print("  1. Uso de f-strings (más moderno y legible)")
print("  2. Manejo de errores y validación")
print("  3. Análisis completo de caracteres")
print("  4. Contar con y sin espacios")
print("  5. Contar caracteres únicos")
print("  6. Contar palabras")
print("  7. Funciones reutilizables")
print("  8. Versión interactiva mejorada")
print("  9. Corrección de typos")
print("  10. Comparación de métodos")

# Función principal mejorada
print("\n=== Función Principal Mejorada ===")
def contar_caracteres_mejorado():
    """
    Versión mejorada de la función original.
    """
    try:
        palabra = input("Escribe una palabra o cadena de caracteres: ")
        if not palabra.strip():
            print("Error: No se ingresó ninguna cadena")
            return
        
        total_caracteres = len(palabra)
        print(f"La cadena '{palabra}', tiene {total_caracteres} caracteres")
    except KeyboardInterrupt:
        print("\nOperación cancelada")
    except Exception as e:
        print(f"Error: {e}")

def main():
    """
    Función principal mejorada.
    """
    contar_caracteres_mejorado()
    print('Fin del programa')

if __name__ == '__main__':
    # Descomentar para ejecutar:
    # main()
    pass
