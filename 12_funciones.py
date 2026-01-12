# Archivo: 12_funciones.py
# Descripción: Funciones en Python

print("=== Funciones en Python ===\n")

# Función básica
print("=== Función Básica ===")
def saludar():
    return "¡Hola!"

mensaje = saludar()
print(f"Resultado: {mensaje}\n")

# Función con parámetros
print("=== Función con Parámetros ===")
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(f"sumar(5, 3) = {resultado}\n")

# Función con parámetros por defecto
print("=== Parámetros por Defecto ===")
def saludar_persona(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}!"

print(saludar_persona("Juan"))
print(saludar_persona("María", "Buenos días"))
print()

# Función con argumentos variables (*args)
print("=== Argumentos Variables (*args) ===")
def sumar_numeros(*args):
    return sum(args)

print(f"sumar_numeros(1, 2, 3) = {sumar_numeros(1, 2, 3)}")
print(f"sumar_numeros(1, 2, 3, 4, 5) = {sumar_numeros(1, 2, 3, 4, 5)}\n")

# Función con keyword arguments (**kwargs)
print("=== Keyword Arguments (**kwargs) ===")
def imprimir_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"  {clave}: {valor}")

print("Información:")
imprimir_info(nombre="Juan", edad=25, ciudad="Madrid")
print()

# Función que retorna múltiples valores
print("=== Retornar Múltiples Valores ===")
def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None
    return suma, resta, multiplicacion, division

s, r, m, d = operaciones(10, 5)
print(f"Operaciones con 10 y 5:")
print(f"  Suma: {s}")
print(f"  Resta: {r}")
print(f"  Multiplicación: {m}")
print(f"  División: {d}\n")

# Funciones lambda (anónimas)
print("=== Funciones Lambda ===")
cuadrado = lambda x: x**2
print(f"cuadrado(5) = {cuadrado(5)}")

numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(f"Cuadrados de {numeros}: {cuadrados}\n")

# Función dentro de función
print("=== Función Anidada ===")
def funcion_externa(x):
    def funcion_interna(y):
        return y * 2
    return funcion_interna(x) + 10

resultado = funcion_externa(5)
print(f"función_externa(5) = {resultado}\n")

# Decoradores (concepto básico)
print("=== Decoradores ===")
def decorador_simple(func):
    def wrapper():
        print("Antes de la función")
        func()
        print("Después de la función")
    return wrapper

@decorador_simple
def decir_hola():
    print("¡Hola!")

decir_hola()
print()

# Funciones con documentación (docstrings)
print("=== Funciones con Documentación ===")
def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    
    Parámetros:
    base (float): La base del rectángulo
    altura (float): La altura del rectángulo
    
    Retorna:
    float: El área del rectángulo
    """
    return base * altura

area = calcular_area_rectangulo(5, 3)
print(f"Área del rectángulo (5x3): {area}")
print(f"Documentación: {calcular_area_rectangulo.__doc__}\n")

# Función recursiva
print("=== Función Recursiva ===")
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"factorial(5) = {factorial(5)}")
print(f"factorial(0) = {factorial(0)}\n")

# Función con tipo hints (type hints)
print("=== Type Hints ===")
def multiplicar(a: int, b: int) -> int:
    return a * b

resultado = multiplicar(4, 7)
print(f"multiplicar(4, 7) = {resultado}\n")

# Función generadora (yield)
print("=== Función Generadora ===")
def numeros_pares(limite):
    for i in range(0, limite, 2):
        yield i

print("Primeros 5 números pares:")
for num in numeros_pares(10):
    print(f"  {num}")
print()

# Scope (ámbito) de variables
print("=== Scope de Variables ===")
variable_global = "Soy global"

def funcion_scope():
    variable_local = "Soy local"
    print(f"Dentro de la función: {variable_local}")
    print(f"Variable global: {variable_global}")

funcion_scope()
print(f"Fuera de la función: {variable_global}\n")

# Función como parámetro
print("=== Función como Parámetro ===")
def aplicar_funcion(func, valor):
    return func(valor)

def doble(x):
    return x * 2

def triple(x):
    return x * 3

print(f"aplicar_funcion(doble, 5) = {aplicar_funcion(doble, 5)}")
print(f"aplicar_funcion(triple, 5) = {aplicar_funcion(triple, 5)}")
