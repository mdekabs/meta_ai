from flask import request, jsonify, make_response
from functools import wraps

def validate_json_input(expected_keys):
    """
    Decorator to validate JSON input in Flask routes.

    This decorator checks if the JSON payload contains all the expected keys.

    Args:
        expected_keys (list): A list of keys that must be present in the JSON data.

    Returns:
        function: A decorator function that wraps the route handler.
    """
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            # Retrieve JSON data from the request
            data = request.get_json()
            
            # Check if data is None or if all expected keys are not present
            if not data or not all(key in data for key in expected_keys):
                # Return an error if validation fails
                return make_response(jsonify({'error': 'Invalid input or missing required fields'}), 400)
            
            # If validation passes, proceed with the function
            return f(*args, **kwargs)
        return wrapped
    return decorator
