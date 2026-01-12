# Archivo: 13_encontrar_numero_mayor.py
# Descripción: Encontrar el número mayor entre varios números

print("=== Encontrar el Número Mayor ===\n")

# Versión 1: Original (con lógica if-elif)
print("=== Versión 1: Original (con if-elif) ===")
def encontrar_mayor_original(num_1, num_2, num_3):
    """
    Encuentra el número mayor entre 3 números usando if-elif.
    Versión basada en lógica condicional.
    """
    if num_1 >= num_2 and num_1 >= num_3:
        return num_1
    elif num_2 >= num_1 and num_2 >= num_3:
        return num_2
    else:
        return num_3

# Ejemplo
numero1 = 15
numero2 = 42
numero3 = 28
resultado = encontrar_mayor_original(numero1, numero2, numero3)
print(f"Números: {numero1}, {numero2}, {numero3}")
print(f"El número mayor es: {resultado}\n")

# Versión 2: Optimizada (usando max())
print("=== Versión 2: Optimizada (usando max()) ===")
def encontrar_mayor_optimizado(num_1, num_2, num_3):
    """
    Encuentra el número mayor usando la función max().
    Versión más concisa y eficiente.
    """
    return max(num_1, num_2, num_3)

resultado = encontrar_mayor_optimizado(numero1, numero2, numero3)
print(f"Números: {numero1}, {numero2}, {numero3}")
print(f"El número mayor es: {resultado}\n")

# Versión 3: Con entrada de usuario (versión original mejorada)
print("=== Versión 3: Con Entrada de Usuario ===")
def encontrar_mayor_con_input():
    """
    Versión interactiva que pide 3 números al usuario.
    Incluye manejo de errores.
    """
    try:
        num_1 = int(input('Ingresa el número 1: '))
        num_2 = int(input('Ingresa el número 2: '))
        num_3 = int(input('Ingresa el número 3: '))
        
        mayor = max(num_1, num_2, num_3)
        print(f'\nLos números ingresados son: {num_1}, {num_2}, {num_3}')
        print(f'El número mayor es: {mayor}')
        return mayor
    except ValueError:
        print("Error: Por favor ingresa números válidos.")
        return None

# Descomentar para probar interactivamente:
# encontrar_mayor_con_input()

# Versión 4: Con múltiples números (lista)
print("=== Versión 4: Con Múltiples Números (Lista) ===")
def encontrar_mayor_lista(numeros):
    """
    Encuentra el número mayor en una lista de números.
    """
    if not numeros:
        return None
    return max(numeros)

lista_numeros = [23, 56, 12, 89, 34, 67, 45]
mayor_lista = encontrar_mayor_lista(lista_numeros)
print(f"Lista de números: {lista_numeros}")
print(f"El número mayor es: {mayor_lista}\n")

# Versión 5: Con múltiples números (argumentos variables)
print("=== Versión 5: Con Argumentos Variables (*args) ===")
def encontrar_mayor_multiple(*numeros):
    """
    Encuentra el número mayor entre cualquier cantidad de números.
    """
    if not numeros:
        return None
    return max(numeros)

resultado_multiple = encontrar_mayor_multiple(10, 25, 5, 30, 15, 20)
print(f"Números: 10, 25, 5, 30, 15, 20")
print(f"El número mayor es: {resultado_multiple}\n")

# Versión 6: Comparación detallada (muestra todos los números ordenados)
print("=== Versión 6: Comparación Detallada ===")
def comparar_numeros(num_1, num_2, num_3):
    """
    Compara 3 números y muestra información detallada.
    """
    numeros = [num_1, num_2, num_3]
    mayor = max(numeros)
    menor = min(numeros)
    ordenados = sorted(numeros, reverse=True)
    
    print(f"Números: {num_1}, {num_2}, {num_3}")
    print(f"Número mayor: {mayor}")
    print(f"Número menor: {menor}")
    print(f"Ordenados de mayor a menor: {ordenados}")
    return mayor

comparar_numeros(42, 15, 28)
print()

# Versión 7: Sin usar max() - usando operador ternario
print("=== Versión 7: Sin max() - Operador Ternario ===")
def encontrar_mayor_ternario(num_1, num_2, num_3):
    """
    Encuentra el mayor usando operador ternario (sin max()).
    """
    mayor = num_1 if num_1 > num_2 else num_2
    mayor = mayor if mayor > num_3 else num_3
    return mayor

resultado = encontrar_mayor_ternario(numero1, numero2, numero3)
print(f"Números: {numero1}, {numero2}, {numero3}")
print(f"El número mayor es: {resultado}\n")

# Versión 8: Con números decimales
print("=== Versión 8: Con Números Decimales ===")
def encontrar_mayor_decimales(*numeros):
    """
    Encuentra el mayor entre números decimales.
    """
    return max(numeros)

decimales = [3.14, 2.71, 1.41, 2.50, 3.00]
mayor_decimal = encontrar_mayor_decimales(*decimales)
print(f"Números decimales: {decimales}")
print(f"El número mayor es: {mayor_decimal}\n")

# Ejemplo práctico: comparación de todas las versiones
print("=== Comparación de Versiones ===")
a, b, c = 25, 42, 18
print(f"Usando números: {a}, {b}, {c}")
print(f"Versión original: {encontrar_mayor_original(a, b, c)}")
print(f"Versión optimizada: {encontrar_mayor_optimizado(a, b, c)}")
print(f"Versión ternaria: {encontrar_mayor_ternario(a, b, c)}")
print(f"Todas las versiones dan el mismo resultado: {encontrar_mayor_original(a, b, c) == encontrar_mayor_optimizado(a, b, c) == encontrar_mayor_ternario(a, b, c)}")
