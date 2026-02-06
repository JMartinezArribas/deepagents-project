# 🤖 Modelos Compatibles

Este agente funciona con **cualquier modelo de Ollama**. No necesitas usar un modelo específico.

## ✅ Auto-detección de Modelos

El agente **detecta automáticamente** el modelo que tienes instalado. No necesitas configurar nada.

### Ejemplo con tu modelo actual (gemma2:4b)

```bash
# Ya tienes instalado gemma2:4b, perfecto!
$ python run_agent.py "¿Qué es Python?"

ℹ️  Usando modelo: gemma2:4b
🔍 Buscando información sobre: ¿Qué es Python?
💭 Generando respuesta...
...
```

El agente usa automáticamente `gemma2:4b` porque es el que detecta instalado.

## 🎯 Modelos Recomendados

Todos estos modelos funcionan perfectamente:

### Rápidos y Eficientes
- **gemma2:4b** ✅ ← El que TÚ tienes (¡excelente elección!)
- **gemma2:2b** - Más pequeño, más rápido
- **phi3** (2.3GB) - De Microsoft, muy eficiente
- **llama3.2:1b** (1.3GB) - El más pequeño y rápido

### Balanceados (Recomendados)
- **llama3.2** (2.7GB) - Muy popular, buen balance
- **mistral** (4.1GB) - Excelente calidad

### Más Potentes (Requieren más RAM)
- **llama3.1:8b** (8GB) - Muy potente
- **mixtral** (24GB) - Modelo grande, máxima calidad

## 🔄 Cambiar de Modelo

Si quieres usar un modelo diferente, tienes dos opciones:

### Opción 1: El agente usa el primero que encuentra

```bash
# El agente usa automáticamente el primer modelo disponible
$ ollama list
NAME            SIZE
gemma2:4b       2.5 GB  ← Usará este
phi3            2.3 GB
```

### Opción 2: Especificar el modelo manualmente

En tu código Python:

```python
from agent import ResearchAgent

# Usar un modelo específico
agent = ResearchAgent(model="phi3")  # Usa phi3 en lugar de gemma2

respuesta = agent.research("Tu pregunta")
```

## 📥 Instalar Más Modelos

Puedes tener múltiples modelos instalados:

```bash
# Ver modelos disponibles en Ollama
ollama list

# Instalar un modelo adicional
ollama pull llama3.2

# Ahora tienes dos modelos
ollama list
# gemma2:4b
# llama3.2

# El agente usará gemma2:4b (el primero)
# Pero puedes especificar llama3.2 si quieres
```

## 🆚 Comparación de Modelos

| Modelo | Tamaño | Velocidad | Calidad | RAM Mínima |
|--------|--------|-----------|---------|------------|
| gemma2:2b | 1.6GB | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | 4GB |
| **gemma2:4b** | 2.5GB | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 6GB |
| phi3 | 2.3GB | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 6GB |
| llama3.2:1b | 1.3GB | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | 4GB |
| llama3.2 | 2.7GB | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 8GB |
| mistral | 4.1GB | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 8GB |

**Tu modelo actual (gemma2:4b) es una excelente elección:**
- ✅ Tamaño moderado (2.5GB)
- ✅ Buena velocidad
- ✅ Muy buena calidad
- ✅ De Google (bien mantenido)

## 💡 Recomendación

**No necesitas cambiar nada.** Tu `gemma2:4b` funciona perfectamente. 

Solo instalarías otro modelo si:
- Quieres uno más rápido (gemma2:2b, llama3.2:1b)
- Quieres mejor calidad (mistral)
- Tienes problemas de RAM (usa uno más pequeño)

## 🔍 Ver Qué Modelo Está Usando

```bash
# El agente te dice qué modelo usa
$ python run_agent.py "test"

ℹ️  Usando modelo: gemma2:4b  ← Te lo muestra aquí
🔍 Buscando información...
```

## ❓ FAQ

**P: ¿Tengo que instalar llama3.2?**  
R: No. El agente funciona con cualquier modelo, incluyendo tu gemma2:4b.

**P: ¿Puedo usar varios modelos?**  
R: Sí. Instala varios y especifica cuál usar:
```python
agent = ResearchAgent(model="llama3.2")
```

**P: ¿Cuál es mejor?**  
R: Depende de tu uso:
- Para velocidad: gemma2:2b, llama3.2:1b
- Para calidad: mistral
- Balance (tu caso): gemma2:4b ← ¡Perfecto!

**P: ¿Mi modelo es lo suficientemente bueno?**  
R: Sí. gemma2:4b es excelente para uso general. Solo necesitarías cambiar si tienes necesidades muy específicas.

## ✅ Resumen

- ✅ No necesitas cambiar nada
- ✅ gemma2:4b funciona perfectamente
- ✅ El agente lo detecta automáticamente
- ✅ Puedes instalar otros modelos si quieres experimentar

¡Tu configuración actual es perfecta para empezar! 🎉
