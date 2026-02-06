"""
Script de prueba para verificar que todo funciona
Ejecuta esto después de instalar: python test_agent.py
"""
import subprocess
import sys


def test_ollama():
    """Prueba que Ollama esté instalado"""
    print("🔍 Verificando Ollama...")
    try:
        result = subprocess.run(
            ["ollama", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            print("   ✅ Ollama instalado correctamente")
            return True
        else:
            print("   ❌ Ollama no responde")
            return False
    except FileNotFoundError:
        print("   ❌ Ollama no está instalado")
        print("   📥 Descárgalo de: https://ollama.com/download")
        return False


def test_model():
    """Prueba que haya al menos un modelo disponible"""
    print("\n🔍 Verificando modelos de Ollama...")
    try:
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        # Parsear modelos disponibles
        lines = result.stdout.strip().split('\n')
        if len(lines) > 1:  # Hay modelos (primera línea es header)
            models = [line.split()[0] for line in lines[1:]]
            print(f"   ✅ Modelos disponibles: {', '.join(models)}")
            return True
        else:
            print("   ❌ No hay modelos instalados")
            print("   📥 Instala uno con: ollama pull llama3.2")
            print("   O con: ollama pull gemma2:4b")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False


def test_dependencies():
    """Prueba que las dependencias Python estén instaladas"""
    print("\n🔍 Verificando dependencias Python...")
    
    try:
        from ddgs import DDGS
        print("   ✅ ddgs instalado")
    except ImportError:
        print("   ❌ ddgs no instalado")
        print("   📥 Instala con: pip install ddgs")
        return False
    
    return True


def test_search():
    """Prueba la búsqueda web"""
    print("\n🔍 Probando búsqueda web...")
    try:
        from search import search_web
        result = search_web("test", max_results=1)
        if result and "Error" not in result:
            print("   ✅ Búsqueda web funcionando")
            return True
        else:
            print("   ⚠️  Búsqueda web con problemas")
            return False
    except Exception as e:
        print(f"   ❌ Error en búsqueda: {e}")
        return False


def test_agent():
    """Prueba el agente completo"""
    print("\n🔍 Probando el agente completo...")
    try:
        from agent import ResearchAgent
        agent = ResearchAgent()
        print("   ✅ Agente inicializado correctamente")
        
        # Prueba simple
        print("\n   💭 Probando con una pregunta simple...")
        response = agent.chat("Di solo 'Hola'")
        if response:
            print(f"   ✅ Respuesta recibida: {response[:50]}...")
            return True
        else:
            print("   ❌ No se recibió respuesta")
            return False
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False


def main():
    """Ejecuta todas las pruebas"""
    print("=" * 60)
    print("🧪 PRUEBAS DEL AGENTE DE INVESTIGACIÓN")
    print("=" * 60)
    
    tests = [
        ("Ollama", test_ollama),
        ("Modelo", test_model),
        ("Dependencias", test_dependencies),
        ("Búsqueda Web", test_search),
        ("Agente", test_agent),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"   ❌ Error inesperado: {e}")
            results.append((name, False))
    
    # Resumen
    print("\n" + "=" * 60)
    print("📊 RESUMEN")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅" if result else "❌"
        print(f"{status} {name}")
    
    print("\n" + "=" * 60)
    
    if passed == total:
        print("🎉 ¡TODO FUNCIONA! Estás listo para usar el agente.")
        print("\nPrueba el agente con:")
        print('   python run_agent.py "¿Qué es la inteligencia artificial?"')
    else:
        print(f"⚠️  {total - passed} prueba(s) fallaron.")
        print("Por favor, revisa los mensajes de error arriba.")
        print("\nPasos para solucionar:")
        print("1. Instala Ollama: https://ollama.com/download")
        print("2. Instala el modelo: ollama pull llama3.2")
        print("3. Instala dependencias: pip install -r requirements.txt")
        sys.exit(1)


if __name__ == "__main__":
    main()
