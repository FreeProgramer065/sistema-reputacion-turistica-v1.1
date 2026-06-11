# clasificador.py
import re

def limpiar_texto(texto):
    """HU02: Limpia el texto eliminando signos de puntuacion y pasandolo a minusculas."""
    if not texto:
        return ""
    # Remover caracteres especiales y pasar a minusculas
    texto_limpio = re.sub(r'[^\w\s]', '', texto.lower())
    return texto_limpio.strip()

def clasificar_sentimiento(texto):
    """HU03 y HU06: Clasifica una reseña basada en palabras clave exactas (Refactorizado)."""
    texto_procesado = limpiar_texto(texto)
    
    if not texto_procesado:
        return "Vacio"

    # XP Refactor: Separamos el texto en palabras exactas para evitar falsos positivos (ej: 'mal' en 'normal')
    palabras_usuario = texto_procesado.split()

    # Vocabulario extendido incluyendo variaciones de genero y numero (Mejora de Calidad Técnica)
    positivas = [
        "bueno", "buena", "buenos", "buenas", "excelente", "excelentes", "genial", "geniales", 
        "limpio", "limpia", "limpios", "limpias", "amable", "amables", "perfecto", "perfecta", 
        "comoda", "comodo", "bonita", "bonito", "hermosa", "hermoso", "aceptable", "gigante"
    ]
    negativas = [
        "malo", "mala", "malos", "malas", "sucio", "sucia", "sucios", "sucias", "tarde", 
        "roto", "rota", "rotos", "rotas", "feo", "fea", "horrible", "horribles", "pesima", 
        "pesimo", "ruido", "desastre", "caro", "cara", "peor", "mal", "lento", "lenta"
    ]
    
    # Contar coincidencias por palabra exacta
    conteo_pos = sum(1 for p in palabras_usuario if p in positivas)
    conteo_neg = sum(1 for p in palabras_usuario if p in negativas)
    
    if conteo_pos > conteo_neg:
        return "Positiva"
    elif conteo_neg > conteo_pos:
        return "Negativa"
    else:
        return "Neutral"

def procesar_archivo(archivo_ruta):
    """HU01 y HU05: Procesa el archivo TXT y genera el reporte estadistico."""
    totales = {"Positiva": 0, "Negativa": 0, "Neutral": 0, "Vacio": 0}
    resultados = []
    
    with open(archivo_ruta, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        
    for linea in lineas:
        sentimiento = clasificar_sentimiento(linea)
        totales[sentimiento] += 1
        if sentimiento != "Vacio":
            resultados.append((linea.strip(), sentimiento))
            
    return resultados, totales

# =====================================================================
# PRUEBAS UNITARIAS ACTUALIZADAS (XP - TDD)
# =====================================================================
def ejecutar_pruebas_tdd():
    """HU04: Pruebas automatizadas para validar el comportamiento del sistema."""
    print("🧪 Ejecutando pruebas unitarias (TDD)...")
    
    # Prueba 1: Verificar clasificacion positiva
    assert clasificar_sentimiento("Excelente servicio y habitacion muy limpia") == "Positiva"
    
    # Prueba 2: Verificar clasificacion negativa con flexión de número (las sábanas rotas)
    assert clasificar_sentimiento("Las sabanas estaban rotas") == "Negativa"
    
    # Prueba 3: Verificar que 'normal' NO se confunda con 'mal' (Asegurar precisión)
    assert clasificar_sentimiento("Un hotel normal") == "Neutral"
    
    # Prueba 4: Verificar limpieza de texto
    assert limpiar_texto("¡HOLA, Mundo!!!") == "hola mundo"
    
    print("✅ Todas las pruebas unitarias pasaron exitosamente.\n")

if __name__ == "__main__":
    ejecutar_pruebas_tdd()
    
    archivo = "resenas.txt"
    print(f"📊 PROCESANDO ARCHIVO REFACTORIZADO: {archivo}")
    print("-" * 50)
    
    lineas_procesadas, reporte_estadistico = procesar_archivo(archivo)
    
    for resena, sent in lineas_procesadas:
        print(f"[{sent}] -> {resena}")
        
    print("-" * 50)
    print("📈 REPORTE ESTADÍSTICO FINAL:")
    print(f" Total Reseñas Positivas: {reporte_estadistico['Positiva']}")
    print(f" Total Reseñas Negativas: {reporte_estadistico['Negativa']}")
    print(f" Total Reseñas Neutrales: {reporte_estadistico['Neutral']}")
    print(f" Líneas vacías ignoradas: {reporte_estadistico['Vacio']}")
    print("-" * 50)
