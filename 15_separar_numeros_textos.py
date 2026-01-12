# Archivo: 15_separar_numeros_textos.py
# Descripción: Separar datos numéricos de textos en una lista

print("=== Separar Números de Textos ===\n")

# Versión 1: Original
print("=== Versión 1: Original ===")
def separar_datos_original(datos):
    """
    Separa números de textos usando type() == int.
    Versión original del código.
    """
    datos_numeros = []
    datos_textos = []
    
    for dato in datos:
        if type(dato) == int:
            datos_numeros.append(dato)
        else:
            datos_textos.append(dato)
    
    print(f"Datos numéricos: {datos_numeros}")
    print(f"Datos textos: {datos_textos}")
    return datos_numeros, datos_textos

datos = ['Ronaldo', 'Jimenez', 7, 27, 'COL', 1999]
print(f"Datos originales: {datos}")
separar_datos_original(datos)
print()

# Versión 2: Optimizada (usando isinstance)
print("=== Versión 2: Optimizada (usando isinstance) ===")
def separar_datos_optimizada(datos):
    """
    Versión optimizada usando isinstance() en lugar de type() == int.
    Mejor práctica en Python.
    """
    datos_numeros = []
    datos_textos = []
    
    for dato in datos:
        if isinstance(dato, int):
            datos_numeros.append(dato)
        else:
            datos_textos.append(dato)
    
    print(f"Datos numéricos: {datos_numeros}")
    print(f"Datos textos: {datos_textos}")
    return datos_numeros, datos_textos

datos = ['Ronaldo', 'Jimenez', 7, 27, 'COL', 1999]
print(f"Datos originales: {datos}")
separar_datos_optimizada(datos)
print()

# Versión 3: Con List Comprehension
print("=== Versión 3: Con List Comprehension ===")
def separar_datos_comprehension(datos):
    """
    Versión concisa usando list comprehension.
    Más pythónica y eficiente.
    """
    datos_numeros = [dato for dato in datos if isinstance(dato, int)]
    datos_textos = [dato for dato in datos if not isinstance(dato, int)]
    
    print(f"Datos numéricos: {datos_numeros}")
    print(f"Datos textos: {datos_textos}")
    return datos_numeros, datos_textos

datos = ['Ronaldo', 'Jimenez', 7, 27, 'COL', 1999]
print(f"Datos originales: {datos}")
separar_datos_comprehension(datos)
print()

# Versión 4: Incluyendo float y otros tipos numéricos
print("=== Versión 4: Todos los Tipos Numéricos ===")
def separar_datos_numericos_completos(datos):
    """
    Separa todos los tipos numéricos (int, float, complex).
    """
    datos_numeros = []
    datos_textos = []
    
    for dato in datos:
        if isinstance(dato, (int, float, complex)):
            datos_numeros.append(dato)
        else:
            datos_textos.append(dato)
    
    print(f"Datos numéricos: {datos_numeros}")
    print(f"Datos textos: {datos_textos}")
    return datos_numeros, datos_textos

datos_mixtos = ['Ronaldo', 'Jimenez', 7, 27.5, 'COL', 1999, 3.14, 2+3j]
print(f"Datos originales: {datos_mixtos}")
separar_datos_numericos_completos(datos_mixtos)
print()

# Versión 5: Retornando diccionario
print("=== Versión 5: Retornando Diccionario ===")
def separar_datos_diccionario(datos):
    """
    Retorna un diccionario con las listas separadas.
    """
    numeros = [dato for dato in datos if isinstance(dato, (int, float))]
    textos = [dato for dato in datos if not isinstance(dato, (int, float))]
    
    resultado = {
        'numeros': numeros,
        'textos': textos
    }
    
    print(f"Resultado: {resultado}")
    return resultado

datos = ['Ronaldo', 'Jimenez', 7, 27, 'COL', 1999]
print(f"Datos originales: {datos}")
separar_datos_diccionario(datos)
print()

# Versión 6: Separar por múltiples tipos
print("=== Versión 6: Separar por Múltiples Tipos ===")
def separar_por_tipos(datos):
    """
    Separa datos en múltiples categorías: números, textos, booleanos, None, etc.
    """
    numeros = []
    textos = []
    booleanos = []
    otros = []
    
    for dato in datos:
        if isinstance(dato, (int, float, complex)):
            numeros.append(dato)
        elif isinstance(dato, str):
            textos.append(dato)
        elif isinstance(dato, bool):
            booleanos.append(dato)
        else:
            otros.append(dato)
    
    resultado = {
        'numeros': numeros,
        'textos': textos,
        'booleanos': booleanos,
        'otros': otros
    }
    
    print("Separación por tipos:")
    for tipo, valores in resultado.items():
        if valores:
            print(f"  {tipo.capitalize()}: {valores}")
    
    return resultado

datos_complejos = ['Ronaldo', 'Jimenez', 7, 27, 'COL', 1999, True, False, None, [1, 2]]
print(f"Datos originales: {datos_complejos}")
separar_por_tipos(datos_complejos)
print()

# Versión 7: Función genérica con filtro personalizado
print("=== Versión 7: Filtro Personalizado ===")
def separar_con_filtro(datos, filtro):
    """
    Separa datos usando una función de filtro personalizada.
    """
    cumple_filtro = [dato for dato in datos if filtro(dato)]
    no_cumple = [dato for dato in datos if not filtro(dato)]
    
    return cumple_filtro, no_cumple

