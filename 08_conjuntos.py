# Archivo: 08_conjuntos.py
# Descripción: Trabajar con conjuntos (sets) en Python

print("=== Conjuntos (Sets) en Python ===\n")

# Crear conjuntos
print("=== Crear Conjuntos ===")
frutas = {"manzana", "banana", "naranja", "uva"}
print(f"Conjunto de frutas: {frutas}")

# Crear desde una lista (elimina duplicados)
numeros = [1, 2, 2, 3, 3, 4, 5, 5]
conjunto_numeros = set(numeros)
print(f"Lista: {numeros}")
print(f"Conjunto (sin duplicados): {conjunto_numeros}\n")

# Conjunto vacío
conjunto_vacio = set()  # No usar {} porque crea un diccionario
print(f"Conjunto vacío: {conjunto_vacio}\n")

# Operaciones básicas
print("=== Operaciones Básicas ===")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Agregar elementos
set1.add(6)
print(f"Set 1 después de add(6): {set1}")

# Agregar múltiples elementos
set1.update([7, 8, 9])
print(f"Set 1 después de update([7, 8, 9]): {set1}\n")

# Eliminar elementos
set1.remove(9)  # Lanza error si no existe
print(f"Set 1 después de remove(9): {set1}")

set1.discard(10)  # No lanza error si no existe
print(f"Set 1 después de discard(10): {set1}")

elemento = set1.pop()  # Elimina y retorna un elemento aleatorio
print(f"Elemento eliminado con pop(): {elemento}")
print(f"Set 1 después de pop(): {set1}\n")

# Operaciones de conjuntos
print("=== Operaciones de Conjuntos ===")
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(f"Conjunto A: {A}")
print(f"Conjunto B: {B}\n")

# Unión
union = A | B  # o A.union(B)
print(f"Unión (A | B): {union}")

# Intersección
interseccion = A & B  # o A.intersection(B)
print(f"Intersección (A & B): {interseccion}")

# Diferencia
diferencia = A - B  # o A.difference(B)
print(f"Diferencia (A - B): {diferencia}")

# Diferencia simétrica
diferencia_simetrica = A ^ B  # o A.symmetric_difference(B)
print(f"Diferencia simétrica (A ^ B): {diferencia_simetrica}\n")

# Verificar subconjuntos y superconjuntos
print("=== Subconjuntos y Superconjuntos ===")
C = {2, 3}
D = {1, 2, 3, 4, 5, 6}
print(f"Conjunto C: {C}")
print(f"Conjunto D: {D}")
print(f"C es subconjunto de A: {C.issubset(A)}")
print(f"A es superconjunto de C: {A.issuperset(C)}")
print(f"A y B son disjuntos: {A.isdisjoint({10, 11, 12})}\n")

# Recorrer conjunto
print("=== Recorrer Conjunto ===")
colores = {"rojo", "verde", "azul", "amarillo"}
print("Colores en el conjunto:")
for color in colores:
    print(f"  - {color}")

print()

# Set comprehension
print("=== Set Comprehension ===")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = {n for n in numeros if n % 2 == 0}
print(f"Números pares: {pares}")

cuadrados = {n**2 for n in range(1, 6)}
print(f"Cuadrados del 1 al 5: {cuadrados}\n")

# Ejemplo práctico: eliminar duplicados de una lista
print("=== Ejemplo Práctico: Eliminar Duplicados ===")
lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]
lista_sin_duplicados = list(set(lista_con_duplicados))
print(f"Lista original: {lista_con_duplicados}")
print(f"Lista sin duplicados: {lista_sin_duplicados}\n")

# Operaciones in-place
print("=== Operaciones In-Place ===")
X = {1, 2, 3, 4}
Y = {3, 4, 5, 6}
print(f"X: {X}, Y: {Y}")

X.update(Y)  # X = X | Y
print(f"X después de update(Y): {X}")

X = {1, 2, 3, 4}
X.intersection_update(Y)  # X = X & Y
print(f"X después de intersection_update(Y): {X}")

X = {1, 2, 3, 4}
X.difference_update(Y)  # X = X - Y
print(f"X después de difference_update(Y): {X}")
