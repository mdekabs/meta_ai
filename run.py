from app import create_app
from app.config import Config

# Create the Flask application instance
app = create_app()

if __name__ == '__main__':
    # Run the Flask application using configuration from Config class
    app.run(
        debug=Config.FLASK_DEBUG, 
        host=Config.FLASK_RUN_HOST, 
        port=Config.FLASK_RUN_PORT
    )
