# Archivo: 24_pila_cola.py
# Descripción: Implementación de estructuras de datos Pila (Stack) y Cola (Queue)

from collections import deque

print("=== Estructuras de Datos: Pila y Cola ===\n")

# Versión 1: Original
print("=== Versión 1: Original ===")
class Pila:
    def __init__(self):
        self.pila = []

    def crear(self):
        self.pila = []

    def apilar(self, elemento):
        self.pila.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.pila.pop()
        else:
            return None

    def esta_vacia(self):
        return len(self.pila) == 0
    
    def imprimir_resultados(self):
        if not self.esta_vacia():
            print("Elementos de la pila:", self.pila)
        else:
            print("La pila está vacía")

    def modificar_estructura(self, x):
        while not self.esta_vacia() and self.pila[-1] != x:
            self.desapilar()

        if not self.esta_vacia():
            print(f"Encontrado {x}, eliminando elementos previos...")
            while len(self.pila) > 1:
                self.desapilar()
        else:
            print(f"No se encontró {x} en la estructura")

        print(f"Estado final de la pila:")
        self.imprimir_resultados()


class Cola:
    def __init__(self):
        self.cola = []

    def crear(self):
        self.cola = []

    def encolar(self, elemento):
        self.cola.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.cola.pop(0)  # O(n) - ineficiente
        else:
            return None

    def esta_vacia(self):
        return len(self.cola) == 0

    def imprimir_resultados(self):
        if not self.esta_vacia():
            print("Elementos de la cola:", self.cola)
        else:
            print("La cola está vacía")

    def modificar_estructura(self, x):
        while not self.esta_vacia() and self.cola[0] != x:
            self.desencolar()

        if not self.esta_vacia():
            print(f"Encontrado {x}, eliminando elementos previos...")
            while len(self.cola) > 1:
                self.desencolar()
        else:
            print(f"No se encontró {x} en la estructura")

        print(f"Estado final de la cola:")
        self.imprimir_resultados()

print("Versión original definida.\n")

# Versión 2: Optimizada
print("=== Versión 2: Optimizada ===")
class PilaOptimizada:
    """
    Implementación optimizada de una Pila (Stack) usando LIFO (Last In First Out).
    """
    
    def __init__(self):
        """Inicializa una pila vacía."""
        self.pila = []
    
    def apilar(self, elemento):
        """Agrega un elemento a la pila."""
        self.pila.append(elemento)
    
    def desapilar(self):
        """
        Elimina y retorna el último elemento agregado.
        Retorna None si la pila está vacía.
        """
        if not self.esta_vacia():
            return self.pila.pop()
        return None
    
    def ver_tope(self):
        """
        Retorna el elemento en el tope sin eliminarlo.
        Retorna None si la pila está vacía.
        """
        if not self.esta_vacia():
            return self.pila[-1]
        return None
    
    def esta_vacia(self):
        """Verifica si la pila está vacía."""
        return len(self.pila) == 0
    
    def tamanio(self):
        """Retorna el número de elementos en la pila."""
        return len(self.pila)
    
    def vaciar(self):
        """Vacia la pila."""
        self.pila.clear()
    
    def __str__(self):
        """Representación en string de la pila."""
        return f"Pila: {self.pila}"
    
    def __repr__(self):
        """Representación formal de la pila."""
        return f"PilaOptimizada({self.pila})"
    
    def imprimir_resultados(self):
        """Imprime el estado actual de la pila."""
        if not self.esta_vacia():
            print(f"Elementos de la pila (tope -> fondo): {self.pila}")
            print(f"Tamaño: {self.tamanio()}, Tope: {self.ver_tope()}")
        else:
            print("La pila está vacía")
    
    def modificar_estructura(self, x):
        """
        Elimina elementos hasta encontrar x, luego elimina todos excepto x.
        """
        encontrado = False
        
        # Eliminar elementos hasta encontrar x
        while not self.esta_vacia() and self.ver_tope() != x:
            self.desapilar()
        
        if not self.esta_vacia():
            encontrado = True
            print(f"Encontrado {x}, eliminando elementos previos...")
            # Eliminar todos excepto x
            while self.tamanio() > 1:
                self.desapilar()
        else:
            print(f"No se encontró {x} en la estructura")
        
        print("Estado final de la pila:")
        self.imprimir_resultados()
        return encontrado


