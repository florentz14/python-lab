# Archivo: 53_expresiones_regulares.py
# Descripción: Manejo de Expresiones Regulares (Regex)

import re

print("=== Expresiones Regulares (Regex) ===\n")

# =============================================================================
# 1. BÚSQUEDA BÁSICA
# =============================================================================
print("=== 1. Búsqueda Básica ===")

texto = "El teléfono es 555-1234 y el otro es 555-5678"

# Buscar un patrón
patron = r'\d{3}-\d{4}'
resultado = re.search(patron, texto)
if resultado:
    print(f"Patrón encontrado: {resultado.group()}")
    print(f"Posición: {resultado.start()} - {resultado.end()}")

# Buscar todas las ocurrencias
resultados = re.findall(patron, texto)
print(f"Todas las ocurrencias: {resultados}")

# Buscar con información de posición
for match in re.finditer(patron, texto):
    print(f"Encontrado '{match.group()}' en posición {match.start()}-{match.end()}")

# =============================================================================
# 2. METACARACTERES COMUNES
# =============================================================================
print("\n=== 2. Metacaracteres Comunes ===")

texto2 = "Los gatos son lindos. Los perros también. Los pájaros vuelan."

# . (punto) - coincide con cualquier carácter excepto nueva línea
patron1 = r'Los .*os'
print(f"Patrón 'Los .*os': {re.findall(patron1, texto2)}")

# ^ - inicio de cadena
patron2 = r'^Los'
print(f"Patrón '^Los': {re.findall(patron2, texto2)}")

# $ - fin de cadena
patron3 = r'vuelan\.$'
print(f"Patrón 'vuelan\\.$': {re.findall(patron3, texto2)}")

# * - cero o más ocurrencias
patron4 = r'Lo*s'
print(f"Patrón 'Lo*s': {re.findall(patron4, texto2)}")

# + - una o más ocurrencias
patron5 = r'Lo+s'
print(f"Patrón 'Lo+s': {re.findall(patron5, texto2)}")

# ? - cero o una ocurrencia
patron6 = r'colou?r'
texto_color = "color y colour"
print(f"Patrón 'colou?r': {re.findall(patron6, texto_color)}")

# =============================================================================
# 3. CLASES DE CARACTERES
# =============================================================================
print("\n=== 3. Clases de Caracteres ===")

texto3 = "Mi email es usuario123@example.com y el otro es admin@test.org"

# \d - dígitos
digitos = re.findall(r'\d+', texto3)
print(f"Dígitos encontrados: {digitos}")

# \w - caracteres alfanuméricos y guión bajo
palabras = re.findall(r'\w+', texto3)
print(f"Palabras (primeras 5): {palabras[:5]}")

# \s - espacios en blanco
espacios = re.findall(r'\s', texto3)
print(f"Número de espacios: {len(espacios)}")

# Clase personalizada [a-z]
minusculas = re.findall(r'[a-z]+', texto3)
print(f"Palabras en minúsculas (primeras 5): {minusculas[:5]}")

# Clase negada [^0-9] - todo excepto dígitos
no_digitos = re.findall(r'[^0-9\s]+', texto3)
print(f"Sin dígitos ni espacios (primeras 5): {no_digitos[:5]}")

# =============================================================================
# 4. VALIDACIÓN DE EMAIL
# =============================================================================
print("\n=== 4. Validación de Email ===")

def validar_email(email):
    """Valida si un email tiene formato correcto"""
    patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron_email, email))

emails = [
    "usuario@example.com",
    "admin@test.co.uk",
    "nombre.apellido@empresa.org",
    "email_invalido",
    "sin@dominio",
    "test@.com"
]

print("Validación de emails:")
for email in emails:
    es_valido = validar_email(email)
    print(f"  {email:30} -> {'✓ Válido' if es_valido else '✗ Inválido'}")

# =============================================================================
# 5. VALIDACIÓN DE TELÉFONO
# =============================================================================
print("\n=== 5. Validación de Teléfono ===")

def validar_telefono(telefono):
    """Valida formato de teléfono (XXX-XXX-XXXX o (XXX) XXX-XXXX)"""
    patrones = [
        r'^\d{3}-\d{3}-\d{4}$',      # 555-123-4567
        r'^\(\d{3}\)\s\d{3}-\d{4}$',  # (555) 123-4567
        r'^\d{10}$'                    # 5551234567
    ]
    return any(re.match(patron, telefono) for patron in patrones)

telefonos = [
    "555-123-4567",
    "(555) 123-4567",
    "5551234567",
    "55-123-4567",
    "555-1234"
]

