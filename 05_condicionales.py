# Archivo: 05_condicionales.py
# Descripción: Estructuras condicionales (if, elif, else)

print("=== Estructuras Condicionales ===\n")

# If simple
edad = 20
print(f"Edad: {edad}")
if edad >= 18:
    print("Eres mayor de edad\n")

# If-else
numero = 10
print(f"Número: {numero}")
if numero > 0:
    print("El número es positivo")
else:
    print("El número es negativo o cero\n")

# If-elif-else
calificacion = 85
print(f"Calificación: {calificacion}")
if calificacion >= 90:
    print("Calificación: A")
elif calificacion >= 80:
    print("Calificación: B")
elif calificacion >= 70:
    print("Calificación: C")
elif calificacion >= 60:
    print("Calificación: D")
else:
    print("Calificación: F")

print()

# Operadores de comparación
a = 5
b = 10
print("=== Operadores de Comparación ===")
print(f"a = {a}, b = {b}")
print(f"a == b: {a == b}")  # Igual a
print(f"a != b: {a != b}")  # Diferente de
print(f"a < b: {a < b}")    # Menor que
print(f"a > b: {a > b}")    # Mayor que
print(f"a <= b: {a <= b}")  # Menor o igual que
print(f"a >= b: {a >= b}")  # Mayor o igual que

print("\n=== Operadores Lógicos ===")
x = 5
y = 10
z = 15
print(f"x = {x}, y = {y}, z = {z}")
print(f"x < y and y < z: {x < y and y < z}")  # AND
print(f"x > y or y < z: {x > y or y < z}")    # OR
print(f"not (x > y): {not (x > y)}")          # NOT

print("\n=== Condicional Anidado ===")
temperatura = 25
clima = "soleado"
if temperatura > 20:
    if clima == "soleado":
        print("¡Día perfecto para la playa!")
    else:
        print("Hace calor pero el clima no es ideal")
else:
    print("Hace frío, mejor quedarse en casa")
