import os
from dataclasses import dataclass
from typing import Optional
from dotenv import load_dotenv


@dataclass
class AppSettings:
    google_api_key: str
    model_name: str = "gemini-2.5-flash"
    page_title: str = "Text-to-Gherkin Generator"
    page_icon: str = "🤖"
    
    def is_valid(self) -> bool:
        return bool(self.google_api_key and self.google_api_key != "")


class ConfigurationManager:
    
    def __init__(self, env_file: str = ".env"):
        self.env_file = env_file
        self._settings: Optional[AppSettings] = None
    
    def load(self) -> AppSettings:
        load_dotenv(self.env_file)
        api_key = os.getenv("GOOGLE_API_KEY", "")
        
        self._settings = AppSettings(google_api_key=api_key)
        return self._settings
    
    @property
    def settings(self) -> AppSettings:
        if self._settings is None:
            return self.load()
        return self._settings
    
    def validate(self) -> tuple[bool, Optional[str]]:
        if self._settings is None:
            self.load()
        
        if not self._settings.google_api_key:
            return False, "GOOGLE_API_KEY no está configurada. Revisa tu archivo .env"
        
        if self._settings.google_api_key == "GOOGLE_KEY":
            return False, "Por favor reemplaza 'GOOGLE_KEY' con tu API Key real en el archivo .env"
        
        return True, None