class ColaOptimizada:
    """
    Implementación optimizada de una Cola (Queue) usando FIFO (First In First Out).
    Usa collections.deque para eficiencia O(1) en ambas operaciones.
    """
    
    def __init__(self):
        """Inicializa una cola vacía usando deque."""
        self.cola = deque()
    
    def encolar(self, elemento):
        """Agrega un elemento al final de la cola."""
        self.cola.append(elemento)
    
    def desencolar(self):
        """
        Elimina y retorna el primer elemento de la cola.
        Retorna None si la cola está vacía.
        """
        if not self.esta_vacia():
            return self.cola.popleft()
        return None
    
    def ver_frente(self):
        """
        Retorna el elemento al frente sin eliminarlo.
        Retorna None si la cola está vacía.
        """
        if not self.esta_vacia():
            return self.cola[0]
        return None
    
    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return len(self.cola) == 0
    
    def tamanio(self):
        """Retorna el número de elementos en la cola."""
        return len(self.cola)
    
    def vaciar(self):
        """Vacia la cola."""
        self.cola.clear()
    
    def __str__(self):
        """Representación en string de la cola."""
        return f"Cola: {list(self.cola)}"
    
    def __repr__(self):
        """Representación formal de la cola."""
        return f"ColaOptimizada({list(self.cola)})"
    
    def imprimir_resultados(self):
        """Imprime el estado actual de la cola."""
        if not self.esta_vacia():
            print(f"Elementos de la cola (frente -> final): {list(self.cola)}")
            print(f"Tamaño: {self.tamanio()}, Frente: {self.ver_frente()}")
        else:
            print("La cola está vacía")
    
    def modificar_estructura(self, x):
        """
        Elimina elementos desde el frente hasta encontrar x, luego elimina todos excepto x.
        """
        encontrado = False
        
        # Eliminar elementos desde el frente hasta encontrar x
        while not self.esta_vacia() and self.ver_frente() != x:
            self.desencolar()
        
        if not self.esta_vacia():
            encontrado = True
            print(f"Encontrado {x}, eliminando elementos previos...")
            # Eliminar todos excepto x
            while self.tamanio() > 1:
                self.desencolar()
        else:
            print(f"No se encontró {x} en la estructura")
        
        print("Estado final de la cola:")
        self.imprimir_resultados()
        return encontrado

print("Versión optimizada definida.\n")

# Versión 3: Con métodos adicionales útiles
print("=== Versión 3: Con Métodos Adicionales ===")
class PilaAvanzada(PilaOptimizada):
    """
    Pila con métodos adicionales útiles.
    """
    
    def buscar(self, elemento):
        """Busca un elemento en la pila. Retorna True si existe."""
        return elemento in self.pila
    
    def contar(self, elemento):
        """Cuenta cuántas veces aparece un elemento en la pila."""
        return self.pila.count(elemento)
    
    def copiar(self):
        """Crea una copia de la pila."""
        nueva_pila = PilaAvanzada()
        nueva_pila.pila = self.pila.copy()
        return nueva_pila
    
    def invertir(self):
        """Invierte el orden de los elementos en la pila."""
        self.pila.reverse()


class ColaAvanzada(ColaOptimizada):
    """
    Cola con métodos adicionales útiles.
    """
    
    def buscar(self, elemento):
        """Busca un elemento en la cola. Retorna True si existe."""
        return elemento in self.cola
    
    def contar(self, elemento):
        """Cuenta cuántas veces aparece un elemento en la cola."""
        return self.cola.count(elemento)
    
    def copiar(self):
        """Crea una copia de la cola."""
        nueva_cola = ColaAvanzada()
        nueva_cola.cola = self.cola.copy()
        return nueva_cola

print("Versiones avanzadas definidas.\n")

