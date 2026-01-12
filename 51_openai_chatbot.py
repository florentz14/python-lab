# Archivo: 51_openai_chatbot.py
# Descripción: Chatbot con OpenAI - Versiones Optimizadas

import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

print("=== Chatbot con OpenAI ===\n")

# =============================================================================
# VERSIÓN 1: API Moderna (Recomendada)
# =============================================================================

try:
    from openai import OpenAI
    
    def chatbot_openai_moderno():
        """
        Chatbot usando la API moderna de OpenAI (v1.0+).
        
        Mejoras:
        - API moderna (OpenAI client)
        - API key desde variable de entorno (seguro)
        - Mejor manejo de errores
        - Modelo actualizado (gpt-3.5-turbo)
        - Mantiene contexto de conversación
        """
        # Obtener API key desde variable de entorno
        api_key = os.getenv("OPENAI_API_KEY")
        
        if not api_key:
            print("ERROR: OPENAI_API_KEY no encontrada en variables de entorno")
            print("Por favor, crea un archivo .env con: OPENAI_API_KEY=tu_api_key")
            return
        
        # Inicializar cliente
        client = OpenAI(api_key=api_key)
        
        print("Chatbot OpenAI iniciado. Escribe 'exit' o 'quit' para salir.")
        print("Escribe 'help' para ver comandos disponibles.\n")
        
        historial = []  # Para mantener contexto de la conversación
        
        while True:
            try:
                prompt = input("\nTú: ").strip()
                
                if not prompt:
                    continue
                
                # Comandos especiales
                if prompt.lower() in ['exit', 'quit', 'salir']:
                    print("¡Hasta luego!")
                    break
                
                if prompt.lower() == 'help':
                    print("\nComandos disponibles:")
                    print("  exit/quit/salir - Salir del chatbot")
                    print("  help - Mostrar esta ayuda")
                    print("  clear - Limpiar historial de conversación")
                    continue
                
                if prompt.lower() == 'clear':
                    historial = []
                    print("Historial limpiado.")
                    continue
                
                # Agregar mensaje del usuario al historial
                historial.append({"role": "user", "content": prompt})
                
                # Hacer petición a OpenAI
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",  # Modelo moderno (más barato)
                    # model="gpt-4",  # Modelo más potente pero más caro
                    messages=historial,
                    max_tokens=1000,
                    temperature=0.7  # Controla la creatividad (0-1)
                )
                
                # Obtener respuesta
                respuesta = response.choices[0].message.content
                
                # Agregar respuesta al historial
                historial.append({"role": "assistant", "content": respuesta})
                
                print(f"\nAsistente: {respuesta}")
                
            except KeyboardInterrupt:
                print("\n\nInterrumpido por el usuario. ¡Hasta luego!")
                break
            except Exception as e:
                print(f"\nERROR: {type(e).__name__}: {e}")
                print("Intenta de nuevo o escribe 'exit' para salir.")
    
    # Descomentar para usar:
    # chatbot_openai_moderno()
    
except ImportError:
    print("ERROR: openai no está instalado.")
    print("Instala con: pip install openai")
    print()

# =============================================================================
# VERSIÓN 2: Con Streaming (Respuestas en Tiempo Real)
# =============================================================================

def chatbot_openai_streaming():
    """
    Chatbot con streaming para ver respuestas en tiempo real.
    
    Ventajas:
    - Muestra la respuesta mientras se genera
    - Mejor experiencia de usuario
    - Útil para respuestas largas
    """
    try:
        from openai import OpenAI
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("ERROR: OPENAI_API_KEY no encontrada en variables de entorno")
            print("Por favor, crea un archivo .env con: OPENAI_API_KEY=tu_api_key")
            return
        
        client = OpenAI(api_key=api_key)
        historial = []
        
        print("Chatbot OpenAI (Streaming) iniciado. Escribe 'exit' para salir.\n")
        
        while True:
            try:
                prompt = input("\nTú: ").strip()
                
                if not prompt:
                    continue
                
                if prompt.lower() in ['exit', 'quit']:
                    print("¡Hasta luego!")
                    break
                
                historial.append({"role": "user", "content": prompt})
                
                print("\nAsistente: ", end="", flush=True)
                
                # Streaming response
                stream = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=historial,
                    max_tokens=1000,
                    temperature=0.7,
                    stream=True
                )
                
                respuesta_completa = ""
                for chunk in stream:
                    if chunk.choices[0].delta.content is not None:
                        contenido = chunk.choices[0].delta.content
                        print(contenido, end="", flush=True)
                        respuesta_completa += contenido
                
                historial.append({"role": "assistant", "content": respuesta_completa})
                print()  # Nueva línea después de la respuesta
                
            except KeyboardInterrupt:
                print("\n\nInterrumpido. ¡Hasta luego!")
                break
            except Exception as e:
                print(f"\nERROR: {e}")
    
    except ImportError:
        print("ERROR: openai no está instalado.")
        print("Instala con: pip install openai")

