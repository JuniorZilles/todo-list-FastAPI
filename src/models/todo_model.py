import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime, inspect
from sqlalchemy.dialects.postgresql import UUID
from src.models.user_model import User
from src.models.base import Base

class Todo(Base):
    __tablename__= 'todo'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    description = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey(User.id), nullable=False)

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
