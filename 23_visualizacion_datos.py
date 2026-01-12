# Archivo: 23_visualizacion_datos.py
# Descripción: Visualización de datos con matplotlib y seaborn

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

print("=== Visualización de Datos con Matplotlib y Seaborn ===\n")

# Versión 1: Original
print("=== Versión 1: Original ===")
def configurar_graficos():
    """
    Configura estilos y temas para los gráficos.
    """
    plt.style.use('ggplot')
    sns.set_theme(style='whitegrid')

def graficar_matriz_correlacion(matriz_correlacion):
    """
    Visualiza la matriz de correlación.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm')
    plt.title('Matriz de Correlación')
    plt.tight_layout()
    plt.show()

def graficar_distribucion(df, columna='cnt'):
    """
    Grafica la distribución de la variable especificada.
    """
    plt.figure(figsize=(8, 5))
    sns.histplot(df[columna], bins=30, kde=True)
    plt.title(f"Distribución de '{columna}'")
    plt.xlabel(columna)
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()

def graficar_dispersion(df, columna_x='temp', columna_y='cnt'):
    """
    Grafica un gráfico de dispersión entre dos variables.
    """
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x=columna_x, y=columna_y)
    plt.title(f"Relación entre {columna_x} y {columna_y}")
    plt.xlabel(columna_x)
    plt.ylabel(columna_y)
    plt.tight_layout()
    plt.show()

def graficar_caja(df, columna_x='season', columna_y='cnt'):
    """
    Grafica un diagrama de caja para ver la distribución de 'cnt' por 'season'.
    """
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x=columna_x, y=columna_y)
    plt.title(f"Distribución de {columna_y} por {columna_x}")
    plt.xlabel(columna_x)
    plt.ylabel(columna_y)
    plt.tight_layout()
    plt.show()

print("Versión original definida.\n")

# Versión 2: Optimizada con mejoras
print("=== Versión 2: Optimizada ===")
def configurar_graficos_mejorado(estilo='ggplot', tema_seaborn='whitegrid', figsize_default=(10, 6)):
    """
    Configura estilos y temas para los gráficos con opciones personalizables.
    
    Parámetros:
    - estilo: Estilo de matplotlib ('ggplot', 'seaborn', 'default', etc.)
    - tema_seaborn: Tema de seaborn ('whitegrid', 'darkgrid', 'white', 'dark', 'ticks')
    - figsize_default: Tamaño por defecto de las figuras
    """
    plt.style.use(estilo)
    sns.set_theme(style=tema_seaborn)
    plt.rcParams['figure.figsize'] = figsize_default
    plt.rcParams['font.size'] = 10

def graficar_matriz_correlacion_mejorada(df, figsize=(10, 8), cmap='coolwarm', 
                                        annot=True, fmt='.2f', title='Matriz de Correlación',
                                        guardar=False, nombre_archivo='correlacion.png'):
    """
    Visualiza la matriz de correlación con opciones mejoradas.
    
    Parámetros:
    - df: DataFrame de pandas
    - figsize: Tamaño de la figura
    - cmap: Mapa de colores
    - annot: Si mostrar valores anotados
    - fmt: Formato de anotaciones
    - title: Título del gráfico
    - guardar: Si guardar el gráfico
    - nombre_archivo: Nombre del archivo si se guarda
    """
    # Calcular matriz de correlación si es DataFrame
    if isinstance(df, pd.DataFrame):
        matriz_correlacion = df.corr()
    else:
        matriz_correlacion = df
    
    plt.figure(figsize=figsize)
    sns.heatmap(matriz_correlacion, annot=annot, cmap=cmap, fmt=fmt, 
                square=True, linewidths=0.5, cbar_kws={"shrink": 0.8})
    plt.title(title, fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    if guardar:
        plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
        print(f"Gráfico guardado como {nombre_archivo}")
    
    plt.show()

def graficar_distribucion_mejorada(df, columna='cnt', bins=30, kde=True, 
                                   figsize=(8, 5), title=None, guardar=False, 
                                   nombre_archivo='distribucion.png'):
    """
    Grafica la distribución con opciones mejoradas.
    """
    if columna not in df.columns:
        raise ValueError(f"La columna '{columna}' no existe en el DataFrame")
    
    if title is None:
        title = f"Distribución de '{columna}'"
    
    plt.figure(figsize=figsize)
    sns.histplot(df[columna], bins=bins, kde=kde, stat='density')
    plt.title(title, fontsize=12, fontweight='bold')
    plt.xlabel(columna, fontsize=10)
    plt.ylabel("Densidad" if kde else "Frecuencia", fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    if guardar:
        plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
        print(f"Gráfico guardado como {nombre_archivo}")
    
    plt.show()

def graficar_dispersion_mejorada(df, columna_x='temp', columna_y='cnt', 
                                 hue=None, size=None, alpha=0.6, figsize=(8, 5),
                                 title=None, guardar=False, nombre_archivo='dispersion.png'):
    """
    Grafica un gráfico de dispersión mejorado.
    """
    if columna_x not in df.columns or columna_y not in df.columns:
        raise ValueError("Las columnas especificadas no existen en el DataFrame")
    
    if title is None:
        title = f"Relación entre {columna_x} y {columna_y}"
    
    plt.figure(figsize=figsize)
    sns.scatterplot(data=df, x=columna_x, y=columna_y, hue=hue, size=size, alpha=alpha)
    plt.title(title, fontsize=12, fontweight='bold')
    plt.xlabel(columna_x, fontsize=10)
    plt.ylabel(columna_y, fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    if guardar:
        plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
        print(f"Gráfico guardado como {nombre_archivo}")
    
    plt.show()

def graficar_caja_mejorada(df, columna_x='season', columna_y='cnt', 
                           hue=None, figsize=(8, 5), title=None, 
                           guardar=False, nombre_archivo='boxplot.png'):
    """
    Grafica un diagrama de caja mejorado.
    """
    if columna_x not in df.columns or columna_y not in df.columns:
        raise ValueError("Las columnas especificadas no existen en el DataFrame")
    
    if title is None:
        title = f"Distribución de {columna_y} por {columna_x}"
    
    plt.figure(figsize=figsize)
    sns.boxplot(data=df, x=columna_x, y=columna_y, hue=hue)
    plt.title(title, fontsize=12, fontweight='bold')
    plt.xlabel(columna_x, fontsize=10)
    plt.ylabel(columna_y, fontsize=10)
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    
    if guardar:
        plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
        print(f"Gráfico guardado como {nombre_archivo}")
    
    plt.show()

print("Versión optimizada definida.\n")

# Versión 3: Funciones adicionales útiles
print("=== Versión 3: Funciones Adicionales ===")
def graficar_multiples_distribuciones(df, columnas, ncols=2, figsize=None):
    """
    Grafica múltiples distribuciones en subplots.
    """
    n = len(columnas)
    nrows = (n + ncols - 1) // ncols
    
    if figsize is None:
        figsize = (5 * ncols, 4 * nrows)
    
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize)
    axes = axes.flatten() if n > 1 else [axes]
    
    for i, col in enumerate(columnas):
        if col in df.columns:
            sns.histplot(df[col], bins=30, kde=True, ax=axes[i])
            axes[i].set_title(f"Distribución de '{col}'")
            axes[i].set_xlabel(col)
            axes[i].set_ylabel("Frecuencia")
        else:
            axes[i].text(0.5, 0.5, f"Columna '{col}' no existe", 
                        ha='center', va='center', transform=axes[i].transAxes)
            axes[i].set_title(f"Error: '{col}'")
    
    # Ocultar ejes extra
    for i in range(n, len(axes)):
        axes[i].axis('off')
    
    plt.tight_layout()
    plt.show()

def graficar_pairplot(df, columnas=None, hue=None, figsize=(12, 10)):
    """
    Crea un pairplot (matriz de gráficos de dispersión).
    """
    if columnas is None:
        columnas = df.select_dtypes(include=[np.number]).columns.tolist()
    
    sns.pairplot(df[columnas + ([hue] if hue else [])], hue=hue, height=2)
    plt.tight_layout()
    plt.show()

def graficar_tiempo_series(df, columna_tiempo, columna_valor, figsize=(12, 5)):
    """
    Grafica una serie temporal.
    """
    if columna_tiempo not in df.columns or columna_valor not in df.columns:
        raise ValueError("Las columnas especificadas no existen")
    
    plt.figure(figsize=figsize)
    plt.plot(df[columna_tiempo], df[columna_valor], linewidth=2)
    plt.title(f"Serie Temporal: {columna_valor}", fontsize=12, fontweight='bold')
    plt.xlabel(columna_tiempo, fontsize=10)
    plt.ylabel(columna_valor, fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def graficar_barplot(df, columna_x, columna_y=None, aggfunc='mean', figsize=(8, 5)):
    """
    Grafica un gráfico de barras.
    """
    plt.figure(figsize=figsize)
    
    if columna_y is None:
        # Contar frecuencias
        datos = df[columna_x].value_counts().sort_index()
        sns.barplot(x=datos.index, y=datos.values)
        plt.ylabel("Frecuencia")
    else:
        # Agregar datos
        datos = df.groupby(columna_x)[columna_y].agg(aggfunc).reset_index()
        sns.barplot(data=datos, x=columna_x, y=columna_y)
        plt.ylabel(f"{aggfunc.capitalize()} de {columna_y}")
    
    plt.title(f"Gráfico de Barras: {columna_x}", fontsize=12, fontweight='bold')
    plt.xlabel(columna_x, fontsize=10)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.show()

def graficar_violin(df, columna_x, columna_y, figsize=(8, 5)):
    """
    Grafica un diagrama de violín.
    """
    plt.figure(figsize=figsize)
    sns.violinplot(data=df, x=columna_x, y=columna_y)
    plt.title(f"Diagrama de Violín: {columna_y} por {columna_x}", 
              fontsize=12, fontweight='bold')
    plt.xlabel(columna_x, fontsize=10)
    plt.ylabel(columna_y, fontsize=10)
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.show()

print("Funciones adicionales definidas.\n")

# Versión 4: Clase para gestión de gráficos
print("=== Versión 4: Clase para Gestión de Gráficos ===")
class VisualizadorDatos:
    """
    Clase para gestionar visualizaciones de datos de manera organizada.
    """
    
    def __init__(self, df, estilo='ggplot', tema='whitegrid'):
        """
        Inicializa el visualizador con un DataFrame.
        """
        self.df = df
        configurar_graficos_mejorado(estilo, tema)
    
    def matriz_correlacion(self, **kwargs):
        """Visualiza matriz de correlación."""
        graficar_matriz_correlacion_mejorada(self.df, **kwargs)
    
    def distribucion(self, columna, **kwargs):
        """Visualiza distribución."""
        graficar_distribucion_mejorada(self.df, columna, **kwargs)
    
    def dispersion(self, columna_x, columna_y, **kwargs):
        """Visualiza gráfico de dispersión."""
        graficar_dispersion_mejorada(self.df, columna_x, columna_y, **kwargs)
    
    def caja(self, columna_x, columna_y, **kwargs):
        """Visualiza diagrama de caja."""
        graficar_caja_mejorada(self.df, columna_x, columna_y, **kwargs)
    
    def barplot(self, columna_x, columna_y=None, **kwargs):
        """Visualiza gráfico de barras."""
        graficar_barplot(self.df, columna_x, columna_y, **kwargs)
    
    def violin(self, columna_x, columna_y, **kwargs):
        """Visualiza diagrama de violín."""
        graficar_violin(self.df, columna_x, columna_y, **kwargs)

print("Clase VisualizadorDatos definida.\n")

# Ejemplo de uso (con datos de ejemplo)
print("=== Ejemplo de Uso ===")
print("Creando datos de ejemplo para demostración...")

# Crear DataFrame de ejemplo
np.random.seed(42)
datos_ejemplo = pd.DataFrame({
    'temp': np.random.normal(20, 5, 100),
    'humedad': np.random.normal(60, 15, 100),
    'viento': np.random.normal(10, 3, 100),
    'season': np.random.choice(['Primavera', 'Verano', 'Otoño', 'Invierno'], 100),
    'cnt': np.random.normal(5000, 1000, 100)
})

print(f"DataFrame de ejemplo creado: {datos_ejemplo.shape[0]} filas, {datos_ejemplo.shape[1]} columnas")
print(f"Columnas: {list(datos_ejemplo.columns)}")
print()

# Resumen y mejoras
print("=== Resumen de Análisis ===")
print("Código original:")
print("  ✓ Funciones bien estructuradas")
print("  ✓ Código claro y legible")
print("  ⚠️  Falta validación de errores")
print("  ⚠️  Parámetros fijos (no personalizables)")
print("  ⚠️  No permite guardar gráficos")
print("  ⚠️  Faltan opciones de personalización")
print()
print("Mejoras implementadas:")
print("  1. ✅ Validación de columnas y errores")
print("  2. ✅ Parámetros personalizables")
print("  3. ✅ Opción para guardar gráficos")
print("  4. ✅ Más opciones de personalización (colores, tamaños, etc.)")
print("  5. ✅ Funciones adicionales (multiples distribuciones, pairplot, etc.)")
print("  6. ✅ Clase para gestión organizada")
print("  7. ✅ Mejor formato y estilo de gráficos")
print("  8. ✅ Documentación mejorada")
print()
print("Nota: Para usar las funciones, necesitas tener datos reales.")
print("Ejemplo:")
print("  configurar_graficos_mejorado()")
print("  graficar_matriz_correlacion_mejorada(tu_dataframe)")
print("  graficar_distribucion_mejorada(tu_dataframe, 'columna')")
