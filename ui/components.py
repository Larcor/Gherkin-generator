import streamlit as st
from config.settings import AppSettings


class UIComponents:
    
    @staticmethod
    def configure_page(settings: AppSettings) -> None:
        st.set_page_config(
            page_title=settings.page_title,
            page_icon=settings.page_icon
        )
    
    @staticmethod
    def render_header() -> None:
        #encabezado
        st.title("🤖 Generador de Casos de Prueba (Text-to-Gherkin)")
        st.markdown("""
            Pega tu **Historia de Usuario** abajo y la IA generará los escenarios 
            de prueba en formato **Gherkin** listos para automatizar.
        """)
    
    @staticmethod
    def render_user_story_input() -> str:
        """Renderiza el área de texto para la historia de usuario."""
        return st.text_area(
            "Historia de Usuario:",
            placeholder="Ej: Como usuario registrado, quiero recuperar mi contraseña mediante email para volver a acceder a mi cuenta...",
            height=150
        )
    
    @staticmethod
    def render_generate_button() -> bool:
        #Boton generar
        return st.button("Generar Escenarios Gherkin ✨")
    
    @staticmethod
    def render_result(gherkin_scenarios: str) -> None:
        #Gherkin generado
        st.subheader("📝 Escenarios Generados:")
        st.code(gherkin_scenarios, language="gherkin")
        st.success("¡Generación completada!")
    
    @staticmethod
    def render_footer() -> None:
        #Footer
        st.markdown("---")
        st.caption("...")
    
    @staticmethod
    def show_error(message: str) -> None:
        #Error
        st.error(message)
    
    @staticmethod
    def show_warning(message: str) -> None:
        #Advertencia
        st.warning(message)
    
    @staticmethod
    def show_spinner(message: str):
        #Spinner
        return st.spinner(message)


class ValidationMessages:
    #Mensajes de validación y error
    
    EMPTY_USER_STORY = "Por favor, ingresa una historia de usuario primero."
    LOADING_MESSAGE = "Se esta analizando la historia"
    API_KEY_MISSING = "No se encontró la API Key."
    GENERATION_ERROR = "Ocurrió un error al generar los escenarios: {error}"
