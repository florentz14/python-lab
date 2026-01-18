# Archivo: 55_requests_api.py
# Descripción: Trabajo con APIs usando requests - JSONPlaceholder

import requests
import json
from typing import Dict, List, Optional

print("=== Trabajo con APIs usando requests ===\n")
print("API utilizada: JSONPlaceholder (https://jsonplaceholder.typicode.com)\n")

# URL base de la API
BASE_URL = "https://jsonplaceholder.typicode.com"

# =============================================================================
# 1. CONFIGURACIÓN Y VERIFICACIÓN DE CONEXIÓN
# =============================================================================
print("=== 1. Verificación de Conexión ===")

def verificar_conexion():
    """Verifica que la API esté disponible"""
    try:
        response = requests.get(f"{BASE_URL}/posts/1", timeout=5)
        if response.status_code == 200:
            print("✓ Conexión exitosa con JSONPlaceholder API")
            return True
        else:
            print(f"✗ Error: Código de estado {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"✗ Error de conexión: {e}")
        return False

verificar_conexion()

# =============================================================================
# 2. GET - OBTENER DATOS
# =============================================================================
print("\n=== 2. GET - Obtener Datos ===")

def obtener_post(post_id: int) -> Optional[Dict]:
    """Obtiene un post específico por ID"""
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        return response.json()
    return None

def obtener_todos_los_posts() -> List[Dict]:
    """Obtiene todos los posts"""
    response = requests.get(f"{BASE_URL}/posts")
    if response.status_code == 200:
        return response.json()
    return []

def obtener_comentarios_de_post(post_id: int) -> List[Dict]:
    """Obtiene los comentarios de un post específico"""
    response = requests.get(f"{BASE_URL}/posts/{post_id}/comments")
    if response.status_code == 200:
        return response.json()
    return []

# Ejemplos
print("\nObtener un post específico (ID=1):")
post = obtener_post(1)
if post:
    print(f"  Título: {post['title']}")
    print(f"  Autor (userId): {post['userId']}")
    print(f"  Cuerpo: {post['body'][:50]}...")

print("\nObtener todos los posts:")
todos_posts = obtener_todos_los_posts()
print(f"  Total de posts: {len(todos_posts)}")
if todos_posts:
    print(f"  Primer post: {todos_posts[0]['title']}")

print("\nObtener comentarios del post 1:")
comentarios = obtener_comentarios_de_post(1)
print(f"  Total de comentarios: {len(comentarios)}")
if comentarios:
    print(f"  Primer comentario: {comentarios[0]['name']}")

# =============================================================================
# 3. FILTRADO Y BÚSQUEDA
# =============================================================================
print("\n=== 3. Filtrado y Búsqueda ===")

def obtener_posts_por_usuario(user_id: int) -> List[Dict]:
    """Obtiene todos los posts de un usuario específico"""
    response = requests.get(f"{BASE_URL}/posts", params={"userId": user_id})
    if response.status_code == 200:
        return response.json()
    return []

def buscar_posts_por_titulo(palabra_clave: str) -> List[Dict]:
    """Busca posts que contengan una palabra clave en el título"""
    todos_posts = obtener_todos_los_posts()
    return [post for post in todos_posts if palabra_clave.lower() in post['title'].lower()]

# Ejemplos
print("\nPosts del usuario 1:")
posts_usuario1 = obtener_posts_por_usuario(1)
print(f"  Total: {len(posts_usuario1)} posts")
if posts_usuario1:
    print(f"  Primer post: {posts_usuario1[0]['title']}")

print("\nBúsqueda de posts con 'qui' en el título:")
posts_buscados = buscar_posts_por_titulo("qui")
print(f"  Encontrados: {len(posts_buscados)} posts")
for post in posts_buscados[:3]:  # Mostrar primeros 3
    print(f"    - {post['title']}")

# =============================================================================
# 4. POST - CREAR NUEVOS RECURSOS
# =============================================================================
print("\n=== 4. POST - Crear Nuevos Recursos ===")

def crear_post(user_id: int, title: str, body: str) -> Optional[Dict]:
    """Crea un nuevo post"""
    nuevo_post = {
        "userId": user_id,
        "title": title,
        "body": body
    }
    
    response = requests.post(
        f"{BASE_URL}/posts",
        json=nuevo_post,
        headers={"Content-Type": "application/json"}
    )
    
    if response.status_code == 201:
        return response.json()
    return None

def crear_comentario(post_id: int, name: str, email: str, body: str) -> Optional[Dict]:
    """Crea un nuevo comentario"""
    nuevo_comentario = {
        "postId": post_id,
        "name": name,
        "email": email,
        "body": body
    }
    
    response = requests.post(
        f"{BASE_URL}/comments",
        json=nuevo_comentario
    )
    
    if response.status_code == 201:
        return response.json()
    return None

# Ejemplos
print("\nCrear un nuevo post:")
nuevo_post = crear_post(
    user_id=1,
    title="Mi nuevo post de prueba",
    body="Este es el contenido del post creado desde Python usando requests."
)
if nuevo_post:
    print(f"  ✓ Post creado con ID: {nuevo_post.get('id', 'N/A')}")
    print(f"  Título: {nuevo_post['title']}")

print("\nCrear un nuevo comentario:")
nuevo_comentario = crear_comentario(
    post_id=1,
    name="Juan Pérez",
    email="juan@example.com",
    body="Este es un comentario de prueba desde Python."
)
if nuevo_comentario:
    print(f"  ✓ Comentario creado con ID: {nuevo_comentario.get('id', 'N/A')}")

# =============================================================================
# 5. PUT - ACTUALIZAR RECURSOS (REEMPLAZO COMPLETO)
# =============================================================================
print("\n=== 5. PUT - Actualizar Recursos (Reemplazo Completo) ===")

def actualizar_post_put(post_id: int, user_id: int, title: str, body: str) -> Optional[Dict]:
    """Actualiza un post completamente usando PUT"""
    post_actualizado = {
        "id": post_id,
        "userId": user_id,
        "title": title,
        "body": body
    }
    
    response = requests.put(
        f"{BASE_URL}/posts/{post_id}",
        json=post_actualizado
    )
    
    if response.status_code == 200:
        return response.json()
    return None

# Ejemplo
print("\nActualizar post 1 (PUT - reemplazo completo):")
post_actualizado = actualizar_post_put(
    post_id=1,
    user_id=1,
    title="Título actualizado con PUT",
    body="Este es el nuevo contenido del post."
)
if post_actualizado:
    print(f"  ✓ Post actualizado")
    print(f"  Nuevo título: {post_actualizado['title']}")

# =============================================================================
# 6. PATCH - ACTUALIZAR RECURSOS (ACTUALIZACIÓN PARCIAL)
# =============================================================================
print("\n=== 6. PATCH - Actualizar Recursos (Actualización Parcial) ===")

def actualizar_post_patch(post_id: int, **campos) -> Optional[Dict]:
    """Actualiza solo los campos especificados usando PATCH"""
    response = requests.patch(
        f"{BASE_URL}/posts/{post_id}",
        json=campos
    )
    
    if response.status_code == 200:
        return response.json()
    return None

# Ejemplo
print("\nActualizar solo el título del post 1 (PATCH):")
post_parcial = actualizar_post_patch(
    post_id=1,
    title="Solo el título fue actualizado"
)
if post_parcial:
    print(f"  ✓ Post actualizado parcialmente")
    print(f"  Nuevo título: {post_parcial['title']}")

# =============================================================================
# 7. DELETE - ELIMINAR RECURSOS
# =============================================================================
print("\n=== 7. DELETE - Eliminar Recursos ===")

def eliminar_post(post_id: int) -> bool:
    """Elimina un post"""
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    return response.status_code == 200

# Ejemplo
print("\nEliminar post 1:")
if eliminar_post(1):
    print("  ✓ Post eliminado (simulado - JSONPlaceholder no elimina realmente)")

# =============================================================================
# 8. MANIPULACIÓN DE DATOS JSON
# =============================================================================
print("\n=== 8. Manipulación de Datos JSON ===")

def obtener_usuarios() -> List[Dict]:
    """Obtiene todos los usuarios"""
    response = requests.get(f"{BASE_URL}/users")
    if response.status_code == 200:
        return response.json()
    return []

def obtener_albums() -> List[Dict]:
    """Obtiene todos los álbumes"""
    response = requests.get(f"{BASE_URL}/albums")
    if response.status_code == 200:
        return response.json()
    return []

def obtener_todos() -> List[Dict]:
    """Obtiene todos los TODOs"""
    response = requests.get(f"{BASE_URL}/todos")
    if response.status_code == 200:
        return response.json()
    return []

# Análisis de datos
print("\nAnálisis de usuarios:")
usuarios = obtener_usuarios()
print(f"  Total de usuarios: {len(usuarios)}")
if usuarios:
    print(f"  Primer usuario: {usuarios[0]['name']} ({usuarios[0]['email']})")
    print(f"  Ciudad: {usuarios[0]['address']['city']}")

print("\nAnálisis de álbumes:")
albums = obtener_albums()
print(f"  Total de álbumes: {len(albums)}")
if albums:
    print(f"  Primer álbum: {albums[0]['title']}")

print("\nAnálisis de TODOs:")
todos = obtener_todos()
todos_completados = [todo for todo in todos if todo['completed']]
todos_pendientes = [todo for todo in todos if not todo['completed']]
print(f"  Total de TODOs: {len(todos)}")
print(f"  Completados: {len(todos_completados)}")
print(f"  Pendientes: {len(todos_pendientes)}")

# =============================================================================
# 9. ESTADÍSTICAS Y AGRUPACIONES
# =============================================================================
print("\n=== 9. Estadísticas y Agrupaciones ===")

def estadisticas_por_usuario() -> Dict:
    """Calcula estadísticas de posts por usuario"""
    posts = obtener_todos_los_posts()
    estadisticas = {}
    
    for post in posts:
        user_id = post['userId']
        if user_id not in estadisticas:
            estadisticas[user_id] = 0
        estadisticas[user_id] += 1
    
    return estadisticas

def posts_por_usuario() -> Dict[int, List[Dict]]:
    """Agrupa posts por usuario"""
    posts = obtener_todos_los_posts()
    agrupados = {}
    
    for post in posts:
        user_id = post['userId']
        if user_id not in agrupados:
            agrupados[user_id] = []
        agrupados[user_id].append(post)
    
    return agrupados

# Ejemplos
print("\nEstadísticas de posts por usuario:")
stats = estadisticas_por_usuario()
for user_id, cantidad in sorted(stats.items())[:5]:  # Primeros 5
    print(f"  Usuario {user_id}: {cantidad} posts")

print("\nPosts agrupados por usuario (primeros 2 usuarios):")
agrupados = posts_por_usuario()
for user_id in sorted(agrupados.keys())[:2]:
    print(f"  Usuario {user_id}: {len(agrupados[user_id])} posts")
    if agrupados[user_id]:
        print(f"    Ejemplo: {agrupados[user_id][0]['title']}")

# =============================================================================
# 10. MANEJO DE ERRORES Y CÓDIGOS DE ESTADO
# =============================================================================
print("\n=== 10. Manejo de Errores y Códigos de Estado ===")

def obtener_con_manejo_errores(url: str) -> Optional[Dict]:
    """Obtiene datos con manejo completo de errores"""
    try:
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"  ✗ Recurso no encontrado (404)")
            return None
        elif response.status_code == 500:
            print(f"  ✗ Error del servidor (500)")
            return None
        else:
            print(f"  ✗ Código de estado: {response.status_code}")
            return None
            
    except requests.exceptions.Timeout:
        print("  ✗ Timeout: La solicitud tardó demasiado")
        return None
    except requests.exceptions.ConnectionError:
        print("  ✗ Error de conexión")
        return None
    except requests.exceptions.RequestException as e:
        print(f"  ✗ Error en la solicitud: {e}")
        return None

