import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. Configuración inicial
load_dotenv() # Carga la API Key del archivo .env

# Configurar la API de Gemini
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("No se encontró la API Key. Asegúrate de crear el archivo .env")

# 2. Configuración de la Interfaz (Streamlit)
st.set_page_config(page_title="Text-to-Gherkin Generator", page_icon="🤖")

st.title("🤖 Generador de Casos de Prueba (Text-to-Gherkin)")
st.markdown("""
    Pega tu **Historia de Usuario** abajo y la IA generará los escenarios 
    de prueba en formato **Gherkin** listos para automatizar.
""")

# 3. Área de entrada del usuario
user_story = st.text_area(
    "Historia de Usuario:",
    placeholder="Ej: Como usuario registrado, quiero recuperar mi contraseña mediante email para volver a acceder a mi cuenta...",
    height=150
)

# 4. Lógica del Botón y el Prompt
if st.button("Generar Escenarios Gherkin ✨"):
    if not user_story:
        st.warning("Por favor, ingresa una historia de usuario primero.")
    elif not api_key:
        st.error("Falta configurar la API Key.")
    else:
        with st.spinner("Un QA Senior está analizando tu historia..."):
            try:
                model = genai.GenerativeModel('gemini-2.5-flash') # Modelo de gemini
                
                # PROMPT
                system_prompt = f"""
                Actúa como un Lead QA Automation Engineer experto en metodologías BDD.

                Tu tarea es convertir la siguiente Historia de Usuario o Caso de Prueba manual en escenarios Gherkin de alta calidad.

                OBJETIVO:
                Generar archivos .feature que sirvan como documentación viva del negocio, legibles por stakeholders no técnicos.

                REGLAS ESTRICTAS DE ESTILO (CRÍTICO):
                1.  **Estilo Declarativo:** Describe QUÉ hace el usuario, no CÓMO lo hace.
                    * PROHIBIDO: "Hacer clic en el botón X", "Escribir 'admin' en el campo #user".
                    * PERMITIDO: "Cuando el usuario envía sus credenciales", "Cuando confirma la transacción".
                2.  **Tercera Persona:** Escribe siempre como "El usuario" o "El cliente", nunca como "Yo".
                3.  **Atomicidad:** Cada escenario debe ser independiente.
                4.  **Reutilización:** Si hay precondiciones repetidas, extráelas a un bloque `Background`.
                5.  **Data Driven:** Si hay múltiples variaciones de datos (ej: varios casos de error), DEBES usar `Scenario Outline` con una tabla de `Examples` en lugar de repetir escenarios.

                REQUERIMIENTOS DE SALIDA:
                1.  Genera 1 `Scenario` para el Happy Path.
                2.  Genera escenarios negativos o bordes (usa `Scenario Outline` si aplica).
                3.  Usa palabras clave en Inglés (Given/When/Then) pero el contenido en Español (o el idioma del input).
                4.  No incluyas explicaciones, solo el bloque de código Gherkin.

                Historia de Usuario:
                "{user_story}"
                """
                
                response = model.generate_content(system_prompt)
                
                # 5. Mostrar resultado
                st.subheader("📝 Escenarios Generados:")
                st.code(response.text, language="gherkin")
                
                st.success("¡Generación completada!")
                
            except Exception as e:
                st.error(f"Ocurrió un error al conectar con Gemini: {e}")

# Footer
st.markdown("---")
st.caption("Herramienta creada con Python, Streamlit y Gemini API.")