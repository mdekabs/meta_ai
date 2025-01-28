from app.utils.logger import logger

# Set of keywords to identify if the query is medical-related
MEDICAL_KEYWORDS = {
    "health", "medicine", "symptom", "disease", "treatment",
    "doctor", "nurse", "diagnosis", "prescription", "therapy"
}

class MedicalAssistantService:
    """
    Service class to handle medical assistance queries.

    This class interacts with an AI model to generate responses for 
    medical-related queries based on predefined keywords.
    """

    def __init__(self, ai_model):
        """
        Initialize the MedicalAssistantService with an AI model.

        Args:
            ai_model: An instance of the AI model used for generating responses.
        """
        self.ai_model = ai_model

    def generate_response(self, message):
        """
        Generate a response based on the user's message.

        This method checks if the message contains medical keywords before 
        forwarding it to the AI model for a response.

        Args:
            message (str): The user's query or message.

        Returns:
            str: Either a response from the AI model or a message indicating 
                 the service is for medical queries only.
        """
        # Check if the message contains any medical keyword
        if not any(keyword in message.lower() for keyword in MEDICAL_KEYWORDS):
            keywords_str = ", ".join(MEDICAL_KEYWORDS)
            return f"This service is for medical-related questions only. Your message must contain at least one of these keywords: {keywords_str}."

        # Log the type and content of the message for debugging
        logger.debug(f"Message type: {type(message)}, Message content: {message}")
        
        try:
            # Attempt to generate a response using the AI model
            return self.ai_model.prompt(message)
        except Exception as e:
            # Log any errors that occur during response generation
            logger.error(f"Error generating response: {e}")
            return "An unexpected error occurred."
