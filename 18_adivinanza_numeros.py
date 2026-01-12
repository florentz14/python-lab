# Archivo: 18_adivinanza_numeros.py
# Descripción: Juego de adivinanza de números con límite de intentos

from random import randint

print("=== Juego de Adivinanza de Números ===\n")

# Versión 1: Original (con correcciones de lógica)
print("=== Versión 1: Original (Corregida) ===")
def adivinanza_original():
    """
    Versión basada en el código original con correcciones de lógica.
    """
    numero = randint(1, 10)  # Corregido: 1 al 10 en lugar de 0 al 10
    intentos = 0
    
    while True:
        try:
            adivina = int(input('Escribe un número, solo tienes 3 intentos: '))
            intentos = intentos + 1
            
            if adivina == numero:
                print('Felicitaciones, adivinaste')
                break
            
            if intentos == 3:
                print(f'Fallaste. El número era {numero}')
                break
        except ValueError:
            print('Por favor ingresa un número válido')
            continue

# Descomentar para probar:
# adivinanza_original()

# Versión 2: Optimizada (estructura mejorada)
print("=== Versión 2: Optimizada ===")
def adivinanza_optimizada():
    """
    Versión optimizada con mejor estructura y manejo de errores.
    """
    numero = randint(1, 10)
    max_intentos = 3
    intentos = 0
    
    print(f'Tienes {max_intentos} intentos para adivinar un número del 1 al 10. ¡Suerte!')
    
    while intentos < max_intentos:
        try:
            adivina = int(input(f'Intento {intentos + 1}/{max_intentos}. Adivina el número: '))
            
            if adivina == numero:
                print(f'¡Felicitaciones! Adivinaste el número {numero} en {intentos + 1} intento(s)')
                return True
            
            intentos += 1
            if intentos < max_intentos:
                if adivina < numero:
                    print(f'El número es mayor. Te quedan {max_intentos - intentos} intentos.')
                else:
                    print(f'El número es menor. Te quedan {max_intentos - intentos} intentos.')
        
        except ValueError:
            print('Error: Por favor ingresa un número válido.')
    
    print(f'Fallaste. El número era {numero}.')
    return False

# Descomentar para probar:
# adivinanza_optimizada()

# Versión 3: Con pistas (mayor/menor)
print("=== Versión 3: Con Pistas (Mayor/Menor) ===")
def adivinanza_con_pistas():
    """
    Versión que da pistas si el número es mayor o menor.
    """
    numero = randint(1, 10)
    max_intentos = 3
    intentos = 0
    
    print('Tienes 3 intentos para adivinar un número del 1 al 10. ¡Suerte!')
    
    while intentos < max_intentos:
        try:
            adivina = int(input(f'Intento {intentos + 1}/{max_intentos}: '))
            
            if adivina == numero:
                print(f'¡Felicitaciones! El número era {numero}')
                return True
            
            intentos += 1
            
            if intentos < max_intentos:
                if adivina < numero:
                    print('El número es mayor')
                else:
                    print('El número es menor')
        
        except ValueError:
            print('Por favor ingresa un número válido')
    
    print(f'Fallaste. El número era {numero}')
    return False

# Versión 4: Configurable (rango y intentos)
print("=== Versión 4: Configurable ===")
def adivinanza_configurable(rango_min=1, rango_max=10, max_intentos=3):
    """
    Versión configurable con rango y número de intentos personalizables.
    """
    numero = randint(rango_min, rango_max)
    intentos = 0
    
    print(f'Tienes {max_intentos} intentos para adivinar un número del {rango_min} al {rango_max}')
    
    while intentos < max_intentos:
        try:
            adivina = int(input(f'Intento {intentos + 1}/{max_intentos}: '))
            
            if adivina < rango_min or adivina > rango_max:
                print(f'El número debe estar entre {rango_min} y {rango_max}')
                continue
            
            if adivina == numero:
                print(f'¡Felicitaciones! Adivinaste en {intentos + 1} intento(s)')
                return True
            
            intentos += 1
            if intentos < max_intentos:
                pista = "mayor" if adivina < numero else "menor"
                print(f'El número es {pista}. Intentos restantes: {max_intentos - intentos}')
        
        except ValueError:
            print('Por favor ingresa un número válido')
    
    print(f'Fallaste. El número era {numero}')
    return False

# Ejemplo de uso configurable (comentado):
# adivinanza_configurable(1, 100, 5)

