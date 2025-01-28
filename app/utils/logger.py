import logging
import os

# Get the Flask environment from environment variables
FLASK_ENV = os.getenv('FLASK_ENV', 'development')

# Configure logging based on the environment
if FLASK_ENV == 'production':
    # Use INFO level for production to log significant events
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
else:
    # Use DEBUG level for development to log all events including debug information
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

# Create a logger for this module
logger = logging.getLogger(__name__)
