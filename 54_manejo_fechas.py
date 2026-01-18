# Archivo: 54_manejo_fechas.py
# Descripción: Manejo de Fechas y Tiempo

from datetime import datetime, date, time, timedelta
import calendar
from dateutil import parser
import locale

print("=== Manejo de Fechas y Tiempo ===\n")

# =============================================================================
# 1. FECHA Y HORA ACTUAL
# =============================================================================
print("=== 1. Fecha y Hora Actual ===")

ahora = datetime.now()
hoy = date.today()
hora_actual = datetime.now().time()

print(f"Fecha y hora completa: {ahora}")
print(f"Solo fecha: {hoy}")
print(f"Solo hora: {hora_actual}")

# Componentes individuales
print(f"\nComponentes:")
print(f"  Año: {ahora.year}")
print(f"  Mes: {ahora.month}")
print(f"  Día: {ahora.day}")
print(f"  Hora: {ahora.hour}")
print(f"  Minuto: {ahora.minute}")
print(f"  Segundo: {ahora.second}")
print(f"  Microsegundo: {ahora.microsecond}")

# =============================================================================
# 2. CREAR FECHAS Y HORAS
# =============================================================================
print("\n=== 2. Crear Fechas y Horas ===")

# Crear fecha específica
fecha1 = date(2024, 3, 15)
print(f"Fecha creada: {fecha1}")

# Crear hora específica
hora1 = time(14, 30, 45)
print(f"Hora creada: {hora1}")

# Crear datetime completo
dt1 = datetime(2024, 3, 15, 14, 30, 45)
print(f"DateTime creado: {dt1}")

# Crear desde string
dt2 = datetime.strptime("2024-12-25 10:30:00", "%Y-%m-%d %H:%M:%S")
print(f"Desde string: {dt2}")

# =============================================================================
# 3. FORMATEO DE FECHAS
# =============================================================================
print("\n=== 3. Formateo de Fechas ===")

fecha = datetime(2024, 3, 15, 14, 30, 45)

# Formateo con strftime
formatos = {
    "%Y-%m-%d": fecha.strftime("%Y-%m-%d"),
    "%d/%m/%Y": fecha.strftime("%d/%m/%Y"),
    "%B %d, %Y": fecha.strftime("%B %d, %Y"),
    "%A, %B %d, %Y": fecha.strftime("%A, %B %d, %Y"),
    "%Y-%m-%d %H:%M:%S": fecha.strftime("%Y-%m-%d %H:%M:%S"),
    "%I:%M %p": fecha.strftime("%I:%M %p"),
}

print("Diferentes formatos:")
for formato, resultado in formatos.items():
    print(f"  {formato:20} -> {resultado}")

# Formateo ISO
print(f"\nFormato ISO 8601: {fecha.isoformat()}")
print(f"Formato RFC 2822: {fecha.strftime('%a, %d %b %Y %H:%M:%S %z')}")

# =============================================================================
# 4. OPERACIONES CON FECHAS
# =============================================================================
print("\n=== 4. Operaciones con Fechas ===")

fecha_base = date(2024, 3, 15)

# Sumar días
fecha_futura = fecha_base + timedelta(days=30)
print(f"Fecha base: {fecha_base}")
print(f"30 días después: {fecha_futura}")

# Restar días
fecha_pasada = fecha_base - timedelta(days=15)
print(f"15 días antes: {fecha_pasada}")

# Sumar semanas
fecha_semana = fecha_base + timedelta(weeks=2)
print(f"2 semanas después: {fecha_semana}")

# Sumar meses (aproximado)
fecha_mes = fecha_base + timedelta(days=30)
print(f"~1 mes después: {fecha_mes}")

# Diferencia entre fechas
fecha1 = date(2024, 1, 1)
fecha2 = date(2024, 12, 31)
diferencia = fecha2 - fecha1
print(f"\nDiferencia entre {fecha1} y {fecha2}: {diferencia.days} días")

# =============================================================================
# 5. OPERACIONES CON DATETIME
# =============================================================================
print("\n=== 5. Operaciones con DateTime ===")

dt_base = datetime(2024, 3, 15, 14, 30, 0)

# Sumar horas
dt_futuro = dt_base + timedelta(hours=5)
print(f"5 horas después: {dt_futuro}")

# Sumar minutos
dt_minutos = dt_base + timedelta(minutes=45)
print(f"45 minutos después: {dt_minutos}")

# Sumar segundos
dt_segundos = dt_base + timedelta(seconds=3600)
print(f"3600 segundos después: {dt_segundos}")

# Diferencia de tiempo
dt1 = datetime(2024, 3, 15, 10, 0, 0)
dt2 = datetime(2024, 3, 15, 14, 30, 0)
diferencia_tiempo = dt2 - dt1
print(f"\nDiferencia entre {dt1.time()} y {dt2.time()}:")
print(f"  Horas: {diferencia_tiempo.total_seconds() / 3600:.2f}")
print(f"  Minutos: {diferencia_tiempo.total_seconds() / 60:.0f}")

