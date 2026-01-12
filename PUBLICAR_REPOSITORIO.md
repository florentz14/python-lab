# Guía para Publicar el Repositorio en GitHub

## ✅ Estado Actual

El repositorio local ya está configurado con:
- ✅ Git inicializado
- ✅ Archivos agregados al staging
- ✅ Commit inicial realizado
- ✅ .gitignore configurado (protege .env)

## 📋 Pasos para Publicar en GitHub

### Opción 1: Usando GitHub CLI (Recomendado)

Si tienes GitHub CLI instalado:

```bash
# Crear repositorio y publicar
gh repo create python-lab --public --source=. --remote=origin --push
```

### Opción 2: Manual (Paso a Paso)

#### 1. Crear Repositorio en GitHub

1. Ve a [GitHub.com](https://github.com) e inicia sesión
2. Haz clic en el botón **"+"** (arriba derecha) → **"New repository"**
3. Configura el repositorio:
   - **Repository name**: `python-lab` (o el nombre que prefieras)
   - **Description**: "Colección completa de algoritmos y estructuras de datos en Python"
   - **Visibility**: Público o Privado (según prefieras)
   - **NO** marques "Initialize with README" (ya tenemos uno)
   - **NO** agregues .gitignore ni licencia (ya los tenemos)
4. Haz clic en **"Create repository"**

#### 2. Conectar Repositorio Local con GitHub

Después de crear el repositorio, GitHub te mostrará comandos. Usa estos:

```bash
# Agregar el repositorio remoto (reemplaza USERNAME con tu usuario de GitHub)
git remote add origin https://github.com/USERNAME/python-lab.git

# O si prefieres SSH:
# git remote add origin git@github.com:USERNAME/python-lab.git

# Verificar que se agregó correctamente
git remote -v
```

#### 3. Publicar el Código

```bash
# Cambiar a la rama main (si no estás ya en ella)
git branch -M main

# Subir el código a GitHub
git push -u origin main
```

#### 4. Verificar

Ve a tu repositorio en GitHub y verifica que todos los archivos estén presentes.

## 🔐 Configuración de Autenticación

### Si usas HTTPS:

GitHub ya no acepta contraseñas. Necesitas un **Personal Access Token**:

1. Ve a GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Genera un nuevo token con permisos `repo`
3. Usa el token como contraseña cuando Git te lo pida

### Si usas SSH:

```bash
# Verificar si tienes clave SSH
ls -al ~/.ssh

# Si no tienes, generar una:
ssh-keygen -t ed25519 -C "tu_email@example.com"

# Agregar la clave a ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copiar la clave pública
cat ~/.ssh/id_ed25519.pub

# Agregar la clave en GitHub:
# Settings → SSH and GPG keys → New SSH key
```

## 📝 Comandos Rápidos

```bash
# Ver estado
git status

# Ver commits
git log --oneline

# Ver remoto configurado
git remote -v

# Subir cambios futuros
git add .
git commit -m "Descripción del cambio"
git push
```

## ⚠️ Importante

- ✅ El archivo `.env` está en `.gitignore` y NO se subirá (seguro)
- ✅ Solo se subirán los archivos de código y documentación
- ✅ El README.md ya está incluido y se mostrará en GitHub

## 🎉 ¡Listo!

Una vez publicado, tu repositorio estará disponible en:
`https://github.com/USERNAME/python-lab`
