"""
Búsqueda web gratuita usando DuckDuckGo
No requiere API key
"""
from ddgs import DDGS


def search_web(query, max_results=3):
    """
    Busca en internet usando DuckDuckGo (gratis, sin API key)
    
    Args:
        query: Lo que quieres buscar
        max_results: Cuántos resultados quieres (default: 3)
    
    Returns:
        String con los resultados formateados
    """
    try:
        ddgs = DDGS()
        results = list(ddgs.text(query, max_results=max_results))
        
        if not results:
            return "No se encontraron resultados."
        
        # Formatear resultados
        output = f"\n🔍 Resultados de búsqueda para: '{query}'\n"
        output += "=" * 60 + "\n\n"
        
        for i, result in enumerate(results, 1):
            output += f"{i}. {result['title']}\n"
            output += f"   {result['body'][:200]}...\n"
            output += f"   🔗 {result['href']}\n\n"
        
        return output
        
    except Exception as e:
        return f"Error en la búsqueda: {str(e)}"


# Prueba rápida
if __name__ == "__main__":
    print("Probando búsqueda web gratuita...")
    resultado = search_web("Python programming", max_results=2)
    print(resultado)
