# Archivo: 19_anio_bisiesto.py
# Descripción: Determinar si un año es bisiesto según el calendario gregoriano

print("=== Años Bisiestos (Calendario Gregoriano) ===\n")

# Versión 1: Forma 1 (Original)
print("=== Versión 1: Forma 1 (Original) ===")
def es_bisiesto_forma1(year_):
    """
    Primera forma del código original.
    Usa múltiples if-elif anidados.
    """
    if year_ > 1582:
        if year_ % 4 != 0:
            return 'Año común'
        elif year_ % 100 != 0:
            return 'Año bisiesto'
        elif year_ % 400 != 0:
            return 'Año común'
        else:
            return 'Año bisiesto'
    else:
        return 'No está dentro del período del calendario gregoriano'

# Pruebas
print("Pruebas de la forma 1:")
test_cases = [2000, 2015, 1999, 1996, 1580]
for year in test_cases:
    resultado = es_bisiesto_forma1(year)
    print(f"  {year}: {resultado}")
print()

# Versión 2: Forma 2 (Original)
print("=== Versión 2: Forma 2 (Original) ===")
def is_leap(year):
    """
    Segunda forma del código original.
    Más concisa pero no valida el período gregoriano.
    """
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    return leap

print("Pruebas de la forma 2 (solo retorna True/False):")
for year in test_cases:
    resultado = is_leap(year)
    print(f"  {year}: {resultado}")
print()

# Versión 3: Forma 3 (Original)
print("=== Versión 3: Forma 3 (Original) ===")
def es_bisiesto_forma3(anio):
    """
    Tercera forma del código original.
    Más concisa usando operadores lógicos.
    No valida el período gregoriano.
    """
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        return True
    else:
        return False

print("Pruebas de la forma 3 (solo retorna True/False):")
for year in test_cases:
    resultado = es_bisiesto_forma3(year)
    print(f"  {year}: {resultado}")
print()

# Versión 4: Optimizada Completa (Recomendada)
print("=== Versión 4: Optimizada Completa (Recomendada) ===")
def es_bisiesto_completo(anio):
    """
    Versión optimizada que incluye:
    - Validación del período gregoriano (desde 1582)
    - Lógica correcta para años bisiestos
    - Mensajes claros en español
    """
    # Validar período gregoriano
    if anio < 1582:
        return 'No está dentro del período del calendario gregoriano'
    
    # Reglas para años bisiestos:
    # 1. No divisible por 4 -> común
    # 2. Divisible por 4 pero no por 100 -> bisiesto
    # 3. Divisible por 100 pero no por 400 -> común
    # 4. Divisible por 400 -> bisiesto
    
    if anio % 4 != 0:
        return 'Año común'
    elif anio % 100 != 0:
        return 'Año bisiesto'
    elif anio % 400 != 0:
        return 'Año común'
    else:
        return 'Año bisiesto'

print("Pruebas de la versión optimizada completa:")
for year in test_cases:
    resultado = es_bisiesto_completo(year)
    print(f"  {year}: {resultado}")

# Verificar datos de prueba
print("\nVerificación de datos de prueba:")
esperados = {
    2000: 'Año bisiesto',
    2015: 'Año común',
    1999: 'Año común',
    1996: 'Año bisiesto',
    1580: 'No está dentro del período del calendario gregoriano'
}
for year, esperado in esperados.items():
    resultado = es_bisiesto_completo(year)
    estado = "✓" if resultado == esperado else "✗"
    print(f"  {estado} {year}: {resultado} (esperado: {esperado})")
print()

# Versión 5: Con función booleana + validación
print("=== Versión 5: Función Booleana + Validación ===")
def es_bisiesto_booleano(anio):
    """
    Retorna True/False para años bisiestos.
    Lanza ValueError si está fuera del período gregoriano.
    """
    if anio < 1582:
        raise ValueError('No está dentro del período del calendario gregoriano')
    
    # Lógica optimizada: (divisible por 4) Y (no divisible por 100 O divisible por 400)
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def verificar_bisiesto(anio):
    """
    Función wrapper que maneja errores y retorna mensaje.
    """
    try:
        if es_bisiesto_booleano(anio):
            return 'Año bisiesto'
        else:
            return 'Año común'
    except ValueError as e:
        return str(e)

print("Pruebas de la versión booleana:")
for year in test_cases:
    resultado = verificar_bisiesto(year)
    print(f"  {year}: {resultado}")
print()

# Versión 6: Versión compacta (una línea)
print("=== Versión 6: Versión Compacta ===")
def es_bisiesto_compacto(anio):
    """
    Versión muy compacta usando expresión lógica.
    """
    if anio < 1582:
        return 'No está dentro del período del calendario gregoriano'
    
    es_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
    return 'Año bisiesto' if es_bisiesto else 'Año común'

print("Pruebas de la versión compacta:")
for year in test_cases:
    resultado = es_bisiesto_compacto(year)
    print(f"  {year}: {resultado}")
print()