print("Validación de teléfonos:")
for tel in telefonos:
    es_valido = validar_telefono(tel)
    print(f"  {tel:20} -> {'✓ Válido' if es_valido else '✗ Inválido'}")

# =============================================================================
# 6. EXTRACCIÓN DE FECHAS
# =============================================================================
print("\n=== 6. Extracción de Fechas ===")

texto_fechas = "La reunión es el 15/03/2024 y otra el 2024-12-25, también hay una el 25 de diciembre de 2024"

# Formato DD/MM/YYYY
fechas_slash = re.findall(r'\d{2}/\d{2}/\d{4}', texto_fechas)
print(f"Fechas formato DD/MM/YYYY: {fechas_slash}")

# Formato YYYY-MM-DD
fechas_guion = re.findall(r'\d{4}-\d{2}-\d{2}', texto_fechas)
print(f"Fechas formato YYYY-MM-DD: {fechas_guion}")

# Formato más flexible
patron_fecha = r'\d{1,2}\s+de\s+\w+\s+de\s+\d{4}'
fechas_texto = re.findall(patron_fecha, texto_fechas)
print(f"Fechas en texto: {fechas_texto}")

# =============================================================================
# 7. REEMPLAZO DE TEXTO
# =============================================================================
print("\n=== 7. Reemplazo de Texto ===")

texto_reemplazo = "El precio es $100.50 y otro es $25.99"

# Reemplazar todos los precios
texto_nuevo = re.sub(r'\$\d+\.\d{2}', '[PRECIO]', texto_reemplazo)
print(f"Original: {texto_reemplazo}")
print(f"Reemplazado: {texto_nuevo}")

# Reemplazar con función
def formatear_precio(match):
    precio = float(match.group().replace('$', ''))
    return f"${precio:,.2f}"

texto_formateado = re.sub(r'\$\d+\.\d{2}', formatear_precio, texto_reemplazo)
print(f"Formateado: {texto_formateado}")

# =============================================================================
# 8. DIVISIÓN DE TEXTO
# =============================================================================
print("\n=== 8. División de Texto ===")

texto_dividir = "palabra1, palabra2; palabra3  palabra4"

# Dividir por múltiples delimitadores
palabras = re.split(r'[,;\s]+', texto_dividir)
print(f"Texto original: {texto_dividir}")
print(f"Palabras divididas: {palabras}")

# Dividir manteniendo delimitadores
palabras_con_delimitadores = re.split(r'([,;])', texto_dividir)
print(f"Con delimitadores: {palabras_con_delimitadores}")

# =============================================================================
# 9. GRUPOS DE CAPTURA
# =============================================================================
print("\n=== 9. Grupos de Captura ===")

texto_grupos = "Juan Pérez tiene 30 años y María García tiene 25 años"

# Capturar nombre y edad
patron_grupo = r'(\w+\s+\w+)\s+tiene\s+(\d+)\s+años'
matches = re.findall(patron_grupo, texto_grupos)

print("Información extraída:")
for nombre, edad in matches:
    print(f"  Nombre: {nombre}, Edad: {edad}")

# Grupos nombrados
patron_nombrado = r'(?P<nombre>\w+\s+\w+)\s+tiene\s+(?P<edad>\d+)\s+años'
match = re.search(patron_nombrado, texto_grupos)
if match:
    print(f"\nGrupos nombrados:")
    print(f"  Nombre completo: {match.group('nombre')}")
    print(f"  Edad: {match.group('edad')}")
    print(f"  Diccionario: {match.groupdict()}")

# =============================================================================
# 10. VALIDACIÓN DE CONTRASEÑA
# =============================================================================
print("\n=== 10. Validación de Contraseña ===")

def validar_contraseña(contraseña):
    """
    Valida que la contraseña tenga:
    - Al menos 8 caracteres
    - Al menos una mayúscula
    - Al menos una minúscula
    - Al menos un dígito
    - Al menos un carácter especial
    """
    if len(contraseña) < 8:
        return False, "Debe tener al menos 8 caracteres"
    
    if not re.search(r'[A-Z]', contraseña):
        return False, "Debe tener al menos una mayúscula"
    
    if not re.search(r'[a-z]', contraseña):
        return False, "Debe tener al menos una minúscula"
    
    if not re.search(r'\d', contraseña):
        return False, "Debe tener al menos un dígito"
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', contraseña):
        return False, "Debe tener al menos un carácter especial"
    
    return True, "Contraseña válida"

contraseñas = [
    "Password123!",
    "weak",
    "NOMAYUSCULAS123!",
    "NoNumeros!",
    "SinEspeciales123"
]

