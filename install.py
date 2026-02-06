#!/usr/bin/env python3
"""
Script de instalación automática para el agente de investigación

Ejecuta: python install.py
"""
import subprocess
import sys
import os


def print_step(step, message):
    """Imprime un paso con formato"""
    print(f"\n{'='*60}")
    print(f"[PASO {step}] {message}")
    print('='*60)


def check_python_version():
    """Verifica la versión de Python"""
    print_step(1, "Verificando Python")
    
    version = sys.version_info
    print(f"Python {version.major}.{version.minor}.{version.micro} detectado")
    
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print("❌ Se requiere Python 3.9 o superior")
        print(f"   Tienes: Python {version.major}.{version.minor}")
        return False
    
    print("✅ Versión de Python compatible")
    return True


def install_dependencies():
    """Instala las dependencias de Python"""
    print_step(2, "Instalando dependencias de Python")
    
    try:
        print("Instalando paquetes...")
        
        # Actualizar pip primero
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
            check=True,
            capture_output=True
        )
        
        # Instalar dependencias una por una para mejor feedback
        packages = [
            "typing-extensions>=4.5.0",
            "click>=8.1.0",
            "ddgs>=0.1.0"
        ]
        
        for package in packages:
            print(f"  Instalando {package.split('>=')[0]}...")
            subprocess.run(
                [sys.executable, "-m", "pip", "install", package],
                check=True,
                capture_output=True
            )
        
        print("\n✅ Todas las dependencias instaladas correctamente")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al instalar dependencias: {e}")
        print("\nIntenta instalar manualmente:")
        print("  pip install typing-extensions click primp duckduckgo-search")
        return False


def check_ollama():
    """Verifica si Ollama está instalado"""
    print_step(3, "Verificando Ollama")
    
    try:
        result = subprocess.run(
            ["ollama", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            print(f"✅ Ollama instalado: {result.stdout.strip()}")
            return True
        else:
            print("❌ Ollama no responde correctamente")
            return False
            
    except FileNotFoundError:
        print("❌ Ollama no está instalado")
        print("\n📥 Instala Ollama:")
        print("   1. Ve a: https://ollama.com/download")
        print("   2. Descarga e instala para macOS")
        print("   3. Ejecuta este script de nuevo")
        return False
    except Exception as e:
        print(f"❌ Error al verificar Ollama: {e}")
        return False


def install_model():
    """Instala el modelo de Ollama"""
    print_step(4, "Instalando modelo de AI")
    
    # Verificar si ya está instalado
    try:
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if "llama3.2" in result.stdout:
            print("✅ Modelo llama3.2 ya está instalado")
            return True
            
    except Exception:
        pass
    
    # Instalar el modelo
    print("\n📦 Descargando modelo llama3.2...")
    print("   (Esto puede tardar varios minutos, ~2.7GB)")
    print("   Por favor espera...\n")
    
    try:
        process = subprocess.Popen(
            ["ollama", "pull", "llama3.2"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        
        # Mostrar progreso
        for line in process.stdout:
            print(f"   {line.strip()}")
        
        process.wait()
        
        if process.returncode == 0:
            print("\n✅ Modelo instalado correctamente")
            return True
        else:
            print("\n❌ Error al instalar el modelo")
            return False
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nIntenta instalar manualmente:")
        print("  ollama pull llama3.2")
        return False


def run_tests():
    """Ejecuta las pruebas finales"""
    print_step(5, "Ejecutando pruebas")
    
    try:
        result = subprocess.run(
            [sys.executable, "test_agent.py"],
            capture_output=False,  # Mostrar output directamente
            timeout=60
        )
        
        return result.returncode == 0
        
    except Exception as e:
        print(f"❌ Error al ejecutar pruebas: {e}")
        return False


def print_success():
    """Muestra mensaje de éxito"""
    print("\n" + "="*60)
    print("🎉 ¡INSTALACIÓN COMPLETADA!")
    print("="*60)
    print("\n✅ Todo está listo para usar el agente")
    print("\n📝 Prueba el agente con:")
    print('   python run_agent.py "¿Qué es Python?"')
    print("\n📚 Ver más ejemplos:")
    print("   python examples/example.py")
    print("\n💡 Documentación completa en:")
    print("   README.md")
    print()


def print_failure():
    """Muestra mensaje de error"""
    print("\n" + "="*60)
    print("❌ INSTALACIÓN INCOMPLETA")
    print("="*60)
    print("\n⚠️  Algunos pasos fallaron.")
    print("\n🔧 Pasos de solución:")
    print("   1. Revisa los errores arriba")
    print("   2. Instala Ollama: https://ollama.com/download")
    print("   3. Instala dependencias: pip install -r requirements.txt")
    print("   4. Instala modelo: ollama pull llama3.2")
    print("   5. Ejecuta: python test_agent.py")
    print()


def main():
    """Función principal de instalación"""
    print("\n" + "="*60)
    print("🤖 INSTALACIÓN DEL AGENTE DE INVESTIGACIÓN")
    print("="*60)
    print("\nEste script instalará todo lo necesario.")
    print("Puede tardar varios minutos.\n")
    
    response = input("¿Continuar? (S/n): ")
    if response.lower() == 'n':
        print("\n❌ Instalación cancelada")
        return
    
    # Ejecutar pasos
    steps = [
        ("Python", check_python_version),
        ("Dependencias", install_dependencies),
        ("Ollama", check_ollama),
        ("Modelo AI", install_model),
    ]
    
    all_ok = True
    for name, func in steps:
        if not func():
            all_ok = False
            print(f"\n⚠️  Paso '{name}' falló")
            
            # Si Ollama no está instalado, detener aquí
            if name == "Ollama":
                print("\n❌ No se puede continuar sin Ollama")
                print_failure()
                return
    
    if all_ok:
        # Ejecutar pruebas finales
        if run_tests():
            print_success()
        else:
            print("\n⚠️  Las pruebas fallaron pero los componentes están instalados")
            print("   Intenta ejecutar: python test_agent.py")
    else:
        print_failure()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Instalación interrumpida por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error inesperado: {e}")
        sys.exit(1)