# Versión 4: Menú interactivo mejorado
print("=== Versión 4: Menú Interactivo Mejorado ===")
def main_optimizada():
    """
    Función main mejorada con manejo de errores y más opciones.
    """
    pila = PilaOptimizada()
    cola = ColaOptimizada()
    
    while True:
        try:
            print("\n" + "=" * 50)
            print("           MENÚ PRINCIPAL")
            print("=" * 50)
            print("\n--- PILA ---")
            print("1. Apilar un elemento")
            print("2. Desapilar un elemento")
            print("3. Ver tope de la pila")
            print("4. Mostrar estado de la pila")
            print("\n--- COLA ---")
            print("5. Encolar un elemento")
            print("6. Desencolar un elemento")
            print("7. Ver frente de la cola")
            print("8. Mostrar estado de la cola")
            print("\n--- OPERACIONES ESPECIALES ---")
            print("9. Modificar estructura (Pila)")
            print("10. Modificar estructura (Cola)")
            print("\n--- UTILIDADES ---")
            print("11. Vaciar pila")
            print("12. Vaciar cola")
            print("13. Salir")
            print("=" * 50)
            
            opcion = input("\nSeleccione una opción: ").strip()
            
            if opcion == "1":
                elemento = input("Ingrese un elemento para apilar: ")
                pila.apilar(elemento)
                print(f"✅ Elemento '{elemento}' apilado correctamente")
                pila.imprimir_resultados()
            
            elif opcion == "2":
                elemento = pila.desapilar()
                if elemento is not None:
                    print(f"✅ Elemento '{elemento}' desapilado correctamente")
                else:
                    print("⚠️  La pila está vacía")
                pila.imprimir_resultados()
            
            elif opcion == "3":
                tope = pila.ver_tope()
                if tope is not None:
                    print(f"🔝 Tope de la pila: {tope}")
                else:
                    print("⚠️  La pila está vacía")
            
            elif opcion == "4":
                pila.imprimir_resultados()
            
            elif opcion == "5":
                elemento = input("Ingrese un elemento para encolar: ")
                cola.encolar(elemento)
                print(f"✅ Elemento '{elemento}' encolado correctamente")
                cola.imprimir_resultados()
            
            elif opcion == "6":
                elemento = cola.desencolar()
                if elemento is not None:
                    print(f"✅ Elemento '{elemento}' desencolado correctamente")
                else:
                    print("⚠️  La cola está vacía")
                cola.imprimir_resultados()
            
            elif opcion == "7":
                frente = cola.ver_frente()
                if frente is not None:
                    print(f"🔝 Frente de la cola: {frente}")
                else:
                    print("⚠️  La cola está vacía")
            
            elif opcion == "8":
                cola.imprimir_resultados()
            
            elif opcion == "9":
                x = input("Ingrese el valor X a buscar en la pila: ")
                pila.modificar_estructura(x)
            
            elif opcion == "10":
                x = input("Ingrese el valor X a buscar en la cola: ")
                cola.modificar_estructura(x)
            
            elif opcion == "11":
                pila.vaciar()
                print("✅ Pila vaciada")
            
            elif opcion == "12":
                cola.vaciar()
                print("✅ Cola vaciada")
            
            elif opcion == "13":
                print("\n👋 ¡Hasta luego!")
                break
            
            else:
                print("❌ Opción no válida. Por favor seleccione una opción del 1 al 13.")
        
        except ValueError as e:
            print(f"❌ Error de valor: {e}")
        except KeyboardInterrupt:
            print("\n\n⚠️  Operación cancelada por el usuario")
            respuesta = input("¿Desea salir? (s/n): ").lower()
            if respuesta == 's':
                break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

# Descomentar para probar:
# main_optimizada()

# Ejemplos de uso
print("=== Ejemplos de Uso ===")
print("\nEjemplo 1: Uso básico de Pila")
pila_ejemplo = PilaOptimizada()
pila_ejemplo.apilar("A")
pila_ejemplo.apilar("B")
pila_ejemplo.apilar("C")
print(f"Estado: {pila_ejemplo}")
print(f"Tope: {pila_ejemplo.ver_tope()}")
elemento = pila_ejemplo.desapilar()
print(f"Desapilado: {elemento}")
print(f"Estado final: {pila_ejemplo}")

print("\nEjemplo 2: Uso básico de Cola")
cola_ejemplo = ColaOptimizada()
cola_ejemplo.encolar("X")
cola_ejemplo.encolar("Y")
cola_ejemplo.encolar("Z")
print(f"Estado: {cola_ejemplo}")
print(f"Frente: {cola_ejemplo.ver_frente()}")
elemento = cola_ejemplo.desencolar()
print(f"Desencolado: {elemento}")
print(f"Estado final: {cola_ejemplo}")

