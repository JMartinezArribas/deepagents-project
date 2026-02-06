"""
Ejemplo de cómo usar el agente en tu código

Ejecuta: python examples/example.py
"""
from agent import ResearchAgent


def ejemplo_basico():
    """Ejemplo básico de uso"""
    print("=" * 60)
    print("EJEMPLO 1: Uso Básico")
    print("=" * 60)
    
    # Crear el agente
    agent = ResearchAgent()
    
    # Hacer una pregunta
    pregunta = "¿Qué es la inteligencia artificial?"
    print(f"\n❓ {pregunta}\n")
    
    respuesta = agent.research(pregunta)
    print(f"💬 {respuesta}\n")


def ejemplo_multiple():
    """Ejemplo con múltiples preguntas"""
    print("\n" + "=" * 60)
    print("EJEMPLO 2: Múltiples Preguntas")
    print("=" * 60)
    
    agent = ResearchAgent()
    
    preguntas = [
        "¿Qué es Python?",
        "¿Qué es machine learning?",
        "¿Qué es blockchain?"
    ]
    
    for i, pregunta in enumerate(preguntas, 1):
        print(f"\n[{i}/{len(preguntas)}] ❓ {pregunta}")
        respuesta = agent.research(pregunta)
        print(f"💬 {respuesta[:200]}...")  # Primeros 200 caracteres
        
        if i < len(preguntas):
            input("\nPresiona Enter para la siguiente pregunta...")


def ejemplo_chat():
    """Ejemplo de chat simple (sin búsqueda web)"""
    print("\n" + "=" * 60)
    print("EJEMPLO 3: Chat Simple")
    print("=" * 60)
    
    agent = ResearchAgent()
    
    mensajes = [
        "Hola, ¿cómo estás?",
        "Cuéntame un chiste corto",
        "Dame un consejo de programación"
    ]
    
    for mensaje in mensajes:
        print(f"\n👤 Usuario: {mensaje}")
        respuesta = agent.chat(mensaje)
        print(f"🤖 Agente: {respuesta}\n")


def ejemplo_personalizado():
    """Ejemplo con modelo personalizado"""
    print("\n" + "=" * 60)
    print("EJEMPLO 4: Modelo Personalizado")
    print("=" * 60)
    print("\n(Solo funciona si tienes otros modelos instalados)")
    
    try:
        # Puedes usar otros modelos si los tienes instalados
        # Por ejemplo: llama3.2:1b (más pequeño y rápido)
        agent = ResearchAgent(model="llama3.2")
        
        pregunta = "Explica en una frase qué es Python"
        print(f"\n❓ {pregunta}")
        
        respuesta = agent.chat(pregunta)
        print(f"💬 {respuesta}\n")
        
    except Exception as e:
        print(f"⚠️  {e}")


def main():
    """Ejecuta todos los ejemplos"""
    print("\n🤖 EJEMPLOS DEL AGENTE DE INVESTIGACIÓN\n")
    
    try:
        # Ejecutar ejemplos
        ejemplo_basico()
        
        respuesta = input("\n¿Quieres ver más ejemplos? (s/n): ")
        if respuesta.lower() == 's':
            ejemplo_multiple()
            ejemplo_chat()
            ejemplo_personalizado()
        
        print("\n✅ Ejemplos completados!")
        print("\n💡 Ahora puedes:")
        print("   1. Usar run_agent.py desde la terminal")
        print("   2. Importar ResearchAgent en tu código")
        print("   3. Modificar estos ejemplos para tus necesidades\n")
        
    except KeyboardInterrupt:
        print("\n\n👋 ¡Hasta luego!")
    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()
