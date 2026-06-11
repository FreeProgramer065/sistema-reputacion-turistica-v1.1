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
    """HU03 y HU06: Clasifica una reseña basada en palabras clave."""
    texto_procesado = limpiar_texto(texto)
    
    if not texto_procesado:
        return "Vacio"

    # Vocabulario extendido de palabras clave
    positivas = ["bueno", "excelente", "genial", "limpio", "amable", "perfecto", "comoda", "bonita", "hermosa", "aceptable"]
    negativas = ["malo", "sucio", "tarde", "roto", "feo", "horrible", "pesima", "ruido", "desastre", "caro", "peor", "mal"]
    
    # Contar coincidencias
    conteo_pos = sum(1 for p in positivas if p in texto_procesado)
    conteo_neg = sum(1 for n in negativas if n in texto_procesado)
    
    if conteo_pos > conteo_neg:
        return "Positiva"
    elif conteo_neg > conteo_pos:
        return "Negativa"
    else:
        return "Neutral" # Si empata o no encuentra palabras clave

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
# PRUEBAS UNITARIAS (Requisito XP - TDD)
# =====================================================================
def ejecutar_pruebas_tdd():
    """HU04: Pruebas automatizadas para validar el comportamiento del sistema."""
    print("🧪 Ejecutando pruebas unitarias (TDD)...")
    
    # Prueba 1: Verificar clasificacion positiva
    assert clasificar_sentimiento("Excelente servicio y habitacion muy limpia") == "Positiva"
    
    # Prueba 2: Verificar clasificacion negativa
    assert clasificar_sentimiento("El cuarto estaba sucio y la atencion fue pesima") == "Negativa"
    
    # Prueba 3: Verificar manejo de textos neutrales (HU06)
    assert clasificar_sentimiento("El desayuno estuvo regular") == "Neutral"
    
    # Prueba 4: Verificar limpieza de texto (HU02)
    assert limpiar_texto("¡HOLA, Mundo!!!") == "hola mundo"
    
    print("✅ Todas las pruebas unitarias pasaron exitosamente.\n")

if __name__ == "__main__":
    # 1. Ejecutar primero las pruebas (Enfoque XP)
    ejecutar_pruebas_tdd()
    
    # 2. Procesar el archivo de reseñas real
    archivo = "resenas.txt"
    print(# Reporte por pantalla
    f"📊 PROCESANDO ARCHIVO: {archivo}")
    print("-" * 50)
    
    lineas_procesadas, reporte_estadistico = procesar_archivo(archivo)
    
    for resena, sent in lineas_procesadas:
        print(# Muestra cada reseña clasificada
        f"[{sent}] -> {resena}")
        
    print("-" * 50)
    print("📈 REPORTE ESTADÍSTICO FINAL:")
    print(f" Total Reseñas Positivas: {reporte_estadistico['Positiva']}")
    print(f" Total Reseñas Negativas: {reporte_estadistico['Negativa']}")
    print(f" Total Reseñas Neutrales: {reporte_estadistico['Neutral']}")
    print(f" Líneas vacías ignoradas: {reporte_estadistico['Vacio']}")
    print("-" * 50)
