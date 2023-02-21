from flask import Flask
from src.controllers.todo_controller import todo


app = Flask(__name__)

app.register_blueprint(todo)

@app.errorhandler(404)
def not_found(error):
    return {'status':404, 'message': 'resource not found'}, 404