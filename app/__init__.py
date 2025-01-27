from flask import Flask
from flask_compress import Compress
from app.routes import initialize_routes
from app.extensions import initialize_extensions

def create_app():
    app = Flask(__name__)
    initialize_extensions(app)
    initialize_routes(app)
    return app
