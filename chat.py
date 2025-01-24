"""Medical Assistant AI: A Flask-based application for handling medical queries with AI support.

This script sets up a web service that processes medical-related questions using an AI model. 
It includes input validation, error handling, and response compression for improved performance.

Dependencies:
    - Flask for web framework
    - flask_compress for response compression
    - logging for log management
    - meta_ai_api (custom module) for AI functionalities

Environment Variables:
    - FLASK_ENV: Set the Flask environment (default: 'development')
    - FLASK_DEBUG: Enable or disable debug mode (default: True)
    - FLASK_RUN_HOST: Host for Flask to run on (default: '0.0.0.0')
    - FLASK_RUN_PORT: Port for Flask to listen on (default: 5000)

Endpoints:
    - '/' : Health check endpoint
    - '/chat' : POST endpoint for medical queries

Note:
    - This service expects messages to contain medical keywords to proceed with AI interaction.
    - Compression is applied to all responses for data efficiency.
"""

from flask import Flask, jsonify, request, make_response, current_app
from meta_ai_api import MetaAI
import logging
import os
from functools import wraps
import requests
from flask_compress import Compress

# Configuration for environment variables
FLASK_ENV = os.getenv('FLASK_ENV', 'development')
FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'True') == 'True'
FLASK_RUN_HOST = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
FLASK_RUN_PORT = int(os.getenv('FLASK_RUN_PORT', 5000))

app = Flask(__name__)
Compress(app)  # Initialize Flask-Compress

# Configure logging with different format for production and development
if FLASK_ENV == 'production':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
else:
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# Custom function to handle JSON input validation
def validate_json_input(expected_keys):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            data = request.get_json()
            if not data or not all(key in data for key in expected_keys):
                return make_response(jsonify({'error': 'Invalid input or missing required fields'}), 400)
            return f(*args, **kwargs)
        return wrapped
    return decorator

# Medical Keywords for filtering messages
MEDICAL_KEYWORDS = {
    "health", "medicine", "symptom", "disease", "treatment",
    "doctor", "nurse", "diagnosis", "prescription", "therapy"
}

class MedicalAssistantService:
    def __init__(self, ai_model):
        self.ai_model = ai_model
    
    def generate_response(self, message):
        try:
            # Check if the message contains any medical-related keyword
            if not any(keyword in message.lower() for keyword in MEDICAL_KEYWORDS):
                keywords_str = ", ".join(MEDICAL_KEYWORDS)
                return f"This service is for medical-related questions only. Your message must contain at least one of these keywords: {keywords_str}."

            # Log the types of arguments for debugging
            logger.debug(f"Message type: {type(message)}, Message content: {message}")
            
            # Generate AI response
            response = self.ai_model.prompt(message)
            return response
        except Exception as e:
            logger.error(f"Unexpected error generating response: {type(e).__name__} - {str(e)}")
            return "An unexpected error occurred."

# Initialize AI model
ai_model = MetaAI()
medical_assistant_service = MedicalAssistantService(ai_model)

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
        
        # Include disclaimer if the response isn't about the service scope
        if "This service is for medical-related questions only." not in response:
            disclaimer = "Please note: This AI is not a substitute for professional medical advice. Always consult with a healthcare provider for medical advice."
            full_response = f"{response}\n\n{disclaimer}"
        else:
            full_response = response
        
        return jsonify({'response': full_response})
    except Exception as e:
        logger.error(f"Exception in /chat endpoint: {e}")
        return make_response(jsonify({'error': 'Internal server error'}), 500)

if __name__ == '__main__':
    app.run(debug=FLASK_DEBUG, host=FLASK_RUN_HOST, port=FLASK_RUN_PORT)
