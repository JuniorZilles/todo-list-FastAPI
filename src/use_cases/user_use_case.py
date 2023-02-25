from src.repositories.user_repository import UserRepository

class UserUseCase():
    def __init__(self) -> None:
        self.repo = UserRepository()

    def save(self, data):
        return self.repo.save(data)