# Ejemplos
print("\nPrueba con URL válida:")
resultado = obtener_con_manejo_errores(f"{BASE_URL}/posts/1")
if resultado:
    print(f"  ✓ Post obtenido: {resultado['title']}")

print("\nPrueba con URL inválida (404):")
resultado = obtener_con_manejo_errores(f"{BASE_URL}/posts/99999")
if not resultado:
    print("  (Manejo de error funcionando correctamente)")

# =============================================================================
# 11. HEADERS Y PARÁMETROS PERSONALIZADOS
# =============================================================================
print("\n=== 11. Headers y Parámetros Personalizados ===")

def obtener_con_headers(url: str, headers: Dict = None) -> Optional[Dict]:
    """Realiza una solicitud con headers personalizados"""
    default_headers = {
        "User-Agent": "Python-Requests/API-Client",
        "Accept": "application/json"
    }
    
    if headers:
        default_headers.update(headers)
    
    response = requests.get(url, headers=default_headers)
    if response.status_code == 200:
        return response.json()
    return None

# Ejemplo
print("\nSolicitud con headers personalizados:")
resultado = obtener_con_headers(
    f"{BASE_URL}/posts/1",
    headers={"X-Custom-Header": "Mi-Valor-Personalizado"}
)
if resultado:
    print(f"  ✓ Post obtenido con headers personalizados")

