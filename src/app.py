from flask import Flask, jsonify
from jsonschema import ValidationError
from src.routes import register_blueprints


app = Flask(__name__)

register_blueprints(app)

@app.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        return jsonify({'error': original_error.message}), 400
    return error

@app.errorhandler(404)
def not_found(error):
    return {'status':404, 'message': 'resource not found'}, 404