from flask import request, jsonify, make_response
from functools import wraps

def validate_json_input(expected_keys):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            data = request.get_json()
            if not data or not all(key in data for key in expected_keys):
                return make_response(jsonify({'error': 'Invalid input or missing required fields'}), 400)
            return f(*args, **kwargs)
        return wrapped
    return decorator
