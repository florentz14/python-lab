# Archivo: 07_diccionarios.py
# Descripción: Trabajar con diccionarios en Python

print("=== Diccionarios en Python ===\n")

# Crear un diccionario
print("=== Crear Diccionarios ===")
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid",
    "profesion": "Desarrollador"
}
print(f"Diccionario persona: {persona}\n")

# Acceder a valores
print("=== Acceder a Valores ===")
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona.get('edad')}")
print(f"Ciudad: {persona.get('ciudad', 'No especificada')}")  # Con valor por defecto
print()

# Modificar valores
print("=== Modificar Valores ===")
persona["edad"] = 26
persona["salario"] = 50000  # Agregar nueva clave
print(f"Diccionario actualizado: {persona}\n")

# Obtener claves, valores y items
print("=== Claves, Valores e Items ===")
print(f"Claves: {list(persona.keys())}")
print(f"Valores: {list(persona.values())}")
print(f"Items: {list(persona.items())}\n")

# Recorrer diccionario
print("=== Recorrer Diccionario ===")
print("Recorrer por claves:")
for clave in persona:
    print(f"  {clave}: {persona[clave]}")

print("\nRecorrer por items:")
for clave, valor in persona.items():
    print(f"  {clave}: {valor}")

print()

# Diccionario anidado
print("=== Diccionarios Anidados ===")
estudiantes = {
    "estudiante1": {
        "nombre": "Ana",
        "notas": [8, 9, 7, 10]
    },
    "estudiante2": {
        "nombre": "Carlos",
        "notas": [6, 7, 8, 9]
    }
}
print(f"Estudiantes: {estudiantes}")
print(f"Nombre estudiante1: {estudiantes['estudiante1']['nombre']}")
print(f"Notas estudiante1: {estudiantes['estudiante1']['notas']}\n")

# Métodos útiles
print("=== Métodos Útiles ===")
productos = {"manzana": 1.50, "banana": 0.80, "naranja": 1.20}
print(f"Productos: {productos}")

# pop() - eliminar y retornar
precio = productos.pop("banana")
print(f"Precio eliminado: {precio}")
print(f"Productos después de pop: {productos}")

# update() - actualizar con otro diccionario
productos.update({"uva": 2.50, "pera": 1.30})
print(f"Productos después de update: {productos}")

# clear() - limpiar diccionario
productos_copia = productos.copy()
productos_copia.clear()
print(f"Productos copia después de clear: {productos_copia}\n")

# Comprobar si existe una clave
print("=== Verificar Existencia ===")
print(f"'manzana' in productos: {'manzana' in productos}")
print(f"'mango' in productos: {'mango' in productos}\n")

# Diccionario con fromkeys()
print("=== fromkeys() ===")
nuevas_claves = ["a", "b", "c"]
diccionario_nuevo = dict.fromkeys(nuevas_claves, 0)
print(f"Diccionario con fromkeys: {diccionario_nuevo}\n")

# Diccionario comprehension
print("=== Dictionary Comprehension ===")
numeros = [1, 2, 3, 4, 5]
cuadrados = {n: n**2 for n in numeros}
print(f"Números y sus cuadrados: {cuadrados}")

pares_cuadrados = {n: n**2 for n in numeros if n % 2 == 0}
print(f"Cuadrados de números pares: {pares_cuadrados}")