# Versión 5: Con estadísticas
print("=== Versión 5: Con Estadísticas ===")
def adivinanza_con_estadisticas():
    """
    Versión que lleva registro de partidas y muestra estadísticas.
    """
    numero = randint(1, 10)
    max_intentos = 3
    intentos = 0
    partidas = 0
    victorias = 0
    
    while True:
        partidas += 1
        numero = randint(1, 10)
        intentos = 0
        acertado = False
        
        print(f'\n--- Partida {partidas} ---')
        print(f'Tienes {max_intentos} intentos para adivinar un número del 1 al 10')
        
        while intentos < max_intentos:
            try:
                adivina = int(input(f'Intento {intentos + 1}/{max_intentos}: '))
                
                if adivina == numero:
                    print(f'¡Felicitaciones! Adivinaste en {intentos + 1} intento(s)')
                    victorias += 1
                    acertado = True
                    break
                
                intentos += 1
                if intentos < max_intentos:
                    pista = "mayor" if adivina < numero else "menor"
                    print(f'El número es {pista}')
            
            except ValueError:
                print('Por favor ingresa un número válido')
        
        if not acertado:
            print(f'Fallaste. El número era {numero}')
        
        # Estadísticas
        print(f'\nEstadísticas: {victorias}/{partidas} victorias ({victorias/partidas*100:.1f}%)')
        
        # Preguntar si quiere seguir jugando
        continuar = input('\n¿Quieres jugar de nuevo? (s/n): ').lower()
        if continuar != 's':
            break
    
    print(f'\n¡Gracias por jugar!')
    print(f'Estadísticas finales: {victorias} victorias de {partidas} partidas')

# Descomentar para probar:
# adivinanza_con_estadisticas()

# Versión 6: Sin bucle infinito (con límite de partidas)
print("=== Versión 6: Versión Simple Mejorada ===")
def adivinanza_simple():
    """
    Versión simple y clara sin bucle infinito.
    """
    numero = randint(1, 10)
    max_intentos = 3
    
    print('Tienes 3 intentos para adivinar un número del 1 al 10. ¡Suerte!')
    
    for intento in range(1, max_intentos + 1):
        try:
            adivina = int(input(f'Intento {intento}/{max_intentos}: '))
            
            if adivina == numero:
                print(f'¡Felicitaciones! Adivinaste el número {numero}')
                return True
            
            if intento < max_intentos:
                if adivina < numero:
                    print('El número es mayor')
                else:
                    print('El número es menor')
        
        except ValueError:
            print('Por favor ingresa un número válido')
    
    print(f'Fallaste. El número era {numero}')
    return False

# Versión 7: Con modo fácil/difícil
print("=== Versión 7: Con Dificultades ===")
def adivinanza_con_dificultad():
    """
    Versión con diferentes niveles de dificultad.
    """
    print('Selecciona la dificultad:')
    print('1. Fácil (1-10, 5 intentos)')
    print('2. Medio (1-50, 4 intentos)')
    print('3. Difícil (1-100, 3 intentos)')
    
    try:
        opcion = int(input('Opción: '))
        
        if opcion == 1:
            rango_min, rango_max, intentos = 1, 10, 5
        elif opcion == 2:
            rango_min, rango_max, intentos = 1, 50, 4
        elif opcion == 3:
            rango_min, rango_max, intentos = 1, 100, 3
        else:
            print('Opción inválida. Usando modo fácil.')
            rango_min, rango_max, intentos = 1, 10, 5
        
        return adivinanza_configurable(rango_min, rango_max, intentos)
    except ValueError:
        print('Opción inválida')
        return False

# Ejemplos y pruebas
print("=== Problemas Identificados en el Código Original ===")
print("1. randint(0, 10) genera números del 0 al 10, pero el comentario dice 1 al 10")
print("2. La lógica del contador: se incrementa antes de verificar, causando problemas")
print("3. Si adivina en el último intento, el contador llega a 3 y dice 'Fallaste' antes de verificar")
print("4. Falta manejo de errores (ValueError cuando no es número)")
print("5. Imports innecesarios (uniform, random no se usan)")
print("6. Falta mostrar el número si falla")
print("7. Typo: 'Felecidades' debería ser 'Felicitaciones'")
print()

print("=== Mejoras Implementadas ===")
print("1. Corregido rango: randint(1, 10) en lugar de (0, 10)")
print("2. Lógica corregida: verificar antes de incrementar contador")
print("3. Manejo de errores con try/except")
print("4. Eliminación de imports innecesarios")
print("5. Mostrar el número correcto si falla")
print("6. Pistas (mayor/menor) para ayudar al jugador")
print("7. Versiones configurable y con estadísticas")
print("8. Mejor estructura y claridad del código")
print()

# Versión de demostración (no interactiva)
print("=== Demostración (Simulación) ===")
def simular_juego():
    """
    Simula el juego para demostración.
    """
    numero = randint(1, 10)
    max_intentos = 3
    intentos_realizados = []
    
    # Simular intentos
    for intento in range(1, max_intentos + 1):
        # En una simulación real, usarías input()
        # Aquí simulamos con números conocidos
        if intento == 1:
            adivina = 5  # Simulación
        elif intento == 2:
            adivina = 7  # Simulación
        else:
            adivina = numero  # Simulación: adivina correctamente
        
        intentos_realizados.append(adivina)
        
        if adivina == numero:
            print(f"Intento {intento}: {adivina} -> ¡Adivinaste! El número era {numero}")
            return True
        else:
            pista = "mayor" if adivina < numero else "menor"
            print(f"Intento {intento}: {adivina} -> El número es {pista}")
    
    print(f"Fallaste. El número era {numero}")
    return False

# Ejecutar una simulación de ejemplo
numero_ejemplo = randint(1, 10)
print(f"\nEjemplo: Número a adivinar = {numero_ejemplo}")
print("(En el juego real, este número estaría oculto)")
