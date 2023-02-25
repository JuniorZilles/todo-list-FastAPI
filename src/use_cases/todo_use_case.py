from src.repositories.todo_repository import TodoRepository

class TodoUseCase():
    def __init__(self) -> None:
        self.repo = TodoRepository()

    def save(self, data):
        return self.repo.save(data)