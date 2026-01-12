# Archivo: 03_entrada_salida.py
# Descripción: Entrada y salida de datos (input/output)

print("=== Entrada y Salida de Datos ===\n")

# Entrada de texto
nombre = input("Por favor, ingresa tu nombre: ")
print(f"Hola, {nombre}!\n")

# Entrada numérica (necesita conversión)
edad = input("¿Cuántos años tienes? ")
edad = int(edad)  # Convertir string a entero
print(f"Tienes {edad} años\n")

# Entrada de número decimal
altura = float(input("¿Cuál es tu altura en metros? "))
print(f"Tu altura es {altura} metros\n")

# Múltiples entradas
print("=== Calculadora Simple ===")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"\nResultados:")
print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} * {num2} = {multiplicacion}")
print(f"{num1} / {num2} = {division}")

# Ejemplo de salida con formato
print("\n=== Formato de Salida ===")
print("Resultado formateado con 2 decimales:")
print(f"División: {division:.2f}")
