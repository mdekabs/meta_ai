from flask import jsonify, request, make_response
from app.services.medical_service import MedicalAssistantService
from app.utils.validators import validate_json_input
from app.utils.logger import logger

# Initialize AI model and service
from meta_ai_api import MetaAI
ai_model = MetaAI()
medical_assistant_service = MedicalAssistantService(ai_model)

def initialize_routes(app):
    @app.route('/')
    def index():
        return "Medical Assistant AI is up and running!"

    @app.route('/chat', methods=['POST'])
    @validate_json_input(['message'])
    def chat():
    data = request.get_json()
    message = data['message']
    logger.info(f"Received message: {message}")

    try:
        # Generate response from the AI
        response = medical_assistant_service.generate_response(message)
        
        if "This service is for medical-related questions only." not in response:
            disclaimer = "Please note: This AI is not a substitute for professional medical advice. Always consult with a healthcare provider for medical advice."
            return jsonify({
                'response': response,
                'disclaimer': disclaimer  # Add disclaimer as a separate field
            })
        else:
            return jsonify({'response': response})
    except Exception as e:
        logger.error(f"Exception in /chat endpoint: {e}")
        return make_response(jsonify({'error': 'Internal server error'}), 500)
