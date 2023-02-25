from src.models.todo_model import Todo
from src.db import db

class TodoRepository():
    def __init__(self) -> None:
        self.db = db

    def save(self, data:dict):
        todo = Todo(**data.__dict__)
        
        self.db.add(todo)
        self.db.commit()
        return todo