# Versión 7: Con entrada de usuario mejorada
print("=== Versión 7: Con Entrada de Usuario Mejorada ===")
def verificar_anio_bisiesto():
    """
    Versión interactiva mejorada con manejo de errores.
    """
    while True:
        try:
            anio = int(input("Introduzca un año: "))
            
            if anio < 1582:
                print(f'{anio}: No está dentro del período del calendario gregoriano')
            elif (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
                print(f'{anio}: Año bisiesto')
            else:
                print(f'{anio}: Año común')
            
            continuar = input("\n¿Verificar otro año? (s/n): ").lower()
            if continuar != 's':
                break
        
        except ValueError:
            print("Error: Por favor ingrese un número entero válido.")
        except KeyboardInterrupt:
            print("\nSaliendo...")
            break

# Descomentar para probar interactivamente:
# verificar_anio_bisiesto()

# Versión 8: Listar años bisiestos en un rango
print("=== Versión 8: Listar Años Bisiestos en un Rango ===")
def listar_anios_bisiestos(anio_inicio, anio_fin):
    """
    Lista todos los años bisiestos en un rango dado.
    """
    if anio_inicio < 1582:
        print(f"Advertencia: El año {anio_inicio} está fuera del período gregoriano")
        anio_inicio = 1582
    
    bisiestos = []
    for anio in range(anio_inicio, anio_fin + 1):
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            bisiestos.append(anio)
    
    return bisiestos

print("Años bisiestos del 1990 al 2000:")
bisiestos = listar_anios_bisiestos(1990, 2000)
print(f"  {bisiestos}")
print()

# Versión 9: Con explicación de las reglas
print("=== Versión 9: Con Explicación de Reglas ===")
def es_bisiesto_con_explicacion(anio):
    """
    Versión que explica por qué un año es o no bisiesto.
    """
    if anio < 1582:
        return 'No está dentro del período del calendario gregoriano'
    
    explicacion = []
    
    if anio % 4 != 0:
        explicacion.append(f"{anio} no es divisible por 4")
        return f'Año común ({", ".join(explicacion)})'
    
    explicacion.append(f"{anio} es divisible por 4")
    
    if anio % 100 != 0:
        explicacion.append(f"{anio} no es divisible por 100")
        return f'Año bisiesto ({", ".join(explicacion)})'
    
    explicacion.append(f"{anio} es divisible por 100")
    
    if anio % 400 != 0:
        explicacion.append(f"{anio} no es divisible por 400")
        return f'Año común ({", ".join(explicacion)})'
    
    explicacion.append(f"{anio} es divisible por 400")
    return f'Año bisiesto ({", ".join(explicacion)})'

print("Versión con explicación:")
for year in [2000, 2015, 1996]:
    resultado = es_bisiesto_con_explicacion(year)
    print(f"  {resultado}")
print()

# Versión 10: Comparación de todas las formas
print("=== Versión 10: Comparación de Todas las Formas ===")
def comparar_formas(anio):
    """
    Compara todas las formas de calcular años bisiestos.
    """
    print(f"\nComparando formas para el año {anio}:")
    
    # Forma 1
    resultado1 = es_bisiesto_forma1(anio)
    print(f"  Forma 1: {resultado1}")
    
    # Forma 2 (solo booleano)
    if anio >= 1582:
        resultado2 = is_leap(anio)
        print(f"  Forma 2: {resultado2}")
    
    # Forma 3 (solo booleano)
    if anio >= 1582:
        resultado3 = es_bisiesto_forma3(anio)
        print(f"  Forma 3: {resultado3}")
    
    # Versión optimizada
    resultado4 = es_bisiesto_completo(anio)
    print(f"  Optimizada: {resultado4}")
    
    # Versión compacta
    resultado5 = es_bisiesto_compacto(anio)
    print(f"  Compacta: {resultado5}")

for year in [2000, 2015, 1580]:
    comparar_formas(year)

print()

# Resumen y mejoras
print("=== Resumen de Análisis ===")
print("Forma 1 (Original):")
print("  ✓ Valida período gregoriano")
print("  ✓ Lógica correcta")
print("  - Código más verboso")
print("  - Mensajes en formato inconsistentes")
print()
print("Forma 2 (Original):")
print("  ✓ Lógica correcta")
print("  ✗ No valida período gregoriano")
print("  ✗ Solo retorna booleano, no mensaje")
print("  - Código anidado")
print()
print("Forma 3 (Original):")
print("  ✓ Lógica correcta y concisa")
print("  ✗ No valida período gregoriano")
print("  ✗ Solo retorna booleano, no mensaje")
print()
print("Mejoras implementadas:")
print("  1. Validación del período gregoriano (1582+)")
print("  2. Mensajes claros en español")
print("  3. Lógica optimizada y clara")
print("  4. Manejo de errores")
print("  5. Versiones compactas y explicativas")
print("  6. Funciones para listar años bisiestos")
print("  7. Comparación de métodos")

# Ejemplos adicionales
print("\n=== Ejemplos Adicionales ===")
ejemplos_adicionales = [1600, 1700, 1800, 1900, 2000, 2100]
print("Años divisibles por 100 y 400:")
for year in ejemplos_adicionales:
    resultado = es_bisiesto_completo(year)
    print(f"  {year}: {resultado}")
