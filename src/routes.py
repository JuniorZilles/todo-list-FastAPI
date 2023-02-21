from flask import Flask
from src.controllers.todo_controller import todo
from src.controllers.user_controller import user

def register_blueprints(app:Flask):
    app.register_blueprint(todo)
    app.register_blueprint(user)