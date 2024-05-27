from flask import Flask, jsonify, request, make_response
from meta_ai_api import MetaAI
import logging
import requests

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Set a default timeout for all requests made by the requests library
requests_timeout = 10  # Adjust the timeout value as needed
requests.adapters.DEFAULT_RETRIES = 3  # Retry failed requests up to 3 times
requests.adapters.DEFAULT_TIMEOUT = requests_timeout

class MedicalAssistantService:
    def __init__(self):
        self.ai = MetaAI()  # No need to pass request_timeout here

    def generate_response(self, message):
        try:
            # Generate AI response
            response = self.ai.prompt(message=message)
            return response
        except Exception as e:
            app.logger.error(f"Error generating response: {e}")
            return "An error occurred while processing your request."

medical_assistant_service = MedicalAssistantService()

@app.route('/')
def index():
    return "Medical Assistant AI ready for use."

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return make_response(jsonify({'error': 'Invalid input'}), 400)
        
        message = data['message']
        app.logger.info(f"Received message: {message}")

        # Generate response from the AI
        response = medical_assistant_service.generate_response(message)
        
        # Include disclaimer in the response
        disclaimer = "Please note: This AI is not a substitute for professional medical advice. Always consult with a healthcare provider for medical advice."
        full_response = f"{response}\n\n{disclaimer}"
        
        return jsonify({'response': full_response})
    except Exception as e:
        app.logger.error(f"Exception in /chat endpoint: {e}")
        return make_response(jsonify({'error': 'Internal server error'}), 500)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
