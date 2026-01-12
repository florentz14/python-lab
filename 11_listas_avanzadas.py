# Archivo: 11_listas_avanzadas.py
# Descripción: Operaciones avanzadas con listas

print("=== Listas Avanzadas en Python ===\n")

# List comprehension básico
print("=== List Comprehension Básico ===")
cuadrados = [x**2 for x in range(1, 6)]
print(f"Cuadrados del 1 al 5: {cuadrados}")

pares = [x for x in range(1, 11) if x % 2 == 0]
print(f"Números pares del 1 al 10: {pares}\n")

# List comprehension con múltiples condiciones
print("=== List Comprehension con Condiciones ===")
numeros = [x for x in range(1, 21) if x % 2 == 0 if x % 3 == 0]
print(f"Números divisibles por 2 y 3: {numeros}\n")

# List comprehension anidado
print("=== List Comprehension Anidado ===")
matriz = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print("Matriz 3x3:")
for fila in matriz:
    print(f"  {fila}")
print()

# Métodos avanzados de listas
print("=== Métodos Avanzados ===")
lista = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Lista original: {lista}")

# Ordenar
lista_ordenada = sorted(lista)
print(f"Lista ordenada (sorted): {lista_ordenada}")
lista.sort()
print(f"Lista después de sort(): {lista}")

lista.reverse()
print(f"Lista después de reverse(): {lista}\n")

# Enumerar
print("=== Enumerar Elementos ===")
frutas = ["manzana", "banana", "naranja"]
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")
print()

# Zip - combinar listas
print("=== Combinar Listas con zip() ===")
nombres = ["Ana", "Carlos", "María"]
edades = [25, 30, 28]
ciudades = ["Madrid", "Barcelona", "Valencia"]

for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"{nombre}, {edad} años, {ciudad}")

lista_combinada = list(zip(nombres, edades, ciudades))
print(f"\nLista combinada: {lista_combinada}\n")

# Map - aplicar función a todos los elementos
print("=== Map - Aplicar Función ===")
numeros = [1, 2, 3, 4, 5]
cuadrados_map = list(map(lambda x: x**2, numeros))
print(f"Números: {numeros}")
print(f"Cuadrados (con map): {cuadrados_map}\n")

# Filter - filtrar elementos
print("=== Filter - Filtrar Elementos ===")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares_filter = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números: {numeros}")
print(f"Pares (con filter): {pares_filter}\n")

# Reduce - reducir a un valor
from functools import reduce
print("=== Reduce - Reducir a un Valor ===")
numeros = [1, 2, 3, 4, 5]
suma_total = reduce(lambda x, y: x + y, numeros)
producto_total = reduce(lambda x, y: x * y, numeros)
print(f"Números: {numeros}")
print(f"Suma total (reduce): {suma_total}")
print(f"Producto total (reduce): {producto_total}\n")

# Slice avanzado
print("=== Slice Avanzado ===")
lista = list(range(10))
print(f"Lista: {lista}")
print(f"Primeros 3: {lista[:3]}")
print(f"Últimos 3: {lista[-3:]}")
print(f"Del índice 2 al 7: {lista[2:7]}")
print(f"Cada 2 elementos: {lista[::2]}")
print(f"Invertida: {lista[::-1]}\n")

# Listas como pilas (stacks)
print("=== Listas como Pilas ===")
pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(f"Pila después de push: {pila}")
ultimo = pila.pop()
print(f"Último elemento (pop): {ultimo}")
print(f"Pila después de pop: {pila}\n")

# Listas como colas (queues)
print("=== Listas como Colas ===")
from collections import deque
cola = deque([1, 2, 3])
cola.append(4)  # Añadir al final
print(f"Cola: {cola}")
primero = cola.popleft()  # Quitar del inicio
print(f"Primer elemento (popleft): {primero}")
print(f"Cola después de popleft: {cola}\n")

# Listas anidadas (matrices básicas)
print("=== Listas Anidadas (Matrices) ===")
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matriz 3x3:")
for fila in matriz:
    print(f"  {fila}")
print(f"Elemento [1][2]: {matriz[1][2]}\n")

# Copiar listas
print("=== Copiar Listas ===")
original = [1, 2, 3, [4, 5]]
copia_superficial = original.copy()  # Shallow copy
import copy
copia_profunda = copy.deepcopy(original)  # Deep copy

original[3].append(6)
print(f"Original: {original}")
print(f"Copia superficial: {copia_superficial}")
print(f"Copia profunda: {copia_profunda}\n")

# Any y All
print("=== Any y All ===")
numeros1 = [2, 4, 6, 8]
numeros2 = [2, 4, 5, 8]
print(f"Lista 1: {numeros1}")
print(f"¿Todos son pares? {all(x % 2 == 0 for x in numeros1)}")
print(f"Lista 2: {numeros2}")
print(f"¿Alguno es par? {any(x % 2 == 0 for x in numeros2)}")
print(f"¿Todos son pares? {all(x % 2 == 0 for x in numeros2)}\n")

# Listas con elementos únicos (usando set)
print("=== Listas con Elementos Únicos ===")
lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 5]
lista_unica = list(dict.fromkeys(lista_con_duplicados))  # Mantiene orden
print(f"Lista original: {lista_con_duplicados}")
print(f"Lista sin duplicados: {lista_unica}")