# =============================================================================
# 6. COMPARACIÓN DE FECHAS
# =============================================================================
print("\n=== 6. Comparación de Fechas ===")

fecha1 = date(2024, 3, 15)
fecha2 = date(2024, 6, 20)
fecha3 = date(2024, 3, 15)

print(f"fecha1: {fecha1}")
print(f"fecha2: {fecha2}")
print(f"fecha3: {fecha3}")

print(f"\nfecha1 < fecha2: {fecha1 < fecha2}")
print(f"fecha1 > fecha2: {fecha1 > fecha2}")
print(f"fecha1 == fecha3: {fecha1 == fecha3}")
print(f"fecha1 != fecha2: {fecha1 != fecha2}")

# =============================================================================
# 7. INFORMACIÓN DEL CALENDARIO
# =============================================================================
print("\n=== 7. Información del Calendario ===")

fecha = date(2024, 3, 15)

# Día de la semana (0=Lunes, 6=Domingo)
dia_semana = fecha.weekday()
print(f"Día de la semana (número): {dia_semana}")
print(f"Día de la semana (nombre): {calendar.day_name[dia_semana]}")

# Día del año
dia_año = fecha.timetuple().tm_yday
print(f"Día del año: {dia_año}")

# Semana del año
semana_año = fecha.isocalendar()[1]
print(f"Semana del año: {semana_año}")

# Días en el mes
dias_mes = calendar.monthrange(2024, 3)[1]
print(f"Días en marzo 2024: {dias_mes}")

# Es año bisiesto
es_bisiesto = calendar.isleap(2024)
print(f"2024 es bisiesto: {es_bisiesto}")

# =============================================================================
# 8. PARSING DE FECHAS DESDE STRING
# =============================================================================
print("\n=== 8. Parsing de Fechas desde String ===")

# Usando strptime con formato conocido
fechas_str = [
    "2024-03-15",
    "15/03/2024",
    "March 15, 2024",
    "2024-03-15 14:30:00",
    "15-Mar-2024"
]

formatos_strptime = [
    "%Y-%m-%d",
    "%d/%m/%Y",
    "%B %d, %Y",
    "%Y-%m-%d %H:%M:%S",
    "%d-%b-%Y"
]

print("Parsing con strptime:")
for fecha_str, formato in zip(fechas_str, formatos_strptime):
    try:
        fecha_parseada = datetime.strptime(fecha_str, formato)
        print(f"  '{fecha_str}' -> {fecha_parseada}")
    except ValueError as e:
        print(f"  '{fecha_str}' -> Error: {e}")

# Usando dateutil.parser (más flexible)
try:
    from dateutil import parser
    fechas_flexibles = [
        "2024-03-15",
        "March 15, 2024",
        "15/03/2024",
        "2024-03-15T14:30:00",
        "15 Mar 2024"
    ]
    
    print("\nParsing con dateutil.parser (más flexible):")
    for fecha_str in fechas_flexibles:
        fecha_parseada = parser.parse(fecha_str)
        print(f"  '{fecha_str}' -> {fecha_parseada}")
except ImportError:
    print("\nNota: dateutil no está instalado. Instala con: pip install python-dateutil")

# =============================================================================
# 9. ZONAS HORARIAS (TIMEZONE)
# =============================================================================
print("\n=== 9. Zonas Horarias ===")

from datetime import timezone

# UTC
utc_ahora = datetime.now(timezone.utc)
print(f"UTC ahora: {utc_ahora}")

# Crear timezone con offset
tz_mexico = timezone(timedelta(hours=-6))  # UTC-6
fecha_tz = datetime(2024, 3, 15, 14, 30, tzinfo=tz_mexico)
print(f"Fecha con timezone (México UTC-6): {fecha_tz}")

# Convertir entre timezones
utc_fecha = fecha_tz.astimezone(timezone.utc)
print(f"Convertida a UTC: {utc_fecha}")

# Nota sobre pytz (más completo)
print("\nNota: Para manejo avanzado de timezones, usa la librería 'pytz'")
print("      Instala con: pip install pytz")

# =============================================================================
# 10. RANGOS DE FECHAS
# =============================================================================
print("\n=== 10. Rangos de Fechas ===")

fecha_inicio = date(2024, 1, 1)
fecha_fin = date(2024, 1, 10)

print(f"Rango: {fecha_inicio} a {fecha_fin}")

# Generar todas las fechas en el rango
fechas_rango = []
fecha_actual = fecha_inicio
while fecha_actual <= fecha_fin:
    fechas_rango.append(fecha_actual)
    fecha_actual += timedelta(days=1)

print("Fechas en el rango:")
for fecha in fechas_rango:
    print(f"  {fecha} ({calendar.day_name[fecha.weekday()]})")