datos = ['Ronaldo', 'Jimenez', 7, 27, 'COL', 1999]
print(f"Datos originales: {datos}")

# Filtrar números
numeros, no_numeros = separar_con_filtro(datos, lambda x: isinstance(x, int))
print(f"Números (con filtro): {numeros}")
print(f"No números: {no_numeros}")

# Filtrar strings que empiezan con mayúscula
mayusculas, otros = separar_con_filtro(datos, lambda x: isinstance(x, str) and x[0].isupper())
print(f"Strings con mayúscula: {mayusculas}")
print(f"Otros: {otros}")
print()

# Versión 8: Usando filter() y map()
print("=== Versión 8: Usando filter() ===")
def separar_con_filter(datos):
    """
    Usando las funciones filter() de Python.
    """
    datos_numeros = list(filter(lambda x: isinstance(x, int), datos))
    datos_textos = list(filter(lambda x: not isinstance(x, int), datos))
    
    print(f"Datos numéricos: {datos_numeros}")
    print(f"Datos textos: {datos_textos}")
    return datos_numeros, datos_textos

datos = ['Ronaldo', 'Jimenez', 7, 27, 'COL', 1999]
print(f"Datos originales: {datos}")
separar_con_filter(datos)
print()

# Versión 9: Separar y convertir strings numéricos
print("=== Versión 9: Convertir Strings Numéricos ===")
def separar_y_convertir(datos):
    """
    Separa números y textos, convirtiendo strings que son números.
    """
    datos_numeros = []
    datos_textos = []
    
    for dato in datos:
        if isinstance(dato, (int, float)):
            datos_numeros.append(dato)
        elif isinstance(dato, str):
            # Intentar convertir strings numéricos
            try:
                if '.' in dato:
                    numero = float(dato)
                else:
                    numero = int(dato)
                datos_numeros.append(numero)
            except ValueError:
                datos_textos.append(dato)
        else:
            datos_textos.append(dato)
    
    print(f"Datos numéricos (convertidos): {datos_numeros}")
    print(f"Datos textos: {datos_textos}")
    return datos_numeros, datos_textos

datos_con_strings_numericos = ['Ronaldo', 'Jimenez', '7', '27', 'COL', '1999', 3.14]
print(f"Datos originales: {datos_con_strings_numericos}")
separar_y_convertir(datos_con_strings_numericos)
print()

# Versión 10: Con estadísticas
print("=== Versión 10: Con Estadísticas ===")
def separar_con_estadisticas(datos):
    """
    Separa números de textos y calcula estadísticas básicas.
    """
    datos_numeros = [dato for dato in datos if isinstance(dato, (int, float))]
    datos_textos = [dato for dato in datos if not isinstance(dato, (int, float))]
    
    print(f"Datos numéricos: {datos_numeros}")
    print(f"Datos textos: {datos_textos}")
    
    if datos_numeros:
        print(f"\nEstadísticas de números:")
        print(f"  Cantidad: {len(datos_numeros)}")
        print(f"  Suma: {sum(datos_numeros)}")
        print(f"  Promedio: {sum(datos_numeros)/len(datos_numeros):.2f}")
        print(f"  Máximo: {max(datos_numeros)}")
        print(f"  Mínimo: {min(datos_numeros)}")
    
    if datos_textos:
        print(f"\nEstadísticas de textos:")
        print(f"  Cantidad: {len(datos_textos)}")
        print(f"  Longitud promedio: {sum(len(str(t)) for t in datos_textos)/len(datos_textos):.2f}")
    
    return datos_numeros, datos_textos

datos = ['Ronaldo', 'Jimenez', 7, 27, 'COL', 1999]
print(f"Datos originales: {datos}")
separar_con_estadisticas(datos)
print()

# Resumen de mejoras
print("=== Resumen de Mejoras ===")
print("Mejoras implementadas:")
print("  1. Usar isinstance() en lugar de type() == int (mejor práctica)")
print("  2. List comprehension para código más conciso")
print("  3. Soporte para múltiples tipos numéricos (int, float, complex)")
print("  4. Separación por múltiples categorías")
print("  5. Filtros personalizados")
print("  6. Conversión de strings numéricos")
print("  7. Cálculo de estadísticas")
print("  8. Retorno estructurado (diccionarios)")

# Comparación de métodos
print("\n=== Comparación de Métodos ===")
datos_test = ['Ronaldo', 'Jimenez', 7, 27, 'COL', 1999]
print(f"Datos de prueba: {datos_test}")

# Método 1: Original
numeros1, textos1 = separar_datos_original(datos_test.copy())
print(f"  Original: {len(numeros1)} números, {len(textos1)} textos")

# Método 2: Comprehension
numeros2, textos2 = separar_datos_comprehension(datos_test.copy())
print(f"  Comprehension: {len(numeros2)} números, {len(textos2)} textos")

# Método 3: Filter
numeros3, textos3 = separar_con_filter(datos_test.copy())
print(f"  Filter: {len(numeros3)} números, {len(textos3)} textos")

print("\nTodos los métodos dan el mismo resultado!")