# =============================================================================
# 12. GUARDAR Y CARGAR DATOS JSON
# =============================================================================
print("\n=== 12. Guardar y Cargar Datos JSON ===")

def guardar_posts_json(archivo: str = "posts_backup.json"):
    """Guarda todos los posts en un archivo JSON"""
    posts = obtener_todos_los_posts()
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)
    print(f"  ✓ {len(posts)} posts guardados en {archivo}")

def cargar_posts_json(archivo: str = "posts_backup.json") -> List[Dict]:
    """Carga posts desde un archivo JSON"""
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            posts = json.load(f)
        print(f"  ✓ {len(posts)} posts cargados desde {archivo}")
        return posts
    except FileNotFoundError:
        print(f"  ✗ Archivo {archivo} no encontrado")
        return []

# Ejemplo
print("\nGuardar posts en archivo:")
guardar_posts_json("posts_backup.json")

print("\nCargar posts desde archivo:")
posts_cargados = cargar_posts_json("posts_backup.json")
if posts_cargados:
    print(f"  Primer post cargado: {posts_cargados[0]['title']}")

# =============================================================================
# 13. FUNCIÓN COMPLETA DE EJEMPLO
# =============================================================================
print("\n=== 13. Función Completa de Ejemplo ===")

def obtener_informacion_completa_usuario(user_id: int) -> Dict:
    """Obtiene información completa de un usuario"""
    # Obtener usuario
    usuario_response = requests.get(f"{BASE_URL}/users/{user_id}")
    usuario = usuario_response.json() if usuario_response.status_code == 200 else None
    
    # Obtener posts del usuario
    posts = obtener_posts_por_usuario(user_id)
    
    # Obtener álbumes del usuario
    albums_response = requests.get(f"{BASE_URL}/albums", params={"userId": user_id})
    albums = albums_response.json() if albums_response.status_code == 200 else []
    
    # Obtener TODOs del usuario
    todos_response = requests.get(f"{BASE_URL}/todos", params={"userId": user_id})
    todos = todos_response.json() if todos_response.status_code == 200 else []
    
    return {
        "usuario": usuario,
        "total_posts": len(posts),
        "total_albums": len(albums),
        "total_todos": len(todos),
        "todos_completados": len([t for t in todos if t['completed']]),
        "posts": posts[:3] if posts else []  # Primeros 3 posts
    }

