# 🏨 Sistema de Reputación Turística - Metodologías Ágiles

Este proyecto consiste en una plataforma automatizada para una cadena hotelera que recopila reseñas y utiliza un clasificador basado en reglas de negocio para categorizar los sentimientos en español (Positiva, Negativa, Neutral). 

El desarrollo se ha realizado aplicando de forma simultánea un marco integrado de **Scrum**, **Kanban** y **Extreme Programming (XP)**.

---

## 🛠️ Aplicación del Marco Ágil

### 1. Gestión del Trabajo (Scrum)
* **Roles:** Ante la restricción de tiempo y coordinación, se aplicó una adaptación de "Solo Scrum", donde un único ingeniero asumió de forma integral las responsabilidades de Product Owner (priorización), Scrum Master (remoción de impedimentos) y Developer (ejecución).
* **Product Backlog:** Configurado con 6 Historias de Usuario priorizadas y estimadas en puntos de historia para asegurar una entrega de valor incremental.

### 2. Gestión del Flujo (Kanban)
* Se implementó un tablero visual con las columnas: `Backlog`, `En curso`, `En revisión` y `Hecho`.
* Se respetó estrictamente un límite **WIP = 2** (Work In Progress) en las columnas intermedias para evitar cuellos de botella, optimizar el flujo de trabajo y mantener el foco.

### 3. Calidad Técnica (XP)
* **TDD (Test-Driven Development):** El diseño del código se guio a través de la creación previa de pruebas unitarias automatizadas que validan los criterios de aceptación antes de procesar el archivo real.
* **Limpieza de Código:** Se implementaron funciones modulares con expresiones regulares para la normalización y limpieza del texto (remoción de signos y conversión a minúsculas).

---

## 📋 Definition of Done (DoD)

Para que una Historia de Usuario se considere formalmente completada ("Hecho"), debe cumplir con los siguientes criterios de calidad exigidos en el taller:

| Requisito | ¿Cumple? | Evidencia |
| :--- | :---: | :--- |
| Código revisado (Pair/Self Review) | **[ X ]** | Código auto-revisado minuciosamente bajo estándares limpios. |
| Al menos una prueba unitaria pasa correctamente | **[ X ]** | 4 pruebas unitarias automatizadas ejecutadas con éxito. |
| Documentación mínima actualizada | **[ X ]** | Archivo README.md completo con instrucciones de uso. |
| El código ejecuta sin errores | **[ X ]** | Script verificado en entorno de ejecución local. |

---

## 🚀 Instrucciones de Ejecución

El script está desarrollado en **Python 3** y no requiere de la instalación de librerías externas (utiliza la librería nativa `re`).

### Requisitos Previos
1. Tener instalado Python 3.x en el sistema.
2. Asegurar que los archivos `clasificador.py` y `resenas.txt` se encuentren en la misma carpeta.

### Comando para ejecutar el programa e iniciar las pruebas:
Abre la terminal o consola de comandos en la ruta del proyecto y ejecuta:

```bash
python clasificador.py
