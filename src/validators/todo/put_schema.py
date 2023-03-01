from pydantic import BaseModel, validator
from datetime import datetime
import re

class UpdateTask(BaseModel):
    date: datetime | None = None
    description: str | None = None

    @validator('date')
    def date_size(cls, v):
        if v == None:
            raise ValueError('date should not be empty')
        return v
    
    @validator('description')
    def description_size(cls, v):
        if v.strip() == '' or v == None:
            raise ValueError('description should not be empty')
        if len(v) < 4:
            raise ValueError('description size must be greater than 3')
        return v
