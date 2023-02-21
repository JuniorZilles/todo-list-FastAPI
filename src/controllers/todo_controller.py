from flask import Blueprint, g
from flask_expects_json import expects_json
from src.validators.todo.post_schema import post_schema

todo = Blueprint('todo', __name__, url_prefix='/todo')

@todo.post('/')
@expects_json(post_schema, check_formats=True)
def create():
    #todo = Todo().from_dict(g.data)
    return "<p>Hello, World!</p>"

@todo.get('/')
def show():
    return "<p>Hello, World!</p>"