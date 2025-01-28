from flask_compress import Compress

def initialize_extensions(app):
    """
    Initialize Flask extensions for the application.

    This function sets up the Compress extension which enables 
    HTTP response compression.

    Args:
        app (Flask): The Flask application instance to extend.
    """
    # Initialize and attach the Compress extension to the Flask app
    Compress(app)
