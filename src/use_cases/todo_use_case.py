from src.repositories.todo_repository import TodoRepository
from src.use_cases.user_use_case import UserUseCase

class TodoUseCase():
    def __init__(self) -> None:
        self.repo = TodoRepository()
        self.userUseCase = UserUseCase()

    def save(self, data):
        if self.userUseCase.findById(data.user_id) == None:
            raise Exception("user_id doesn't match a existing user")
        return self.repo.save(data)

    def findById(self, id:str):
        return self.repo.findById(id)
    
    def findAll(self, limit:int, offset:int):
        return self.repo.find(limit, offset)
    
    def update(self, id:str, payload):
        return self.repo.update(id, payload)
    
    def delete(self, id: str):
        return self.repo.delete(id)