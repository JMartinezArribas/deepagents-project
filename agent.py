"""
Agente de investigación simple y gratuito
Usa Ollama (local) + DuckDuckGo (búsqueda gratis)
"""
import subprocess
from search import search_web


class ResearchAgent:
    """Agente de investigación completamente gratuito"""
    
    def __init__(self, model=None):
        """
        Inicializa el agente
        
        Args:
            model: Modelo de Ollama a usar (default: None, auto-detecta)
        """
        # Si no se especifica modelo, detectar automáticamente
        if model is None:
            self.model = self._detect_model()
        else:
            self.model = model
        
        self._check_setup()
    
    def _detect_model(self):
        """Detecta automáticamente el primer modelo disponible"""
        try:
            result = subprocess.run(
                ["ollama", "list"],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            # Parsear la lista de modelos
            lines = result.stdout.strip().split('\n')
            if len(lines) > 1:  # Primera línea es el header
                # Tomar el primer modelo disponible
                first_model = lines[1].split()[0]
                print(f"ℹ️  Usando modelo: {first_model}")
                return first_model
            else:
                raise RuntimeError("No hay modelos instalados")
                
        except Exception as e:
            raise RuntimeError(
                f"❌ No se pudo detectar ningún modelo.\n"
                f"Error: {e}\n"
                f"Instala un modelo con: ollama pull gemma3:4b"
            )
    
    def _check_setup(self):
        """Verifica que todo esté instalado correctamente"""
        # Verificar Ollama
        try:
            result = subprocess.run(
                ["ollama", "list"],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            # Verificar que el modelo especificado existe
            if self.model not in result.stdout:
                # Listar modelos disponibles
                lines = result.stdout.strip().split('\n')
                available = [line.split()[0] for line in lines[1:]] if len(lines) > 1 else []
                
                raise RuntimeError(
                    f"❌ Modelo '{self.model}' no encontrado.\n"
                    f"Modelos disponibles: {', '.join(available) if available else 'ninguno'}\n"
                    f"Instala un modelo con: ollama pull gemma3:4b"
                )
        except FileNotFoundError:
            raise RuntimeError(
                "❌ Ollama no está instalado.\n"
                "Descárgalo de: https://ollama.com/download"
            )
    
    def _call_ollama(self, prompt):
        """
        Llama a Ollama con un prompt
        
        Args:
            prompt: El texto a enviar al modelo
            
        Returns:
            La respuesta del modelo
        """
        try:
            result = subprocess.run(
                ["ollama", "run", self.model, prompt],
                capture_output=True,
                text=True,
                timeout=60
            )
            return result.stdout.strip()
        except Exception as e:
            return f"Error al llamar a Ollama: {str(e)}"
    
    def research(self, question):
        """
        Investiga una pregunta usando búsqueda web + AI
        
        Args:
            question: La pregunta a investigar
            
        Returns:
            Respuesta completa del agente
        """
        print(f"\n🔍 Buscando información sobre: {question}")
        
        # Paso 1: Buscar en internet
        search_results = search_web(question, max_results=3)
        
        # Paso 2: Crear prompt para el modelo
        prompt = f"""Pregunta del usuario: {question}

Información encontrada en internet:
{search_results}

Instrucciones: 
- Usa la información de arriba para responder la pregunta
- Sé claro y conciso
- Si la información es limitada, dilo
- Responde en español

Respuesta:"""
        
        # Paso 3: Generar respuesta
        print("💭 Generando respuesta...")
        response = self._call_ollama(prompt)
        
        return response
    
    def chat(self, message):
        """
        Chat simple sin búsqueda web
        
        Args:
            message: El mensaje para el modelo
            
        Returns:
            Respuesta del modelo
        """
        print("💭 Procesando...")
        return self._call_ollama(message)


# Prueba rápida
if __name__ == "__main__":
    print("Inicializando agente...")
    agent = ResearchAgent()
    
    print("\n✅ Agente listo!")
    print("\nProbando con una pregunta:")
    
    respuesta = agent.research("¿Qué es Python?")
    print(f"\n📝 Respuesta:\n{respuesta}")