print("\nEjemplo 3: Comparación de eficiencia")
import time

# Cola con list (O(n))
def test_cola_list(n):
    cola = []
    inicio = time.time()
    for i in range(n):
        cola.append(i)
    for i in range(n):
        cola.pop(0)
    return time.time() - inicio

# Cola con deque (O(1))
def test_cola_deque(n):
    cola = deque()
    inicio = time.time()
    for i in range(n):
        cola.append(i)
    for i in range(n):
        cola.popleft()
    return time.time() - inicio

n = 10000
tiempo_list = test_cola_list(n)
tiempo_deque = test_cola_deque(n)
print(f"Tiempo con list.pop(0) para {n} elementos: {tiempo_list:.4f}s")
print(f"Tiempo con deque.popleft() para {n} elementos: {tiempo_deque:.4f}s")
print(f"Mejora: {tiempo_list/tiempo_deque:.1f}x más rápido con deque")

print()

# Resumen y mejoras
print("=== Resumen de Análisis ===")
print("Problemas en el código original:")
print("1. ❌ Cola usa pop(0) que es O(n) - ineficiente")
print("2. ⚠️  Método crear() es redundante (ya se hace en __init__)")
print("3. ⚠️  Falta validación de errores en main")
print("4. ⚠️  No hay métodos para ver tope/frente sin eliminar")
print("5. ⚠️  Falta documentación")
print("6. ⚠️  No hay métodos de utilidad (vaciar, tamaño, etc.)")
print()
print("Mejoras implementadas:")
print("1. ✅ Cola usa deque para O(1) en ambas operaciones")
print("2. ✅ Eliminado método redundante crear()")
print("3. ✅ Manejo de errores completo")
print("4. ✅ Métodos ver_tope() y ver_frente()")
print("5. ✅ Documentación completa")
print("6. ✅ Métodos adicionales (tamaño, vaciar, etc.)")
print("7. ✅ Representación con __str__ y __repr__")
print("8. ✅ Menú interactivo mejorado")
print("9. ✅ Versiones avanzadas con más funcionalidades")

# Función main original (para referencia)
def main_original():
    """
    Función main original (para referencia).
    """
    pila = Pila()
    cola = Cola()

    while True:
        print("-" * 20)
        print("1. Apilar un elemento")
        print("2. Desapilar un elemento")
        print("3. Encolar un elemento")
        print("4. Desencolar un elemento")
        print("5. Modificar estructura")
        print("6. Salir")
        print("-" * 20)

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                elemento = input("Ingrese un elemento: ")
                pila.apilar(elemento)
                print(f"Elemento {elemento} apilado correctamente")
                pila.imprimir_resultados()

            elif opcion == 2:
                elemento = pila.desapilar()
                if elemento is not None:
                    print(f"Elemento {elemento} desapilado correctamente")
                else:
                    print("La pila está vacía")
                pila.imprimir_resultados()

            elif opcion == 3:
                elemento = input("Ingrese un elemento: ")
                cola.encolar(elemento)
                print(f"Elemento {elemento} encolado correctamente")
                cola.imprimir_resultados()

            elif opcion == 4:
                elemento = cola.desencolar()
                if elemento is not None:
                    print(f"Elemento {elemento} desencolado correctamente")
                else:
                    print("La cola está vacía")
                cola.imprimir_resultados()

            elif opcion == 5:
                estructura = input("Seleccione la estructura (Pila/Cola): ")
                x = input("Ingrese el valor X a buscar: ")
                if estructura.lower() == "pila":
                    pila.modificar_estructura(x)
                elif estructura.lower() == "cola":
                    cola.modificar_estructura(x)
                else:
                    print("Estructura no válida")

            elif opcion == 6:
                break

            else:
                print("Opción no válida")
        
        except ValueError:
            print("Por favor ingrese un número válido")
        except KeyboardInterrupt:
            print("\nSaliendo...")
            break

if __name__ == "__main__":
    # Descomentar para ejecutar:
    # main_optimizada()  # Versión mejorada
    # main_original()    # Versión original
    print("\nNota: Descomenta main_optimizada() o main_original() para ejecutar")
