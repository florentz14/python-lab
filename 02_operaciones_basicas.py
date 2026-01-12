# Archivo: 02_operaciones_basicas.py
# Descripción: Operaciones aritméticas básicas en Python

# Variables numéricas
a = 10
b = 3

print("=== Operaciones Aritméticas Básicas ===")
print(f"a = {a}")
print(f"b = {b}\n")

# Suma
suma = a + b
print(f"Suma: {a} + {b} = {suma}")

# Resta
resta = a - b
print(f"Resta: {a} - {b} = {resta}")

# Multiplicación
multiplicacion = a * b
print(f"Multiplicación: {a} * {b} = {multiplicacion}")

# División
division = a / b
print(f"División: {a} / {b} = {division}")

# División entera (floor division)
division_entera = a // b
print(f"División entera: {a} // {b} = {division_entera}")

# Módulo (resto de la división)
modulo = a % b
print(f"Módulo: {a} % {b} = {modulo}")

# Potencia
potencia = a ** b
print(f"Potencia: {a} ** {b} = {potencia}")

# Operaciones con decimales
print("\n=== Operaciones con Decimales ===")
x = 7.5
y = 2.3
print(f"x = {x}, y = {y}")
print(f"x + y = {x + y}")
print(f"x - y = {x - y}")
print(f"x * y = {x * y}")
print(f"x / y = {x / y}")

# Operaciones combinadas
print("\n=== Operaciones Combinadas ===")
resultado = (a + b) * 2 - 5
print(f"({a} + {b}) * 2 - 5 = {resultado}")

# Orden de operaciones (PEMDAS)
resultado2 = 10 + 5 * 2
print(f"10 + 5 * 2 = {resultado2}")  # 20, no 30

# Incremento y decremento
print("\n=== Incremento y Decremento ===")
numero = 5
print(f"numero inicial: {numero}")
numero += 3  # Equivale a: numero = numero + 3
print(f"después de += 3: {numero}")
numero -= 2  # Equivale a: numero = numero - 2
print(f"después de -= 2: {numero}")
numero *= 2  # Equivale a: numero = numero * 2
print(f"después de *= 2: {numero}")
numero /= 3  # Equivale a: numero = numero / 3
print(f"después de /= 3: {numero}")
