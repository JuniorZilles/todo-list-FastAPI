from flask import Blueprint, g
from flask_expects_json import expects_json
from src.validators.user.post_schema import post_schema
user = Blueprint('user', __name__, url_prefix='/user')

@user.post('/')
@expects_json(post_schema, check_formats=True)
def create():
    #user = User().from_dict(g.data)
    return "<p>Hello, World!</p>"

@user.get('/')
def show():
    return "<p>Hello, World!</p>"