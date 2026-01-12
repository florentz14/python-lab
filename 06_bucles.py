# Archivo: 06_bucles.py
# Descripción: Bucles (for y while)

print("=== Bucles en Python ===\n")

# Bucle for con range()
print("=== Bucle for con range() ===")
print("Contando del 1 al 5:")
for i in range(1, 6):
    print(f"Número: {i}")

print("\n=== Bucle for con lista ===")
frutas = ["manzana", "banana", "naranja", "uva"]
print("Lista de frutas:")
for fruta in frutas:
    print(f"- {fruta}")

print("\n=== Bucle for con índice ===")
for indice, fruta in enumerate(frutas):
    print(f"{indice + 1}. {fruta}")

# Bucle while
print("\n=== Bucle while ===")
contador = 0
print("Contador del 0 al 4:")
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

# Bucle while con condición
print("\n=== Bucle while con entrada ===")
numero = 0
while numero != 5:
    numero = int(input("Adivina el número (1-10), o escribe 5 para salir: "))
    if numero == 5:
        print("¡Correcto! Saliendo del bucle...")
    elif numero < 5:
        print("El número es mayor")
    else:
        print("El número es menor")

# break y continue
print("\n=== break y continue ===")
print("Números del 1 al 10, saltando el 5:")
for i in range(1, 11):
    if i == 5:
        continue  # Salta esta iteración
    print(i)
    if i == 8:
        break  # Sale del bucle

# Bucle anidado
print("\n=== Bucle Anidado (Tabla de Multiplicar) ===")
print("Tabla del 2:")
for i in range(1, 6):
    resultado = 2 * i
    print(f"2 x {i} = {resultado}")
