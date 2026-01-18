# Archivo: 52_ecuaciones_diferenciales.py
# Descripción: Resolución de Ecuaciones Diferenciales

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, odeint

print("=== Ecuaciones Diferenciales ===\n")

# =============================================================================
# 1. ECUACIÓN DIFERENCIAL DE PRIMER ORDEN - MÉTODO DE EULER
# =============================================================================
print("=== 1. Método de Euler ===")

def metodo_euler(f, y0, t0, tf, n_pasos):
    """
    Resuelve una ecuación diferencial dy/dt = f(t, y) usando el método de Euler.
    
    Parámetros:
    - f: función f(t, y) que define la derivada
    - y0: condición inicial y(t0)
    - t0: tiempo inicial
    - tf: tiempo final
    - n_pasos: número de pasos
    
    Retorna: (t_array, y_array)
    """
    h = (tf - t0) / n_pasos  # Tamaño del paso
    t = np.linspace(t0, tf, n_pasos + 1)
    y = np.zeros(n_pasos + 1)
    y[0] = y0
    
    for i in range(n_pasos):
        y[i + 1] = y[i] + h * f(t[i], y[i])
    
    return t, y

# Ejemplo 1: dy/dt = -2y, y(0) = 1
print("\nEjemplo 1: dy/dt = -2y, y(0) = 1")
print("Solución analítica: y(t) = e^(-2t)")

def ejemplo1_derivada(t, y):
    return -2 * y

t_euler, y_euler = metodo_euler(ejemplo1_derivada, y0=1, t0=0, tf=2, n_pasos=50)
y_exacta = np.exp(-2 * t_euler)

print(f"Valor en t=2 (Euler): {y_euler[-1]:.6f}")
print(f"Valor en t=2 (Exacta): {y_exacta[-1]:.6f}")
print(f"Error: {abs(y_euler[-1] - y_exacta[-1]):.6f}")

# Visualización
plt.figure(figsize=(10, 6))
plt.plot(t_euler, y_euler, 'b-', label='Método de Euler', linewidth=2)
plt.plot(t_euler, y_exacta, 'r--', label='Solución Exacta', linewidth=2)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Método de Euler: dy/dt = -2y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# =============================================================================
# 2. MÉTODO DE RUNGE-KUTTA (ORDEN 4)
# =============================================================================
print("\n=== 2. Método de Runge-Kutta (Orden 4) ===")

