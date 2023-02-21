from flask import Blueprint

todo = Blueprint('todo', __name__, url_prefix='/todo')

@todo.post('/')
def create():
    return "<p>Hello, World!</p>"

@todo.get('/')
def show():
    return "<p>Hello, World!</p>"