from flask_compress import Compress

def initialize_extensions(app):
    Compress(app)
