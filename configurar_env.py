# Script para configurar el archivo .env
# Ejecuta este script para crear el archivo .env a partir de la plantilla

import os
import shutil

def configurar_env():
    """Crea el archivo .env si no existe."""
    archivo_env = ".env"
    plantilla = "env_template.txt"
    
    if os.path.exists(archivo_env):
        print(f"El archivo {archivo_env} ya existe.")
        respuesta = input("¿Deseas sobrescribirlo? (s/n): ").lower()
        if respuesta != 's':
            print("Operación cancelada.")
            return
    
    if not os.path.exists(plantilla):
        print(f"Error: No se encontró el archivo {plantilla}")
        return
    
    # Copiar plantilla
    shutil.copy(plantilla, archivo_env)
    print(f"Archivo {archivo_env} creado desde {plantilla}")
    print(f"\nIMPORTANTE:")
    print(f"1. Abre el archivo {archivo_env}")
    print(f"2. Reemplaza 'tu_api_key_aqui' con tu API key real de OpenAI")
    print(f"3. Guarda el archivo")
    print(f"\nObtén tu API key en: https://platform.openai.com/api-keys")

if __name__ == "__main__":
    configurar_env()
