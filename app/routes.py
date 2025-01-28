from flask import jsonify, request, make_response
from app.services.medical_service import MedicalAssistantService
from app.utils.validators import validate_json_input
from app.utils.logger import logger

# Constants for better readability
INDEX_RESPONSE = "Medical Assistant AI is up and running!"
DISCLAIMER_MESSAGE = (
    "Please note: This AI is not a substitute for professional medical advice. "
    "Always consult with a healthcare provider for medical advice."
)
ERROR_RESPONSE = {'error': 'Internal server error'}
HTTP_INTERNAL_SERVER_ERROR = 500
REQUIRED_FIELDS = ['message']

# Initialize AI model and service
from meta_ai_api import MetaAI

ai_model = MetaAI()
medical_assistant_service = MedicalAssistantService(ai_model)


def initialize_routes(app):
    @app.route('/')
    def index():
        """
        Endpoint to check if the Medical Assistant AI service is operational.

        Returns:
            str: A message indicating the service status.
        """
        return INDEX_RESPONSE

    @app.route('/chat', methods=['POST'])
    @validate_json_input(REQUIRED_FIELDS)  # Ensure the JSON input contains 'message'
    def chat():
        """
        Handle chat requests for medical assistance.

        This function processes user messages, generates AI responses, 
        and includes a disclaimer for non-medical queries.

        Returns:
            flask.Response: JSON response with AI-generated advice or error message.
        """
        data = request.get_json()
        message = data['message']
        logger.info(f"Received message: {message}")

        try:
            # Generate response from the AI
            response = medical_assistant_service.generate_response(message)

            # Check if the response contains a predefined scope warning
            if "This service is for medical-related questions only." not in response:
                # Format the response with a disclaimer for non-medical content
                return jsonify({
                    'response': response,
                    'disclaimer': DISCLAIMER_MESSAGE  # Add disclaimer as a separate field
                })
            else:
                # Return only the response if it's already within medical scope
                return jsonify({'response': response})

        except Exception as e:
            logger.error(f"Exception in /chat endpoint: {e}")
            # Return a standard error response for any exceptions
            return make_response(jsonify(ERROR_RESPONSE), HTTP_INTERNAL_SERVER_ERROR)
