import os

class Config:
    """
    Configuration class for Flask application settings.

    This class uses environment variables to set up configuration 
    parameters for the Flask application.
    """
    
    # Environment setting for Flask
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    
    # Debug mode toggle
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'True') == 'True'
    
    # Host address for running the Flask server
    FLASK_RUN_HOST = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
    
    # Port number for running the Flask server
    FLASK_RUN_PORT = int(os.getenv('FLASK_RUN_PORT', 5000))
