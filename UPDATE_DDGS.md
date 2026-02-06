# 🔄 Actualización del Paquete de Búsqueda

## ⚠️ Cambio Importante

El paquete `duckduckgo-search` ha sido renombrado a `ddgs`.

Si ves este warning:
```
RuntimeWarning: This package (duckduckgo_search) has been renamed to `ddgs`! 
Use `pip install ddgs` instead.
```

**No te preocupes, es fácil de solucionar.**

## ✅ Solución Rápida (2 minutos)

```bash
# 1. Activar entorno virtual
source venv/bin/activate  # Mac/Linux
# o
venv\Scripts\activate     # Windows

# 2. Desinstalar paquete antiguo
pip uninstall duckduckgo-search -y

# 3. Instalar paquete nuevo
pip install ddgs

# 4. Verificar
python test_agent.py
```

¡Listo! El warning desaparecerá.

## 🔍 ¿Por Qué Este Cambio?

Los desarrolladores del paquete lo renombraron para:
- Nombre más corto y fácil de recordar
- Evitar confusión con otros paquetes
- Mejor mantenimiento

**El paquete es el mismo, solo cambió el nombre.**

## 📋 Verificar Qué Tienes Instalado

```bash
# Ver qué paquetes tienes
pip list | grep -E "ddgs|duckduckgo"

# Si ves "duckduckgo-search" → necesitas actualizar
# Si ves "ddgs" → estás actualizado ✅
```

## 🆕 Para Instalaciones Nuevas

Si estás instalando desde cero, simplemente usa:

```bash
pip install ddgs
```

Ya no necesitas instalar `duckduckgo-search`.

## ❓ FAQ

**P: ¿Afecta la funcionalidad?**  
R: No. El paquete funciona exactamente igual, solo cambió el nombre.

**P: ¿Necesito cambiar mi código?**  
R: No. El proyecto ya está actualizado para usar `ddgs`.

**P: ¿Puedo tener ambos instalados?**  
R: Sí, pero no es necesario. Es mejor tener solo `ddgs`.

**P: ¿Esto afecta mi modelo de Ollama?**  
R: No. Solo es el paquete de búsqueda web. Tu modelo (gemma2:4b) no se afecta.

## ✨ Confirmación de Actualización

Después de actualizar, cuando ejecutes el agente deberías ver:

```bash
$ python run_agent.py "test"

ℹ️  Usando modelo: gemma2:4b
🔍 Buscando información sobre: test
💭 Generando respuesta...
```

**Sin warnings.** ✅

## 🔧 Si Tienes Problemas

Si después de actualizar sigues viendo el warning:

```bash
# Limpieza completa
pip uninstall duckduckgo-search ddgs -y
pip cache purge
pip install ddgs

# Reinicia tu terminal
# Activa el entorno virtual de nuevo
source venv/bin/activate

# Prueba
python test_agent.py
```

---

**Resumen:** Solo cambia `duckduckgo-search` por `ddgs`. ¡Es todo! 🎉
