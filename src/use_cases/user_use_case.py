from src.repositories.user_repository import UserRepository
from src.utils.criptograph_string import encryptString

class UserUseCase():
    def __init__(self) -> None:
        self.repo = UserRepository()

    def save(self, data):
        data.password = encryptString(data.password)
        user = self.repo.save(data)
        return user
    
    def findById(self, id:str):
        user = self.repo.findById(id)
        return user
    
    def findAll(self, limit:int, offset:int):
        users =  self.repo.find(limit, offset)
        return users
    
    def update(self, id:str, payload):
        return self.repo.update(id, payload)
    
    def delete(self, id: str):
        return self.repo.delete(id)