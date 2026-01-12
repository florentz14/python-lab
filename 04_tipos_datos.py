# Archivo: 04_tipos_datos.py
# Descripción: Tipos de datos en Python

print("=== Tipos de Datos en Python ===\n")

# Enteros (int)
numero_entero = 42
print(f"Entero: {numero_entero}")
print(f"Tipo: {type(numero_entero)}\n")

# Flotantes (float)
numero_decimal = 3.14
print(f"Flotante: {numero_decimal}")
print(f"Tipo: {type(numero_decimal)}\n")

# Strings (str)
texto = "Hola, Python"
print(f"String: {texto}")
print(f"Tipo: {type(texto)}\n")

# Booleanos (bool)
verdadero = True
falso = False
print(f"Booleano verdadero: {verdadero}")
print(f"Booleano falso: {falso}")
print(f"Tipo: {type(verdadero)}\n")

# Listas (list)
lista = [1, 2, 3, 4, 5]
print(f"Lista: {lista}")
print(f"Tipo: {type(lista)}\n")

# Tuplas (tuple)
tupla = (1, 2, 3)
print(f"Tupla: {tupla}")
print(f"Tipo: {type(tupla)}\n")

# Diccionarios (dict)
diccionario = {"nombre": "Juan", "edad": 25}
print(f"Diccionario: {diccionario}")
print(f"Tipo: {type(diccionario)}\n")

# Conjuntos (set)
conjunto = {1, 2, 3, 4, 5}
print(f"Conjunto: {conjunto}")
print(f"Tipo: {type(conjunto)}\n")

# None (NoneType)
nada = None
print(f"None: {nada}")
print(f"Tipo: {type(nada)}\n")

# Conversión de tipos
print("=== Conversión de Tipos ===")
numero_como_string = "123"
numero_convertido = int(numero_como_string)
print(f"String '{numero_como_string}' convertido a int: {numero_convertido}")

decimal_como_string = "3.14"
decimal_convertido = float(decimal_como_string)
print(f"String '{decimal_como_string}' convertido a float: {decimal_convertido}")

numero_a_string = str(456)
print(f"Número 456 convertido a string: '{numero_a_string}'")
