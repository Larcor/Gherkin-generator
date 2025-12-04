# 🤖 Generador de Casos de Prueba (Text-to-Gherkin)

Una herramienta inteligente que convierte Historias de Usuario en escenarios de prueba en formato **Gherkin** automáticamente, utilizando la IA de **Google Gemini**.

## 📋 Descripción

Este proyecto utiliza **Streamlit** para proporcionar una interfaz web interactiva donde puedes pegar una Historia de Usuario y obtener inmediatamente escenarios de prueba en formato Gherkin, listos para ser utilizados en frameworks de automatización como **Cucumber**, **Behave** o **Karate**.

### ✨ Características

- **Generación automática de escenarios Gherkin** a partir de Historias de Usuario
- **Happy Paths y casos negativos** generados automáticamente
- **Estilo declarativo BDD** (describe QUÉ hace el usuario, no CÓMO)
- **Data-driven**: utiliza `Scenario Outline` para casos con múltiples variaciones
- **Interfaz web** intuitiva y fácil de usar
- **Google Gemini AI** (modelo gemini-2.5-flash)

## 🛠️ Tecnologías Utilizadas

- **Python 3.11**
- **Streamlit** - Framework para crear la interfaz web
- **Google Generative AI (Gemini)** - IA para generación de escenarios
- **python-dotenv** - Manejo de variables de entorno

## 📦 Requisitos Previos

- Python 3.11
- Una API Key de Google AI Studio ([Obtener aquí](https://aistudio.google.com/app/apikey))

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Larcor/Gherkin-generator.git
```

### 2. Crear un entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la API Key

1. Copia el archivo de ejemplo:
   ```bash
   copy .env.example .env
   ```

2. Edita el archivo `.env` y reemplaza `GOOGLE_KEY` con tu API Key real de Google AI Studio:
   ```
   GOOGLE_API_KEY=tu_api_key_aqui
   ```

## 🏗️ Arquitectura y Patrones de Diseño

Este proyecto ha sido refactorizado aplicando principios **SOLID** y patrones de diseño profesionales para garantizar mantenibilidad, escalabilidad y testabilidad.

### Principios SOLID Aplicados

| Principio | Implementación |
|-----------|----------------|
| **Single Responsibility** | Cada módulo tiene una única responsabilidad: `ConfigurationManager` maneja configuración, `GeminiService` maneja la API, etc. |
| **Open/Closed** | Abierto a extensión: puedes agregar nuevos servicios de IA (`OpenAIService`, `ClaudeService`) sin modificar código existente |
| **Liskov Substitution** | Cualquier implementación de `AIService` puede sustituir a otra sin romper el código |
| **Interface Segregation** | Interfaces pequeñas y específicas (`AIService` solo define lo necesario) |
| **Dependency Inversion** | El código depende de abstracciones (`AIService`), no de implementaciones concretas |

### Patrones de Diseño

- **Strategy Pattern**: `AIService` define la interfaz, `GeminiService` es una estrategia concreta
- **Dependency Injection**: `app.py` inyecta dependencias a los componentes
- **Builder Pattern**: `PromptBuilder` construye prompts complejos de manera fluida
- **Separation of Concerns**: Capas separadas (config, services, ui, prompts)

### Estructura Modular

```
generador-gherkin/
├── app.py                          # Composition Root (orquestación)
├── requirements.txt                # Gestión de dependencias
├── .env / .env.example             # Configuración
├── config/
│   ├── __init__.py
│   └── settings.py                 # ConfigurationManager (SRP)
├── services/
│   ├── __init__.py
│   ├── ai_service.py               # Interfaz abstracta AIService (DIP)
│   └── gemini_service.py           # Implementación Gemini (LSP)
├── prompts/
│   ├── __init__.py
│   └── prompt_builder.py           # Constructor de prompts (Builder Pattern)
└── ui/
    ├── __init__.py
    └── components.py               # Componentes de UI reutilizables (SRP)
```

### Beneficios de esta Arquitectura

✅ **Mantenibilidad**: Código organizado y fácil de entender  
✅ **Testabilidad**: Componentes aislados que pueden probarse independientemente  
✅ **Escalabilidad**: Fácil agregar nuevos proveedores de IA o features  
✅ **Reutilización**: Componentes modulares y reutilizables  
✅ **Profesionalismo**: Sigue las mejores prácticas de la industria  


## ▶️ Ejecución

Para ejecutar la aplicación:

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

## 📖 Uso

1. **Abre la aplicación** en tu navegador
2. **Pega tu Historia de Usuario** en el área de texto
   - Ejemplo: *"Como usuario registrado, quiero recuperar mi contraseña mediante email para volver a acceder a mi cuenta"*
3. **Haz clic en "Generar Escenarios Gherkin ✨"**
4. **Copia los escenarios generados** y úsalos en tu proyecto de automatización

### Ejemplo de Salida

La herramienta genera escenarios Gherkin como:

```gherkin
Feature: Recuperación de contraseña

  Scenario: Usuario recupera contraseña exitosamente
    Given el usuario está en la página de login
    When el usuario solicita recuperar su contraseña
    And ingresa su email registrado
    Then el sistema envía un email con instrucciones de recuperación
    And el usuario recibe confirmación de envío
```

## 📁 Estructura del Proyecto

```
generador-gherkin/
├── app.py              # Aplicación principal de Streamlit
├── .env                # Variables de entorno (no versionado)
├── .env.example        # Plantilla de variables de entorno
├── .gitignore          # Archivos a ignorar en Git
├── README.md           # Este archivo
└── venv/               # Entorno virtual (no versionado)
```

## 🔒 Seguridad

- **Nunca compartas tu API Key** públicamente
- El archivo `.env` está excluido del control de versiones mediante `.gitignore`
- Usa el archivo `.env.example` como plantilla (sin datos sensibles)

## 📝 Notas

- El modelo utilizado es **gemini-2.5-flash** de Google
- Los escenarios se generan en **español** pero usando palabras clave de Gherkin en **inglés** (Given/When/Then)
- La herramienta sigue las mejores prácticas de **BDD (Behavior-Driven Development)**
