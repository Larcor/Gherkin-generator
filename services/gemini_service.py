import google.generativeai as genai
from typing import Optional


class GeminiServiceError(Exception):    
    def __init__(self, message: str, original_error: Optional[Exception] = None):
        super().__init__(message)
        self.original_error = original_error


class GeminiService:
    #Gemini
    def __init__(self, api_key: str, model_name: str = "gemini-2.5-flash"):
        self.api_key = api_key
        self.model_name = model_name
        self._model: Optional[genai.GenerativeModel] = None
        
        if self.is_configured():
            genai.configure(api_key=self.api_key)
    
    def is_configured(self) -> bool:
        #verifica api key
        return bool(self.api_key and self.api_key != "")
    
    def _get_model(self) -> genai.GenerativeModel:
        
        if not self.is_configured():
            raise GeminiServiceError("El servicio Gemini no está configurado con una API key")
        
        if self._model is None:
            self._model = genai.GenerativeModel(self.model_name)
        
        return self._model
    
    def generate_gherkin_scenarios(self, user_story: str, prompt_template: str) -> str:
        #genera escenarios gherkin
        try:
            model = self._get_model()
            full_prompt = prompt_template.format(user_story=user_story)
            response = model.generate_content(full_prompt)
            
            if not response or not response.text:
                raise GeminiServiceError("Respuesta vacía de la API de Gemini")
            
            return response.text
            
        except GeminiServiceError:
            raise
        except Exception as e:
            raise GeminiServiceError(
                f"Error al comunicarse con Gemini: {str(e)}",
                original_error=e
            )
