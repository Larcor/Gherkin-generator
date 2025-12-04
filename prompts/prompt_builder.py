from typing import Optional


class PromptBuilder:
    #Constructor de prompts
    
    GHERKIN_GENERATION_TEMPLATE = """
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
    
    def __init__(self):
        self._template: Optional[str] = None
        self._custom_rules: list[str] = []
    
    def for_gherkin_generation(self) -> 'PromptBuilder':
        #Template gherkin
        self._template = self.GHERKIN_GENERATION_TEMPLATE
        return self
    
    def add_custom_rule(self, rule: str) -> 'PromptBuilder':
        
        self._custom_rules.append(rule)
        return self
    
    def build(self) -> str:
        #Contruye y retorna el prompt armado
        if self._template is None:
            raise ValueError("No se ha establecido un template. Llama a for_gherkin_generation() primero.")
        
        prompt = self._template
        
        if self._custom_rules:
            custom_rules_section = "\n\nREGLAS ADICIONALES:\n"
            custom_rules_section += "\n".join(f"- {rule}" for rule in self._custom_rules)
            prompt = prompt.replace('Historia de Usuario:', 
                                   f'{custom_rules_section}\n\nHistoria de Usuario:')
        
        return prompt
    
    @staticmethod
    def get_default_gherkin_template() -> str:
        return PromptBuilder.GHERKIN_GENERATION_TEMPLATE
