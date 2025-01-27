from app.utils.logger import logger

MEDICAL_KEYWORDS = {
    "health", "medicine", "symptom", "disease", "treatment",
    "doctor", "nurse", "diagnosis", "prescription", "therapy"
}

class MedicalAssistantService:
    def __init__(self, ai_model):
        self.ai_model = ai_model
    
    def generate_response(self, message):
        if not any(keyword in message.lower() for keyword in MEDICAL_KEYWORDS):
            keywords_str = ", ".join(MEDICAL_KEYWORDS)
            return f"This service is for medical-related questions only. Your message must contain at least one of these keywords: {keywords_str}."
        logger.debug(f"Message type: {type(message)}, Message content: {message}")
        try:
            return self.ai_model.prompt(message)
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return "An unexpected error occurred."
