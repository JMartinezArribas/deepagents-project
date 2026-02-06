# 🚀 Cómo Subir Este Proyecto a GitHub

Guía rápida y simple en 5 pasos.

## Paso 1: Instalar Git

Si no tienes Git instalado:
- **Windows**: https://git-scm.com/download/win
- **Mac**: `brew install git` o descarga de https://git-scm.com
- **Linux**: `sudo apt install git` o `sudo yum install git`

## Paso 2: Configurar Git (solo la primera vez)

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@ejemplo.com"
```

## Paso 3: Inicializar Git en el Proyecto

```bash
cd deepagents-research-assistant
git init
git add .
git commit -m "Initial commit: Simple research agent"
```

## Paso 4: Crear Repositorio en GitHub

1. Ve a https://github.com
2. Click en el botón **"+"** (arriba derecha) → **"New repository"**
3. Configura:
   - **Repository name**: `deepagents-research-assistant`
   - **Description**: `Free AI research agent using Ollama + DuckDuckGo`
   - **Public** o Private (tú eliges)
   - **NO** marques ninguna opción de inicialización
4. Click **"Create repository"**

## Paso 5: Conectar y Subir

GitHub te mostrará comandos. Usa estos (reemplaza TU_USUARIO):

```bash
git remote add origin https://github.com/TU_USUARIO/deepagents-research-assistant.git
git branch -M main
git push -u origin main
```

## ✅ ¡Listo!

Tu proyecto ya está en GitHub en:
`https://github.com/TU_USUARIO/deepagents-research-assistant`

## 🔄 Actualizaciones Futuras

Cuando hagas cambios:

```bash
git add .
git commit -m "Descripción de los cambios"
git push
```

## 💡 Tips

1. **README.md** se mostrará automáticamente en GitHub
2. Añade el enlace del repo a tu CV/LinkedIn
3. Agrega temas (topics) en GitHub: `ai`, `research`, `ollama`, `python`
4. ¡Comparte tu repo!

## ⭐ Badge para el README

Añade esto al inicio de tu README.md para mostrar que es open source:

```markdown
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
```
