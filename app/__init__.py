from flask import Flask
from flask_compress import Compress
from app.routes import initialize_routes
from app.extensions import initialize_extensions

# Constants for configuration or setup
APP_NAME = "__name__"

def create_app():
    """
    Create and configure the Flask application instance.

    This function initializes the Flask app, sets up extensions, 
    and defines routes.

    Returns:
        Flask: The configured Flask application object.
    """
    app = Flask(APP_NAME)  # Create Flask application instance
    initialize_extensions(app)  # Set up extensions like databases, etc.
    initialize_routes(app)  # Register all routes for the application
    return app
