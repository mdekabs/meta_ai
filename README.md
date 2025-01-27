# Medical Assistant AI

A Flask-based microservice for handling medical-related queries using AI. This service leverages a custom AI model to process medical queries, validates inputs, and delivers intelligent responses with a focus on healthcare topics.

## Features
- AI-powered medical query processing
- Input validation and response compression
- Easy-to-use RESTful API endpoints
- Dockerized for simple deployment

## Prerequisites
To run this project, ensure you have the following installed:
- Python 3.11+
- Docker and Docker Compose

## Directory Structure
```plaintext
.
├── app
│   ├── __init__.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── chat_routes.py
│   └── services
│       ├── __init__.py
│       ├── medical_assistant_service.py
│   └── validators
│       ├── __init__.py
│       ├── json_validator.py
│   └── utils
│       ├── __init__.py
│       ├── logger.py
├── tests
│   ├── test_routes.py
│   ├── test_services.py
│   ├── test_validators.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Installation

### Local Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   flask run
   ```

### Docker Setup
1. Build and run the application using Docker Compose:
   ```bash
   docker-compose up --build
   ```

2. Access the service at `http://localhost:5000`.

## API Endpoints

### Health Check
**GET /**
- Description: Verify the service is running.
- Response: `Medical Assistant AI is up and running!`

### Chat
**POST /chat**
- Description: Submit a medical query for AI processing.
- Request Body:
  ```json
  {
    "message": "<Your medical query>"
  }
  ```
- Response:
  ```json
  {
    "response": "<AI-generated response>"
  }
  ```

## Testing
Run tests using pytest:
```bash
pytest
```
Generate coverage report:
```bash
pytest --cov=app
```

## Deployment
This service can be deployed on any container orchestration platform, such as Kubernetes or AWS ECS, using the provided Docker setup.

## Environment Variables
Configure the application using the following variables:
- `FLASK_ENV`: Set Flask environment (`development` or `production`).
- `FLASK_DEBUG`: Enable or disable debug mode.
- `FLASK_RUN_HOST`: Host for Flask to run on.
- `FLASK_RUN_PORT`: Port for Flask to listen on.

## Notes
- This service is designed for medical-related queries only. Ensure prompts include at least one medical keyword.
- Responses include a disclaimer highlighting that the AI is not a substitute for professional medical advice.

