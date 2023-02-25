from pydantic import BaseModel, validator
from datetime import datetime
import re

class Task(BaseModel):
    date: datetime
    description: str
    user_id: str

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

    @validator('user_id')
    def user_info(cls, v):
        if v.strip() == '' or v == None:
            raise ValueError('user_id should not be empty')
        if re.search('^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$', v) == None:
            raise ValueError('user_id doesnt match the format')
        return v