print("Validación de contraseñas:")
for pwd in contraseñas:
    es_valida, mensaje = validar_contraseña(pwd)
    estado = "✓" if es_valida else "✗"
    print(f"  {estado} {pwd:20} -> {mensaje}")

# =============================================================================
# 11. EXTRACCIÓN DE URL
# =============================================================================
print("\n=== 11. Extracción de URL ===")

texto_urls = "Visita https://www.example.com o http://test.org/path?query=1"

patron_url = r'https?://[^\s]+'
urls = re.findall(patron_url, texto_urls)
print(f"URLs encontradas: {urls}")

# Extraer componentes de URL
def parsear_url(url):
    patron = r'(https?)://([^/]+)(/.*)?'
    match = re.match(patron, url)
    if match:
        protocolo, dominio, ruta = match.groups()
        return {
            'protocolo': protocolo,
            'dominio': dominio,
            'ruta': ruta if ruta else '/'
        }
    return None

for url in urls:
    componentes = parsear_url(url)
    print(f"  {url}")
    if componentes:
        for key, value in componentes.items():
            print(f"    {key}: {value}")

# =============================================================================
# 12. LIMPIEZA DE TEXTO
# =============================================================================
print("\n=== 12. Limpieza de Texto ===")

texto_sucio = "Este   texto    tiene    muchos    espacios    y\n\ntambien\n\nsaltos de línea"

# Eliminar espacios múltiples
texto_limpio1 = re.sub(r'\s+', ' ', texto_sucio)
print(f"Sin espacios múltiples: {texto_limpio1}")

# Eliminar saltos de línea múltiples
texto_limpio2 = re.sub(r'\n+', '\n', texto_sucio)
print(f"Sin saltos múltiples:\n{texto_limpio2}")

# Eliminar caracteres especiales (solo letras, números y espacios)
texto_especial = "¡Hola! ¿Cómo estás? #Python @2024"
texto_solo_alfanumerico = re.sub(r'[^\w\s]', '', texto_especial)
print(f"Sin caracteres especiales: {texto_solo_alfanumerico}")

# =============================================================================
# 13. BÚSQUEDA CASE-INSENSITIVE
# =============================================================================
print("\n=== 13. Búsqueda Case-Insensitive ===")

texto_mixto = "Python es genial. PYTHON es poderoso. python es fácil."

# Búsqueda normal (case-sensitive)
matches1 = re.findall(r'python', texto_mixto)
print(f"Case-sensitive 'python': {matches1}")

# Búsqueda case-insensitive
matches2 = re.findall(r'python', texto_mixto, re.IGNORECASE)
print(f"Case-insensitive 'python': {matches2}")

# Con flags múltiples
matches3 = re.findall(r'^python', texto_mixto, re.IGNORECASE | re.MULTILINE)
print(f"Con MULTILINE: {matches3}")

# =============================================================================
# 14. LOOKAHEAD Y LOOKBEHIND
# =============================================================================
print("\n=== 14. Lookahead y Lookbehind ===")

texto_look = "El precio es $100 y el costo es $50"

# Positive lookahead - encuentra $ seguido de número
precios = re.findall(r'\$\d+(?=\s|$)', texto_look)
print(f"Precios (lookahead): {precios}")

# Positive lookbehind - encuentra número precedido de $
numeros = re.findall(r'(?<=\$)\d+', texto_look)
print(f"Números después de $ (lookbehind): {numeros}")

# Negative lookahead - encuentra palabra que NO es seguida de espacio
palabras_sin_espacio = re.findall(r'\w+(?!\s)', texto_look)
print(f"Palabras sin espacio después: {palabras_sin_espacio[:5]}")

# =============================================================================
# RESUMEN
# =============================================================================
print("\n=== Resumen de Expresiones Regulares ===")
print("""
Metacaracteres importantes:
- .     : Cualquier carácter
- ^     : Inicio de cadena
- $     : Fin de cadena
- *     : Cero o más
- +     : Una o más
- ?     : Cero o una
- {n}   : Exactamente n veces
- {n,m} : Entre n y m veces
- []    : Clase de caracteres
- |     : OR (alternativa)
- ()    : Grupo de captura

Clases predefinidas:
- \\d    : Dígito [0-9]
- \\w    : Carácter alfanumérico [a-zA-Z0-9_]
- \\s    : Espacio en blanco
- \\D    : No dígito
- \\W    : No alfanumérico
- \\S    : No espacio

Funciones principales:
- re.search()   : Busca primera ocurrencia
- re.findall()  : Busca todas las ocurrencias
- re.finditer() : Itera sobre todas las ocurrencias
- re.match()    : Coincide desde el inicio
- re.sub()      : Reemplaza coincidencias
- re.split()    : Divide por patrón
""")
