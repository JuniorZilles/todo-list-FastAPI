from fastapi import FastAPI
from src.controllers.todo_controller import router as todo
from src.controllers.user_controller import router as user

def register_blueprints(app:FastAPI):
    prefix = '/api/v1'
    app.include_router(user, prefix=prefix)
    app.include_router(todo, prefix=prefix)