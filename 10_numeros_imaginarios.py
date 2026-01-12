# Archivo: 10_numeros_imaginarios.py
# Descripción: Trabajar con números complejos (imaginarios) en Python

import cmath
import math

print("=== Números Complejos (Imaginarios) en Python ===\n")

# Crear números complejos
print("=== Crear Números Complejos ===")
# Método 1: usando j (no i)
z1 = 3 + 4j
z2 = 2 - 5j
z3 = complex(1, 2)  # 1 + 2j
print(f"z1 = {z1}")
print(f"z2 = {z2}")
print(f"z3 = {z3}\n")

# Partes del número complejo
print("=== Partes del Número Complejo ===")
z = 3 + 4j
print(f"z = {z}")
print(f"Parte real: {z.real}")
print(f"Parte imaginaria: {z.imag}")
print(f"Conjugado: {z.conjugate()}\n")

# Operaciones básicas
print("=== Operaciones Básicas ===")
a = 2 + 3j
b = 1 - 2j
print(f"a = {a}")
print(f"b = {b}")

suma = a + b
print(f"Suma (a + b): {suma}")

resta = a - b
print(f"Resta (a - b): {resta}")

multiplicacion = a * b
print(f"Multiplicación (a * b): {multiplicacion}")

division = a / b
print(f"División (a / b): {division}\n")

# Módulo y fase (forma polar)
print("=== Módulo y Fase ===")
z = 3 + 4j
modulo = abs(z)  # o math.sqrt(z.real**2 + z.imag**2)
fase = cmath.phase(z)  # en radianes
fase_grados = math.degrees(fase)

print(f"z = {z}")
print(f"Módulo |z| = {modulo}")
print(f"Fase (radianes) = {fase:.4f}")
print(f"Fase (grados) = {fase_grados:.2f}°\n")

# Forma polar y rectangular
print("=== Conversión entre Formas ===")
z = 1 + 1j
# Convertir a forma polar (módulo, fase)
polar = cmath.polar(z)
print(f"z = {z}")
print(f"Forma polar (módulo, fase): {polar}")

# Convertir de forma polar a rectangular
rectangular = cmath.rect(polar[0], polar[1])
print(f"De polar a rectangular: {rectangular}\n")

# Funciones matemáticas con números complejos
print("=== Funciones Matemáticas ===")
z = 1 + 2j
print(f"z = {z}")
print(f"Raíz cuadrada: {cmath.sqrt(z)}")
print(f"Exponencial: {cmath.exp(z)}")
print(f"Logaritmo natural: {cmath.log(z)}")
print(f"Seno: {cmath.sin(z)}")
print(f"Coseno: {cmath.cos(z)}\n")

# Potencias de i
print("=== Potencias de i ===")
i = 1j
print(f"i = {i}")
print(f"i² = {i**2}")
print(f"i³ = {i**3}")
print(f"i⁴ = {i**4}")
print(f"i⁵ = {i**5}\n")

# Ejemplo: resolver ecuación cuadrática con números complejos
print("=== Ecuación Cuadrática ===")
# x² + 2x + 5 = 0
a_coef = 1
b_coef = 2
c_coef = 5

discriminante = b_coef**2 - 4*a_coef*c_coef
print(f"Ecuación: {a_coef}x² + {b_coef}x + {c_coef} = 0")
print(f"Discriminante: {discriminante}")

if discriminante < 0:
    raiz1 = (-b_coef + cmath.sqrt(discriminante)) / (2*a_coef)
    raiz2 = (-b_coef - cmath.sqrt(discriminante)) / (2*a_coef)
    print(f"Raíz 1: {raiz1}")
    print(f"Raíz 2: {raiz2}\n")

# Operaciones con listas de números complejos
print("=== Operaciones con Listas ===")
numeros_complejos = [1+2j, 3+4j, 5+6j]
print(f"Números complejos: {numeros_complejos}")

suma_total = sum(numeros_complejos)
print(f"Suma total: {suma_total}")

modulos = [abs(z) for z in numeros_complejos]
print(f"Módulos: {modulos}\n")

# Representación en el plano complejo (concepto)
print("=== Representación en el Plano Complejo ===")
z = 3 + 4j
print(f"z = {z}")
print(f"Coordenadas: (real={z.real}, imaginaria={z.imag})")
print(f"En el plano complejo: punto en ({z.real}, {z.imag})")
print(f"Distancia al origen: {abs(z)}")
print(f"Ángulo desde el eje real: {math.degrees(cmath.phase(z)):.2f}°\n")

# Números complejos especiales
print("=== Números Complejos Especiales ==")
print(f"0 + 0j = {0+0j}")
print(f"1 + 0j = {1+0j}")
print(f"0 + 1j = {0+1j}")
print(f"-1 + 0j = {-1+0j}")
print(f"0 - 1j = {0-1j}\n")

# Verificar propiedades
print("=== Verificar Propiedades ===")
z1 = 2 + 3j
z2 = 4 - 5j
print(f"z1 = {z1}, z2 = {z2}")
print(f"Conjugado de (z1 + z2) = conjugado(z1) + conjugado(z2): {(z1+z2).conjugate() == z1.conjugate() + z2.conjugate()}")
print(f"|z1 * z2| = |z1| * |z2|: {abs(z1*z2) == abs(z1)*abs(z2)}")
