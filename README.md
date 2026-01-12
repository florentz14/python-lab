# Python Lab - Colección Completa de Algoritmos y Estructuras de Datos

Una colección exhaustiva de algoritmos, estructuras de datos y ejemplos prácticos implementados en Python 3.14.2. Este proyecto cubre desde conceptos básicos hasta algoritmos avanzados, incluyendo matemáticas, grafos, programación dinámica, y más.

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Categorías de Algoritmos](#-categorías-de-algoritmos)
- [Requisitos](#-requisitos)
- [Contribuciones](#-contribuciones)
- [Licencia](#-licencia)

## ✨ Características

- **52 archivos Python** con implementaciones completas
- **100+ algoritmos** diferentes
- Código documentado y optimizado
- Ejemplos prácticos y casos de uso
- Comparaciones de eficiencia entre métodos
- Compatible con Python 3.14.2+

## 📁 Estructura del Proyecto

### Fundamentos de Python (01-12)

| Archivo | Descripción |
|---------|-------------|
| `01_variables.py` | Variables y tipos básicos |
| `02_operaciones_basicas.py` | Operaciones aritméticas |
| `03_entrada_salida.py` | Input/Output en Python |
| `04_tipos_datos.py` | Tipos de datos (int, float, str, bool, etc.) |
| `05_condicionales.py` | Estructuras condicionales (if, elif, else) |
| `06_bucles.py` | Bucles (for, while) |
| `07_diccionarios.py` | Diccionarios y operaciones |
| `08_conjuntos.py` | Conjuntos (sets) y operaciones |
| `09_matrices.py` | Operaciones con matrices (NumPy) |
| `10_numeros_imaginarios.py` | Números complejos |
| `11_listas_avanzadas.py` | List comprehensions, map, filter, reduce |
| `12_funciones.py` | Funciones, decoradores, generadores |

### Algoritmos Básicos Optimizados (13-20)

| Archivo | Descripción |
|---------|-------------|
| `13_encontrar_numero_mayor.py` | Encontrar el mayor entre n números |
| `14_raiz_cuadrada.py` | Múltiples métodos (iterativo, binario, math.sqrt) |
| `15_separar_numeros_textos.py` | Separar números y texto de listas |
| `16_palindromos.py` | Detección de palíndromos (múltiples métodos) |
| `17_suma_recursiva.py` | Suma recursiva (Gauss, iterativo) |
| `18_adivinanza_numeros.py` | Juego de adivinanza con intentos |
| `19_anio_bisiesto.py` | Cálculo de años bisiestos (Gregoriano) |
| `20_contar_caracteres.py` | Análisis completo de strings |

### Algoritmos Avanzados (21-35)

| Archivo | Descripción |
|---------|-------------|
| `21_planificacion_procesos.py` | Algoritmo FCFS (First Come First Served) |
| `22_planificacion_procesos_interactivo.py` | FCFS interactivo |
| `23_visualizacion_datos.py` | Visualización con matplotlib y seaborn |
| `24_pila_cola.py` | Estructuras Stack y Queue |
| `25_sistemas_ecuaciones_lineales.py` | Resolución de sistemas lineales |
| `26_conjetura_goldbach.py` | Conjetura de Goldbach |
| `27_ecuaciones_cuadraticas.py` | Ecuaciones cuadráticas (real y compleja) |
| `28_estadistica_basica.py` | Estadística descriptiva completa |
| `29_factorial.py` | Cálculo de factorial (múltiples métodos) |
| `30_fibonacci.py` | Secuencia de Fibonacci (recursivo, iterativo, Binet) |
| `31_integracion_numerica.py` | Integración numérica (Riemann, Simpson, scipy) |
| `32_potenciacion.py` | Exponentiación (rápida, modular) |
| `33_sistema_ecuaciones_ejemplo.py` | Ejemplo específico de sistemas |
| `34_rango_matriz.py` | Rango de matrices (SVD, QR) |
| `35_suma_riemann.py` | Sumas de Riemann (izquierda, derecha, medio) |

### Algoritmos Clásicos (36-46)

| Archivo | Descripción |
|---------|-------------|
| `36_metodos_ordenamiento.py` | 7 métodos de ordenamiento (Bubble, Quick, Merge, etc.) |
| `37_arboles.py` | Estructuras de árboles (BST, AVL, recorridos) |
| `38_grafos.py` | Grafos (BFS, DFS, representaciones) |
| `39_algoritmos_busqueda.py` | Búsqueda lineal, binaria, KMP |
| `40_tablas_hash.py` | Hash tables (chaining, open addressing) |
| `41_programacion_dinamica.py` | DP (Mochila, LCS, Coin Change, etc.) |
| `42_algoritmos_greedy.py` | Algoritmos voraces (Kruskal, Huffman, etc.) |
| `43_grafos_avanzados.py` | Grafos avanzados (Floyd-Warshall, Topological Sort) |
| `44_algoritmos_strings.py` | Strings (Rabin-Karp, Z-algorithm, Edit Distance) |
| `45_algoritmos_matematicos.py` | Matemáticas (Pascal, Euclides, Criba de Eratóstenes) |
| `46_torres_hanoi.py` | Torres de Hanoi (recursivo e iterativo) |

### Algoritmos Avanzados y Aplicaciones (47-51)

| Archivo | Descripción |
|---------|-------------|
| `47_backtracking.py` | Backtracking (N-Reinas, Sudoku, Laberintos) |
| `48_estructuras_avanzadas.py` | Trie, Segment Tree, Fenwick Tree, Union-Find |
| `49_metodos_numericos.py` | Métodos numéricos (Newton-Raphson, Interpolación, Regresión) |
| `50_geometria_computacional.py` | Geometría (Convex Hull, intersecciones, áreas) |
| `51_openai_chatbot.py` | Chatbot con OpenAI API (moderna) |

## 🚀 Instalación

### Prerrequisitos

- Python 3.14.2 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el repositorio**

```bash
git clone <url-del-repositorio>
cd python-lab
```

2. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

3. **Configurar variables de entorno (opcional, solo para OpenAI)**

Si deseas usar el chatbot de OpenAI (`51_openai_chatbot.py`):

```bash
# Ejecutar script de configuración
python configurar_env.py

# O crear manualmente el archivo .env
# Copia env_template.txt a .env y agrega tu API key
```

## 💻 Uso

### Ejecutar un archivo individual

```bash
python 36_metodos_ordenamiento.py
python 47_backtracking.py
python 51_openai_chatbot.py
```

### Ejemplo rápido

```python
# Ejecutar algoritmo de ordenamiento
python 36_metodos_ordenamiento.py

# Ejecutar N-Reinas con backtracking
python 47_backtracking.py

# Ejecutar chatbot OpenAI
python 51_openai_chatbot.py
# Luego descomenta main() o la función específica en el código
```

## 📚 Categorías de Algoritmos

### 🔍 Búsqueda
- Búsqueda lineal
- Búsqueda binaria
- KMP (Knuth-Morris-Pratt)
- Rabin-Karp
- Z-Algorithm

### 📊 Ordenamiento
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort
- Counting Sort

### 🌳 Estructuras de Datos
- **Básicas**: Listas, Tuplas, Diccionarios, Conjuntos
- **Lineales**: Stack (Pila), Queue (Cola), Deque
- **Avanzadas**: Trie, Segment Tree, Fenwick Tree
- **Árboles**: BST, AVL, Recorridos (BFS, DFS)
- **Grafos**: Lista de adyacencia, Matriz de adyacencia
- **Hash**: Hash Tables (Chaining, Open Addressing)

### 🧮 Algoritmos de Grafos
- BFS (Breadth-First Search)
- DFS (Depth-First Search)
- Dijkstra (camino más corto)
- Floyd-Warshall (todos los caminos)
- Bellman-Ford
- Kruskal (MST)
- Topological Sort
- Componentes fuertemente conexas (Kosaraju)

### 💡 Programación Dinámica
- Problema de la Mochila (0/1)
- Subsecuencia Común Más Larga (LCS)
- Coin Change
- Longest Increasing Subsequence (LIS)
- Camino mínimo en grid
- Fibonacci optimizado

### 🎯 Algoritmos Greedy
- Mochila Fraccionaria
- Activity Selection
- Kruskal (MST)
- Codificación de Huffman
- Cambio de Monedas (greedy)

### 🔄 Backtracking
- Problema de las N-Reinas
- Solucionador de Sudoku
- Resolución de Laberintos
- Permutaciones y Combinaciones
- Subset Sum

### 🔢 Matemáticas y Algoritmos Numéricos
- Triángulo de Pascal
- Algoritmo de Euclides (MCD, MCM)
- Criba de Eratóstenes
- Exponenciación Modular
- Método de Newton-Raphson
- Interpolación (Lagrange, Newton)
- Regresión Lineal y Polinomial

### 📐 Geometría Computacional
- Distancias (Euclidiana, Manhattan, Chebyshev)
- Área de polígonos (Shoelace)
- Convex Hull (Graham Scan)
- Intersección de líneas y círculos
- Punto en polígono (Ray Casting)

### 📈 Estadística y Análisis de Datos
- Estadísticas descriptivas (media, mediana, moda)
- Varianza y desviación estándar
- Cuartiles y percentiles
- Visualización de datos (matplotlib, seaborn)

### 🤖 Aplicaciones Especiales
- Chatbot con OpenAI API
- Planificación de procesos (FCFS)
- Visualización de datos

## 📦 Requisitos

Las dependencias principales están en `requirements.txt`:

### Científicas
- `numpy` - Operaciones numéricas
- `pandas` - Análisis de datos
- `scipy` - Computación científica
- `scikit-learn` - Machine Learning
- `sympy` - Matemáticas simbólicas

### Visualización
- `matplotlib` - Gráficos básicos
- `seaborn` - Gráficos estadísticos

### Utilidades
- `python-dotenv` - Variables de entorno
- `tabulate` - Tablas formateadas
- `openai` - API de OpenAI (opcional)

### Desarrollo Web (opcional)
- `fastapi` - Framework web
- `uvicorn` - Servidor ASGI

## 📖 Ejemplos de Uso

### Ordenamiento

```python
# Ejecutar archivo
python 36_metodos_ordenamiento.py

# Compara diferentes métodos de ordenamiento
# Incluye análisis de complejidad temporal
```

### Backtracking - N-Reinas

```python
python 47_backtracking.py

# Encuentra todas las soluciones al problema de las N-Reinas
# Visualiza el tablero con las reinas colocadas
```

### Chatbot OpenAI

```python
python 51_openai_chatbot.py

# En el código, descomenta:
main()  # Para seleccionar versión interactivamente
```

### Geometría Computacional

```python
python 50_geometria_computacional.py

# Ejemplos de:
# - Distancias entre puntos
# - Convex Hull
# - Intersecciones
```

## 🎓 Estructura de Cada Archivo

Cada archivo generalmente incluye:
1. **Versión original** (si aplica) - Para comparación
2. **Versiones optimizadas** - Mejoras implementadas
3. **Comparaciones de eficiencia** - Tiempos y complejidad
4. **Ejemplos prácticos** - Casos de uso
5. **Documentación** - Comentarios y docstrings

## 🔧 Configuración Especial

### OpenAI Chatbot

Para usar el chatbot de OpenAI, necesitas:

1. Obtener una API key en [OpenAI Platform](https://platform.openai.com/api-keys)
2. Configurar el archivo `.env`:

```bash
python configurar_env.py
# Luego edita .env y agrega tu API key
```

3. El archivo `.env` está en `.gitignore` por seguridad

## 📊 Estadísticas del Proyecto

- **52 archivos Python**
- **100+ algoritmos implementados**
- **15+ categorías de algoritmos**
- **Código documentado** con docstrings
- **Ejemplos prácticos** en cada archivo
- **Comparaciones de eficiencia** donde aplica

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaFuncionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/NuevaFuncionalidad`)
5. Abre un Pull Request

## 📝 Notas

- Todos los algoritmos están implementados desde cero para fines educativos
- Algunos usan bibliotecas estándar de Python (como `max()`, `sorted()`) para comparación
- Los archivos son independientes y pueden ejecutarse por separado
- El código está optimizado pero también incluye versiones educativas

## 🔗 Recursos Adicionales

- [Documentación de Python](https://docs.python.org/3/)
- [NumPy Documentation](https://numpy.org/doc/)
- [OpenAI API Documentation](https://platform.openai.com/docs)

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo y de aprendizaje.

## 👨‍💻 Autor

Proyecto desarrollado como colección educativa de algoritmos y estructuras de datos en Python.

---

**¡Aprende, practica y diviértete con algoritmos!** 🚀