# Ejemplo
print("\nInformación completa del usuario 1:")
info_usuario = obtener_informacion_completa_usuario(1)
if info_usuario['usuario']:
    print(f"  Nombre: {info_usuario['usuario']['name']}")
    print(f"  Email: {info_usuario['usuario']['email']}")
    print(f"  Posts: {info_usuario['total_posts']}")
    print(f"  Álbumes: {info_usuario['total_albums']}")
    print(f"  TODOs: {info_usuario['total_todos']} ({info_usuario['todos_completados']} completados)")

# =============================================================================
# RESUMEN
# =============================================================================
print("\n=== Resumen de Trabajo con APIs ===")
print("""
Métodos HTTP utilizados:
- GET    : Obtener recursos
- POST   : Crear nuevos recursos
- PUT    : Actualizar recurso completo
- PATCH  : Actualizar recurso parcialmente
- DELETE : Eliminar recursos

Conceptos importantes:
- Status codes: 200 (OK), 201 (Created), 404 (Not Found), 500 (Error)
- JSON: Formato de intercambio de datos
- Headers: Información adicional en las solicitudes
- Parámetros: Filtrado y búsqueda (query parameters)
- Timeout: Límite de tiempo para las solicitudes
- Manejo de errores: Try/except para errores de conexión

Librería requests:
- requests.get()    : Solicitud GET
- requests.post()   : Solicitud POST
- requests.put()    : Solicitud PUT
- requests.patch()  : Solicitud PATCH
- requests.delete() : Solicitud DELETE

JSONPlaceholder API:
- /posts     : Posts de blog
- /users     : Usuarios
- /comments  : Comentarios
- /albums    : Álbumes
- /photos    : Fotos
- /todos     : Lista de tareas

Nota: JSONPlaceholder es una API de prueba que simula un servidor real.
      Los cambios (POST, PUT, DELETE) no se guardan realmente.
""")