def runge_kutta_4(f, y0, t0, tf, n_pasos):
    """
    Resuelve una ecuación diferencial usando el método de Runge-Kutta de orden 4.
    Más preciso que el método de Euler.
    """
    h = (tf - t0) / n_pasos
    t = np.linspace(t0, tf, n_pasos + 1)
    y = np.zeros(n_pasos + 1)
    y[0] = y0
    
    for i in range(n_pasos):
        k1 = h * f(t[i], y[i])
        k2 = h * f(t[i] + h/2, y[i] + k1/2)
        k3 = h * f(t[i] + h/2, y[i] + k2/2)
        k4 = h * f(t[i] + h, y[i] + k3)
        
        y[i + 1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
    
    return t, y

# Comparación Euler vs Runge-Kutta
print("\nComparación Euler vs Runge-Kutta:")
t_rk, y_rk = runge_kutta_4(ejemplo1_derivada, y0=1, t0=0, tf=2, n_pasos=50)

print(f"Euler - Error en t=2: {abs(y_euler[-1] - y_exacta[-1]):.6f}")
print(f"RK4   - Error en t=2: {abs(y_rk[-1] - y_exacta[-1]):.6f}")

plt.figure(figsize=(10, 6))
plt.plot(t_euler, y_euler, 'b-', label='Método de Euler', linewidth=2, alpha=0.7)
plt.plot(t_rk, y_rk, 'g-', label='Runge-Kutta 4', linewidth=2, alpha=0.7)
plt.plot(t_euler, y_exacta, 'r--', label='Solución Exacta', linewidth=2)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Comparación de Métodos: dy/dt = -2y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# =============================================================================
# 3. USANDO SCIPY.SOLVE_IVP (Método más avanzado)
# =============================================================================
print("\n=== 3. Usando scipy.integrate.solve_ivp ===")

def ejemplo2_derivada(t, y):
    """dy/dt = t * y, y(0) = 1"""
    return t * y

# Resolver con scipy
solucion = solve_ivp(ejemplo2_derivada, [0, 2], [1], 
                     t_eval=np.linspace(0, 2, 100),
                     method='RK45')

print(f"Valor en t=2: {solucion.y[0][-1]:.6f}")
print(f"Solución exacta: {np.exp(2**2/2):.6f}")

plt.figure(figsize=(10, 6))
plt.plot(solucion.t, solucion.y[0], 'b-', label='Solución Numérica', linewidth=2)
plt.plot(solucion.t, np.exp(solucion.t**2 / 2), 'r--', 
         label='Solución Exacta: y = e^(t²/2)', linewidth=2)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Solución usando scipy.solve_ivp: dy/dt = t*y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# =============================================================================
# 4. MODELO DE CRECIMIENTO POBLACIONAL (Modelo de Malthus)
# =============================================================================
print("\n=== 4. Modelo de Crecimiento Poblacional ===")
print("dy/dt = r * y, donde r es la tasa de crecimiento")

def crecimiento_poblacional(t, y, r=0.1):
    """Modelo de Malthus: crecimiento exponencial"""
    return r * y

r_tasa = 0.1  # Tasa de crecimiento (10% por unidad de tiempo)
poblacion_inicial = 1000

sol_poblacion = solve_ivp(
    lambda t, y: crecimiento_poblacional(t, y, r_tasa),
    [0, 50],
    [poblacion_inicial],
    t_eval=np.linspace(0, 50, 100)
)

print(f"Población inicial: {poblacion_inicial}")
print(f"Población en t=50: {sol_poblacion.y[0][-1]:.2f}")

plt.figure(figsize=(10, 6))
plt.plot(sol_poblacion.t, sol_poblacion.y[0], 'g-', linewidth=2)
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.title('Modelo de Crecimiento Exponencial (Malthus)')
plt.grid(True, alpha=0.3)
plt.show()

# =============================================================================
# 5. MODELO LOGÍSTICO (Crecimiento limitado)
# =============================================================================
print("\n=== 5. Modelo Logístico ===")
print("dy/dt = r * y * (1 - y/K), donde K es la capacidad de carga")

def modelo_logistico(t, y, r=0.1, K=5000):
    """Modelo logístico con capacidad de carga"""
    return r * y * (1 - y / K)

sol_logistica = solve_ivp(
    lambda t, y: modelo_logistico(t, y, r=0.15, K=5000),
    [0, 100],
    [100],
    t_eval=np.linspace(0, 100, 200)
)

print(f"Capacidad de carga (K): 5000")
print(f"Población inicial: 100")
print(f"Población final: {sol_logistica.y[0][-1]:.2f}")

plt.figure(figsize=(10, 6))
plt.plot(sol_logistica.t, sol_logistica.y[0], 'b-', linewidth=2, label='Población')
plt.axhline(y=5000, color='r', linestyle='--', label='Capacidad de Carga (K)')
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.title('Modelo Logístico de Crecimiento Poblacional')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# =============================================================================
# 6. SISTEMA DE ECUACIONES DIFERENCIALES
# =============================================================================
print("\n=== 6. Sistema de Ecuaciones Diferenciales ===")
print("Modelo Predador-Presa (Lotka-Volterra)")

def sistema_predador_presa(t, y, a=1.0, b=0.1, c=1.5, d=0.075):
    """
    Sistema de ecuaciones diferenciales:
    dx/dt = a*x - b*x*y  (presa)
    dy/dt = -c*y + d*x*y (predador)
    """
    x, y_pred = y
    dxdt = a * x - b * x * y_pred
    dydt = -c * y_pred + d * x * y_pred
    return [dxdt, dydt]

# Condiciones iniciales: 10 presas, 5 predadores
condiciones_iniciales = [10, 5]
t_sistema = np.linspace(0, 50, 1000)

sol_sistema = solve_ivp(
    lambda t, y: sistema_predador_presa(t, y),
    [0, 50],
    condiciones_iniciales,
    t_eval=t_sistema
)

print(f"Condiciones iniciales: {condiciones_iniciales[0]} presas, {condiciones_iniciales[1]} predadores")

# Gráfico temporal
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(sol_sistema.t, sol_sistema.y[0], 'g-', label='Presas', linewidth=2)
plt.plot(sol_sistema.t, sol_sistema.y[1], 'r-', label='Predadores', linewidth=2)
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.title('Modelo Predador-Presa (Temporal)')
plt.legend()
plt.grid(True, alpha=0.3)

# Plano de fase
plt.subplot(1, 2, 2)
plt.plot(sol_sistema.y[0], sol_sistema.y[1], 'b-', linewidth=1.5)
plt.plot(sol_sistema.y[0][0], sol_sistema.y[1][0], 'go', markersize=10, label='Inicio')
plt.xlabel('Presas')
plt.ylabel('Predadores')
plt.title('Plano de Fase')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# =============================================================================
# 7. ECUACIÓN DIFERENCIAL DE SEGUNDO ORDEN
# =============================================================================
print("\n=== 7. Ecuación Diferencial de Segundo Orden ===")
print("Oscilador Armónico: d²y/dt² + ω²y = 0")

def oscilador_armonico(t, y, omega=1.0):
    """
    Convierte la EDO de segundo orden en un sistema de primer orden:
    y1 = y, y2 = dy/dt
    dy1/dt = y2
    dy2/dt = -ω² * y1
    """
    y1, y2 = y
    return [y2, -omega**2 * y1]

omega = 2.0  # Frecuencia angular
sol_oscilador = solve_ivp(
    lambda t, y: oscilador_armonico(t, y, omega),
    [0, 10],
    [1, 0],  # y(0)=1, y'(0)=0
    t_eval=np.linspace(0, 10, 200)
)

# Solución exacta: y(t) = cos(ωt)
y_exacta_oscilador = np.cos(omega * sol_oscilador.t)

print(f"Frecuencia angular (ω): {omega}")
print(f"Valor en t=10 (numérico): {sol_oscilador.y[0][-1]:.6f}")
print(f"Valor en t=10 (exacto): {y_exacta_oscilador[-1]:.6f}")

plt.figure(figsize=(10, 6))
plt.plot(sol_oscilador.t, sol_oscilador.y[0], 'b-', label='Solución Numérica', linewidth=2)
plt.plot(sol_oscilador.t, y_exacta_oscilador, 'r--', label='Solución Exacta: cos(ωt)', linewidth=2)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Oscilador Armónico: d²y/dt² + ω²y = 0')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# =============================================================================
# RESUMEN DE MÉTODOS
# =============================================================================
print("\n=== Resumen de Métodos ===")
print("""
1. Método de Euler: Simple pero menos preciso
2. Runge-Kutta 4: Más preciso que Euler
3. scipy.solve_ivp: Método avanzado con adaptación de paso
4. Modelos aplicados:
   - Crecimiento exponencial
   - Modelo logístico
   - Sistema predador-presa
   - Oscilador armónico

Todos los métodos resuelven ecuaciones de la forma dy/dt = f(t,  y)
Para ecuaciones de orden superior, se convierten en sistemas de primer orden.
""")
