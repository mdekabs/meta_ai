from flask import Flask, jsonify, request
from meta_ai_api import MetaAI

app = Flask(__name__)

class MetaAIService:
    def __init__(self):
        self.ai = MetaAI()

    def generate_response(self, message):
        return self.ai.prompt(message=message)

ai_service = MetaAIService()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['message']
    response = ai_service.generate_response(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0"i, port=5000)
