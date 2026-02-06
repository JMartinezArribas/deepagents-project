# 🔧 Solución de Problemas

Soluciones a los errores más comunes.

## ❌ Error: "No module named 'typing_extensions'"

### Solución:
```bash
# Asegúrate de estar en el entorno virtual
source venv/bin/activate

# Instala las dependencias en orden
pip install --upgrade pip
pip install typing-extensions
pip install click
pip install ddgs
```

### Si persiste el error:
```bash
# Borra el entorno virtual y créalo de nuevo
deactivate
rm -rf venv
python3 -m venv venv
source venv/bin/activate

# Ejecuta el instalador automático
python install.py
```

## ❌ Error: "Ollama no está instalado"

### Solución para macOS:
1. Ve a https://ollama.com/download
2. Descarga "Ollama-darwin.zip"
3. Descomprime y arrastra a Aplicaciones
4. Abre Ollama desde Aplicaciones
5. Verifica: `ollama --version`

### Si Ollama no responde:
```bash
# En macOS, asegúrate de que Ollama esté corriendo
# Busca el icono de Ollama en la barra de menú (arriba a la derecha)

# Si no está, abre la aplicación Ollama
open -a Ollama

# Espera unos segundos y prueba de nuevo
ollama --version
```

## ❌ Error: "No hay modelos disponibles"

### Solución:
```bash
# Instala el modelo
ollama pull llama3.2

# Verifica que se instaló
ollama list

# Deberías ver algo como:
# NAME            ID              SIZE    MODIFIED
# llama3.2:latest  a80c4f17acd5    2.0 GB  2 hours ago
```

### Si la descarga falla:
```bash
# Intenta con un modelo más pequeño primero
ollama pull llama3.2:1b

# O prueba con otro modelo
ollama pull phi3
```

## ❌ Error: "Command not found: ollama"

### Solución para macOS:
```bash
# Verifica si Ollama está instalado
ls /Applications/Ollama.app

# Si existe pero no se encuentra el comando, añade al PATH
echo 'export PATH="/Applications/Ollama.app/Contents/MacOS:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Si usas bash en lugar de zsh:
echo 'export PATH="/Applications/Ollama.app/Contents/MacOS:$PATH"' >> ~/.bash_profile
source ~/.bash_profile
```

## ❌ Error: "pip: command not found"

### Solución:
```bash
# En macOS, usa pip3
pip3 install -r requirements.txt

# O especifica python3 explícitamente
python3 -m pip install -r requirements.txt
```

## ❌ Error en la búsqueda web (DuckDuckGo)

### Si ves: "RuntimeWarning: This package has been renamed to `ddgs`"

**Solución:**
```bash
# Desinstala el paquete antiguo
pip uninstall duckduckgo-search -y

# Instala el nuevo paquete
pip install ddgs
```

### Si persiste el error:
```bash
# Reinstala desde cero
pip uninstall ddgs -y
pip install --upgrade ddgs
```

## ❌ El agente es muy lento

### Soluciones:

**1. Usa un modelo más pequeño:**
```bash
# En agent.py, cambia el modelo a uno más pequeño
ollama pull llama3.2:1b  # Solo 1.3GB, mucho más rápido
```

Luego en `agent.py` línea 12:
```python
def __init__(self, model="llama3.2:1b"):  # Cambiar aquí
```

**2. Verifica que Ollama use tu GPU (si tienes):**
```bash
# Mientras el agente está corriendo, en otra terminal:
ollama ps

# Deberías ver información sobre el uso de GPU
```

**3. Cierra otras aplicaciones** para liberar RAM

## ❌ Error: "Python version incompatible"

### Solución:
```bash
# Verifica tu versión de Python
python3 --version

# Necesitas Python 3.9 o superior
# En macOS 12.7.6, puedes instalar una versión más nueva:

# Opción 1: Con Homebrew
brew install python@3.11

# Opción 2: Descarga de python.org
# Ve a: https://www.python.org/downloads/
# Descarga Python 3.11 para macOS

# Luego usa python3.11 en lugar de python3
python3.11 -m venv venv
```

## ⚠️ Problemas específicos de macOS 12.7.6

### Si tienes macOS 12.7.6:

```bash
# 1. Asegúrate de usar python3 (no python)
python3 --version

# 2. Instala Xcode Command Line Tools si no los tienes
xcode-select --install

# 3. Actualiza pip
python3 -m pip install --upgrade pip

# 4. Usa python3 explícitamente en todos los comandos
python3 -m venv venv
python3 install.py
python3 test_agent.py
python3 run_agent.py "tu pregunta"
```

## 🆘 Si nada funciona

### Reinstalación completa:

```bash
# 1. Borra todo
deactivate  # Si estás en un venv
cd ..
rm -rf deepagents-research-assistant
rm -rf ~/Library/Application\ Support/Ollama  # Borra datos de Ollama

# 2. Desinstala Ollama
# Arrastra Ollama.app a la Papelera
# Reinicia tu Mac

# 3. Empieza de cero
# Descarga el proyecto de nuevo
# Sigue la Opción A (Instalación Automática) del README
```

## 📝 Obtener ayuda

Si sigues teniendo problemas:

1. **Ejecuta esto y copia el output:**
```bash
python3 --version
ollama --version
ollama list
pip list | grep -E "ddgs|typing|click"
```

2. **Abre un Issue en GitHub** con:
   - Tu sistema operativo y versión
   - El output del comando de arriba
   - El error completo que estás viendo

## ✅ Verificación Final

Cuando todo esté funcionando, deberías ver esto:

```bash
$ python test_agent.py
============================================================
🧪 PRUEBAS DEL AGENTE DE INVESTIGACIÓN
============================================================
🔍 Verificando Ollama...
   ✅ Ollama instalado correctamente
   
🔍 Verificando modelos de Ollama...
   ✅ Modelos disponibles: gemma2:4b, llama3.2, phi3
   
🔍 Verificando dependencias Python...
   ✅ ddgs instalado
   
🔍 Probando búsqueda web...
   ✅ Búsqueda web funcionando
   
🔍 Probando el agente completo...
   ℹ️  Usando modelo: gemma2:4b
   ✅ Agente inicializado correctamente
   💭 Probando con una pregunta simple...
   ✅ Respuesta recibida: Hola...
   
============================================================
📊 RESUMEN
============================================================
✅ Ollama
✅ Modelo
✅ Dependencias
✅ Búsqueda Web
✅ Agente

============================================================
🎉 ¡TODO FUNCIONA! Estás listo para usar el agente.
```

**Nota:** El agente usará automáticamente el primer modelo que encuentre instalado (como tu `gemma2:4b`). No necesitas configurar nada.
