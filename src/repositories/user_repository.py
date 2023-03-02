from src.models.user_model import User
from src.db import db
from sqlalchemy import or_

class UserRepository():
    def __init__(self) -> None:
        self.db = db
    
    def save(self, data:dict):
        user = User(**data.__dict__)
        
        self.db.add(user)
        self.db.commit()
        return user
    
    def findById(self, id:str):
        return self.db.query(User).filter(User.id == id).first()
    
    def findByDuplicate(self, cpf:str, email:str):
        return self.db.query(User).filter(or_(User.email == email, User.cpf == cpf)).first()
    
    def find(self, limit:int, offset:int):
        return self.db.query(User).offset(offset).limit(limit).all()
    
    def delete(self, id:str):
        user = self.db.query(User).filter(User.id == id).delete()
        return user
    
    def update(self, id:str, payload):
        user = self.db.query(User).filter(User.id == id).update(payload)
        return user