# =============================================================================
# VERSIÓN 3: Con Configuración Avanzada
# =============================================================================

def chatbot_avanzado():
    """
    Chatbot con configuraciones avanzadas:
    - Múltiples modelos
    - Control de temperatura
    - Límite de tokens
    - Manejo de errores robusto
    - Información de uso (tokens)
    """
    try:
        from openai import OpenAI
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("ERROR: OPENAI_API_KEY no encontrada en variables de entorno")
            print("Por favor, crea un archivo .env con: OPENAI_API_KEY=tu_api_key")
            return
        
        client = OpenAI(api_key=api_key)
        
        # Configuración
        CONFIG = {
            "modelo": "gpt-3.5-turbo",  # gpt-3.5-turbo, gpt-4, gpt-4-turbo
            "temperatura": 0.7,  # 0.0 (determinístico) a 2.0 (muy creativo)
            "max_tokens": 1000,
            "top_p": 1.0,  # Nucleus sampling
            "frequency_penalty": 0.0,  # Penalizar repeticiones
            "presence_penalty": 0.0  # Penalizar nuevos temas
        }
        
        historial = []
        num_mensajes = 0
        
        print("Chatbot OpenAI Avanzado")
        print(f"Modelo: {CONFIG['modelo']}")
        print(f"Temperatura: {CONFIG['temperatura']}")
        print("Escribe 'exit' para salir, 'config' para cambiar configuración\n")
        
        while True:
            try:
                prompt = input("\nTú: ").strip()
                
                if not prompt:
                    continue
                
                if prompt.lower() == 'exit':
                    print(f"\nTotal de mensajes: {num_mensajes}")
                    print("¡Hasta luego!")
                    break
                
                if prompt.lower() == 'config':
                    print("\nConfiguración actual:")
                    for key, value in CONFIG.items():
                        print(f"  {key}: {value}")
                    continue
                
                historial.append({"role": "user", "content": prompt})
                num_mensajes += 1
                
                response = client.chat.completions.create(
                    model=CONFIG["modelo"],
                    messages=historial,
                    max_tokens=CONFIG["max_tokens"],
                    temperature=CONFIG["temperatura"],
                    top_p=CONFIG["top_p"],
                    frequency_penalty=CONFIG["frequency_penalty"],
                    presence_penalty=CONFIG["presence_penalty"]
                )
                
                respuesta = response.choices[0].message.content
                historial.append({"role": "assistant", "content": respuesta})
                
                # Información adicional
                tokens_usados = response.usage.total_tokens
                print(f"\nAsistente: {respuesta}")
                print(f"[Tokens usados: {tokens_usados}]")
                
            except KeyboardInterrupt:
                print("\n\nInterrumpido. ¡Hasta luego!")
                break
            except Exception as e:
                error_msg = str(e)
                if "rate_limit" in error_msg.lower():
                    print("\nERROR: Límite de peticiones excedido. Espera un momento.")
                elif "insufficient_quota" in error_msg.lower():
                    print("\nERROR: Cuota insuficiente. Verifica tu plan de OpenAI.")
                elif "invalid_api_key" in error_msg.lower():
                    print("\nERROR: API key inválida. Verifica tu OPENAI_API_KEY.")
                else:
                    print(f"\nERROR: {e}")
    
    except ImportError:
        print("ERROR: openai no está instalado.")
        print("Instala con: pip install openai")


# =============================================================================
# FUNCIÓN PRINCIPAL
# =============================================================================

def main():
    """Función principal para seleccionar la versión del chatbot."""
    print("Selecciona la versión del chatbot:")
    print("1. Versión estándar (recomendada)")
    print("2. Versión con streaming")
    print("3. Versión avanzada (con configuración)")
    
    try:
        opcion = input("\nOpción (1-3): ").strip()
        
        if opcion == "1":
            chatbot_openai_moderno()
        elif opcion == "2":
            chatbot_openai_streaming()
        elif opcion == "3":
            chatbot_avanzado()
        else:
            print("Opción inválida. Ejecutando versión estándar...")
            chatbot_openai_moderno()
    except KeyboardInterrupt:
        print("\n\nOperación cancelada.")


if __name__ == "__main__":
    # Ejecutar función principal
    # Descomentar la siguiente línea para ejecutar:
    # main()
    
    # O ejecutar directamente una versión específica:
    # chatbot_openai_moderno()
    pass
