# 🤖 DeepAgents Research Assistant

Un agente de investigación AI gratuito.


## 🎯 ¿Qué hace este proyecto?

Este agente puede:
- 🔍 Buscar información en internet
- 💭 Analizar y sintetizar resultados
- 📝 Generar respuestas completas
- 💯 Todo 100% gratis

**✨ Funciona con cualquier modelo de Ollama** - No necesitas un modelo específico. El agente detecta automáticamente el modelo que tienes instalado (como `llama3.2`, `gemma3`, `phi3`, etc.)

## 📋 Lo que necesitas

- Python 3.9 o superior
- 8GB de RAM (16GB recomendado)
- 10GB de espacio en disco
- Internet (solo para búsquedas web)

## 🚀 Instalación 

### Opción A: Instalación Automática (Recomendada)

```bash
# 1. Descomprimir el proyecto
cd deepagents-research-assistant

# 2. Crear entorno virtual
python3 -m venv venv

# 3. Activar entorno virtual
# En Mac/Linux:
source venv/bin/activate
# En Windows:
venv\Scripts\activate

# 4. Ejecutar instalador automático
python install.py
```

El script `install.py` instalará todo automáticamente. ¡Solo espera!

### Opción B: Instalación Manual

Si prefieres hacerlo paso a paso:

**Paso 1: Crear entorno virtual**
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**Paso 2: Instalar dependencias**
```bash
pip install --upgrade pip
pip install typing-extensions click ddgs
```

**Paso 3: Instalar Ollama**
- Ve a https://ollama.com/download
- Descarga para tu sistema operativo (macOS, Windows, Linux)
- Instala el programa

**Paso 4: Descargar un modelo**

Puedes usar **cualquier modelo** de Ollama. Ejemplos:

```bash
# Opción 1: Llama (recomendado)
ollama pull llama3.2

# Opción 2: Gemma (de Google, muy eficiente)
ollama pull gemma3:4b

# Opción 3: Phi (de Microsoft, compacto)
ollama pull phi3

# Opción 4: Mistral (más potente)
ollama pull mistral
```

**El agente detecta automáticamente el modelo que instales.** No necesitas configurar nada. Ver [MODELS.md](MODELS.md) para más detalles.

**Paso 5: Verificar instalación**
```bash
python test_agent.py
```

## ✅ Probar que funciona

Ejecuta el script de prueba:

```bash
python test_agent.py
```

Deberías ver algo como:

```
✅ Ollama instalado
✅ Modelo gemma3:4b disponible
✅ Búsqueda web funcionando
🚀 Todo listo para usar!

Probando el agente con una pregunta simple...
Respuesta: [El agente responderá aquí]
```

## 📖 Cómo usar

### Uso básico en línea de comandos

```bash
python run_agent.py "¿Qué es la inteligencia artificial?"
```

### Uso en tu código Python

```python
from agent import ResearchAgent

# Crear el agente
agent = ResearchAgent()

# Hacer una pregunta
respuesta = agent.research("¿Qué es machine learning?")
print(respuesta)
```

## 📁 Estructura del proyecto

```
deepagents-research-assistant/
│
├── agent.py                # El agente principal (código simple)
├── search.py               # Búsqueda web gratuita
├── run_agent.py           # Script para línea de comandos
├── test_agent.py          # Script de prueba
├── requirements.txt       # Dependencias Python
├── README.md              # Este archivo
└── examples/              # Ejemplos de uso
    └── example.py
```

## 🔧 Solución de problemas

### "Ollama no está instalado"
```bash
# Verifica la instalación
ollama --version

# Si no está instalado, descarga de:
# https://ollama.com/download
```

### "No hay modelos disponibles"
```bash
# Instala el modelo
ollama pull gemma3:4b

# Verifica que se instaló
ollama list
```

### "Error de importación"
```bash
# Asegúrate de estar en el entorno virtual
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Reinstala dependencias
pip install -r requirements.txt
```

## 💡 Ejemplos

### Ejemplo 1: Pregunta simple
```bash
python run_agent.py "¿Qué es Python?"
```

### Ejemplo 2: Investigación más profunda
```bash
python run_agent.py "Explica las diferencias entre machine learning y deep learning"
```

### Ejemplo 3: Usar en tu código
```python
from agent import ResearchAgent

agent = ResearchAgent()

preguntas = [
    "¿Qué es blockchain?",
    "¿Cómo funciona el machine learning?",
    "¿Qué son las redes neuronales?"
]

for pregunta in preguntas:
    print(f"\n❓ {pregunta}")
    respuesta = agent.research(pregunta)
    print(f"💬 {respuesta}\n")
```

## 📊 Costos

- ✅ Software: **0€**
- ✅ Modelos AI: **0€**
- ✅ Búsquedas web: **0€**
- ✅ Uso ilimitado: **0€**

**Total: 0€ para siempre** 🎉

## 🤝 Contribuir

¿Quieres mejorar el proyecto? ¡Genial!

1. Fork el repositorio
2. Crea una rama: `git checkout -b mi-mejora`
3. Haz commit: `git commit -m "Agrego X funcionalidad"`
4. Push: `git push origin mi-mejora`
5. Abre un Pull Request

## 📄 Licencia

MIT License - Úsalo como quieras

## 🆘 ¿Necesitas ayuda?

- 📖 Lee este README completo
- 🐛 Abre un Issue en GitHub
- 💬 Pregunta en las Discussions del repo

## ⭐ Si te gusta el proyecto

Dale una estrella ⭐ en GitHub y compártelo con otros!

