from config.settings import ConfigurationManager
from services.gemini_service import GeminiService, GeminiServiceError
from prompts.prompt_builder import PromptBuilder
from ui.components import UIComponents, ValidationMessages


def main():    
    config_manager = ConfigurationManager()
    settings = config_manager.settings
    
    UIComponents.configure_page(settings)
    
    is_valid, error_message = config_manager.validate()
    if not is_valid:
        UIComponents.show_error(error_message)
    
    ai_service = GeminiService(
        api_key=settings.google_api_key,
        model_name=settings.model_name
    )
    
    prompt_template = PromptBuilder().for_gherkin_generation().build()
    
    UIComponents.render_header()
    user_story = UIComponents.render_user_story_input()
    
    if UIComponents.render_generate_button():
        if not user_story:
            UIComponents.show_warning(ValidationMessages.EMPTY_USER_STORY)
            return
        
        if not is_valid:
            UIComponents.show_error(ValidationMessages.API_KEY_MISSING)
            return
        
        try:
            with UIComponents.show_spinner(ValidationMessages.LOADING_MESSAGE):
                gherkin_scenarios = ai_service.generate_gherkin_scenarios(
                    user_story=user_story,
                    prompt_template=prompt_template
                )
                UIComponents.render_result(gherkin_scenarios)
                
        except GeminiServiceError as e:
            error_msg = ValidationMessages.GENERATION_ERROR.format(error=str(e))
            UIComponents.show_error(error_msg)
        except Exception as e:
            error_msg = ValidationMessages.GENERATION_ERROR.format(error=str(e))
            UIComponents.show_error(error_msg)
    
    UIComponents.render_footer()


if __name__ == "__main__":
    main()