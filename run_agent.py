"""
Script para usar el agente desde la línea de comandos

Uso:
    python run_agent.py "Tu pregunta aquí"

Ejemplo:
    python run_agent.py "¿Qué es machine learning?"
"""
import sys
from agent import ResearchAgent


def main():
    # Verificar que se pasó una pregunta
    if len(sys.argv) < 2:
        print("❌ Error: Debes proporcionar una pregunta")
        print("\nUso:")
        print('   python run_agent.py "Tu pregunta aquí"')
        print("\nEjemplo:")
        print('   python run_agent.py "¿Qué es Python?"')
        sys.exit(1)
    
    # Obtener la pregunta (juntar todos los argumentos)
    question = " ".join(sys.argv[1:])
    
    print("=" * 60)
    print("🤖 AGENTE DE INVESTIGACIÓN")
    print("=" * 60)
    print(f"\n❓ Pregunta: {question}\n")
    
    try:
        # Crear el agente
        agent = ResearchAgent()
        
        # Hacer la investigación
        respuesta = agent.research(question)
        
        # Mostrar resultado
        print("\n" + "=" * 60)
        print("📝 RESPUESTA")
        print("=" * 60)
        print(f"\n{respuesta}\n")
        print("=" * 60)
        
    except RuntimeError as e:
        print(f"\n❌ {e}")
        print("\n💡 Ejecuta primero:")
        print("   python test_agent.py")
        print("\nPara verificar la instalación.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
