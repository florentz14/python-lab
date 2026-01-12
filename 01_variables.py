# Archivo: 01_variables.py
# Descripción: Ejemplos básicos de variables en Python

# Variables de diferentes tipos
nombre = "Juan"
edad = 25
altura = 1.75
es_estudiante = True

# Imprimir variables individuales
print("=== Imprimir Variables Individuales ===")
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("Es estudiante:", es_estudiante)

# Imprimir múltiples variables en una línea
print("\n=== Múltiples Variables en una Línea ===")
print(f"Nombre: {nombre}, Edad: {edad}, Altura: {altura}m")

# Usando format()
print("\n=== Usando format() ===")
print("Mi nombre es {} y tengo {} años".format(nombre, edad))

# Usando % (formato antiguo)
print("\n=== Usando % (formato antiguo) ===")
print("Altura: %.2f metros" % altura)

# Concatenar strings
print("\n=== Concatenar Strings ===")
mensaje = "Hola, me llamo " + nombre + " y tengo " + str(edad) + " años"
print(mensaje)

# Variables en múltiples líneas
print("\n=== Variables en Múltiples Líneas ===")
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
