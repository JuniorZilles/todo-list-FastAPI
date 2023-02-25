from src.db import engine
from src.models.base import Base
from src.models.user_model import User
from src.models.todo_model import Todo

def createDatabase():
    Base.metadata.create_all(engine)