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
    
    def findById(self, id:str):
        return self.db.query(Todo).filter(Todo.id == id).first()
    
    def find(self, limit:int, offset:int):
        return self.db.query(Todo).offset(offset).limit(limit).all()
    
    def delete(self, id:str):
        todo = self.db.query(Todo).filter(Todo.id == id).delete()
        return todo
    
    def update(self, id:str, payload):
        todo = self.db.query(Todo).filter(Todo.id == id).update(payload)
        return todo