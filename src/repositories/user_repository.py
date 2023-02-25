from src.models.user_model import User
from src.db import db

class UserRepository():
    def __init__(self) -> None:
        self.db = db
    
    def save(self, data:dict):
        user = User(**data.__dict__)
        
        self.db.add(user)
        self.db.commit()
        return user