# =============================================================================
# 11. CÁLCULOS ÚTILES
# =============================================================================
print("\n=== 11. Cálculos Útiles ===")

fecha = date(2024, 3, 15)

# Primer día del mes
primer_dia = date(fecha.year, fecha.month, 1)
print(f"Primer día del mes: {primer_dia}")

# Último día del mes
ultimo_dia = date(fecha.year, fecha.month, calendar.monthrange(fecha.year, fecha.month)[1])
print(f"Último día del mes: {ultimo_dia}")

# Primer lunes del mes
primer_lunes = date(fecha.year, fecha.month, 1)
while primer_lunes.weekday() != 0:  # 0 = Lunes
    primer_lunes += timedelta(days=1)
print(f"Primer lunes del mes: {primer_lunes}")

# Días hasta fin de año
fin_año = date(fecha.year, 12, 31)
dias_restantes = (fin_año - fecha).days
print(f"Días hasta fin de año: {dias_restantes}")

# =============================================================================
# 12. TIMESTAMPS (UNIX TIME)
# =============================================================================
print("\n=== 12. Timestamps (Unix Time) ===")

# Convertir datetime a timestamp
dt = datetime(2024, 3, 15, 14, 30, 0)
timestamp = dt.timestamp()
print(f"DateTime: {dt}")
print(f"Timestamp: {timestamp}")

# Convertir timestamp a datetime
dt_desde_timestamp = datetime.fromtimestamp(timestamp)
print(f"Desde timestamp: {dt_desde_timestamp}")

# Timestamp actual
timestamp_ahora = datetime.now().timestamp()
print(f"Timestamp actual: {timestamp_ahora}")

# =============================================================================
# 13. FORMATO RELATIVO (Hace X tiempo)
# =============================================================================
print("\n=== 13. Formato Relativo ===")

def tiempo_relativo(fecha_pasada):
    """Convierte una fecha a formato relativo (hace X tiempo)"""
    ahora = datetime.now()
    diferencia = ahora - fecha_pasada
    
    if diferencia.days > 365:
        años = diferencia.days // 365
        return f"hace {años} año{'s' if años > 1 else ''}"
    elif diferencia.days > 30:
        meses = diferencia.days // 30
        return f"hace {meses} mes{'es' if meses > 1 else ''}"
    elif diferencia.days > 0:
        return f"hace {diferencia.days} día{'s' if diferencia.days > 1 else ''}"
    elif diferencia.seconds > 3600:
        horas = diferencia.seconds // 3600
        return f"hace {horas} hora{'s' if horas > 1 else ''}"
    elif diferencia.seconds > 60:
        minutos = diferencia.seconds // 60
        return f"hace {minutos} minuto{'s' if minutos > 1 else ''}"
    else:
        return "hace unos segundos"

fechas_ejemplo = [
    datetime.now() - timedelta(days=400),
    datetime.now() - timedelta(days=45),
    datetime.now() - timedelta(days=5),
    datetime.now() - timedelta(hours=2),
    datetime.now() - timedelta(minutes=30)
]

print("Formato relativo:")
for fecha in fechas_ejemplo:
    print(f"  {fecha.strftime('%Y-%m-%d %H:%M')} -> {tiempo_relativo(fecha)}")

# =============================================================================
# 14. VALIDACIÓN DE FECHAS
# =============================================================================
print("\n=== 14. Validación de Fechas ===")

def validar_fecha(año, mes, día):
    """Valida si una fecha es válida"""
    try:
        fecha = date(año, mes, día)
        return True, fecha
    except ValueError as e:
        return False, str(e)

fechas_validar = [
    (2024, 2, 29),  # Bisiesto
    (2023, 2, 29),  # No bisiesto
    (2024, 13, 1),  # Mes inválido
    (2024, 12, 32), # Día inválido
    (2024, 4, 15),  # Válida
]

print("Validación de fechas:")
for año, mes, día in fechas_validar:
    es_valida, resultado = validar_fecha(año, mes, día)
    estado = "✓" if es_valida else "✗"
    print(f"  {estado} {año}-{mes:02d}-{día:02d} -> {resultado}")

# =============================================================================
# RESUMEN
# =============================================================================
print("\n=== Resumen de Manejo de Fechas ===")
print("""
Clases principales:
- datetime: Fecha y hora completa
- date: Solo fecha
- time: Solo hora
- timedelta: Diferencia de tiempo

Operaciones comunes:
- datetime.now()          : Fecha/hora actual
- date.today()            : Fecha actual
- strftime()              : Formatear fecha a string
- strptime()              : Parsear string a fecha
- timedelta()             : Operaciones con tiempo
- timestamp()             : Convertir a Unix timestamp

Librerías útiles:
- datetime (built-in)     : Funcionalidad básica
- calendar (built-in)     : Información de calendario
- dateutil               : Parsing flexible (pip install python-dateutil)
- pytz                   : Zonas horarias (pip install pytz)
""")
