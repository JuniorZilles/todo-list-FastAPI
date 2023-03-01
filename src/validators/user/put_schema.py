from pydantic import BaseModel, validator
from datetime import date
import re

class UpdateUser(BaseModel):
    name: str | None = None
    birth_date: date | None = None
    address:str | None = None
    city:str | None = None
    state:str | None = None
    country:str | None = None
    zip_code:str | None = None

    @validator('name')
    def name_size(cls, v):
        if v.strip() == '' or v == None:
            raise ValueError('name should not be empty')
        if len(v) < 7:
            raise ValueError('name size must be greater than 6')
        return v

    @validator('birth_date')
    def birth_date_format(cls, v):
        if v == None:
            raise ValueError('birth_date is required')
        return v

    @validator('address')
    def address_size(cls, v):
        if v.strip() == '' or v == None:
            raise ValueError('address should not be empty')
        if len(v) < 6:
            raise ValueError('address size must be greater than 5')
        return v
    
    @validator('city')
    def city_size(cls, v):
        if v.strip() == '' or v == None:
            raise ValueError('city should not be empty')
        if len(v) < 4:
            raise ValueError('city size must be greater than 3')
        return v

    @validator('state')
    def state_size(cls, v):
        if v.strip() == '' or v == None:
            raise ValueError('state should not be empty')
        if len(v) < 2:
            raise ValueError('state size must be greater than 1')
        return v

    @validator('country')
    def country_size(cls, v):
        if v.strip() == '' or v == None:
            raise ValueError('country should not be empty')
        if len(v) < 2:
            raise ValueError('country size must be greater than 1')
        return v
    
    @validator('zip_code')
    def zip_code_size(cls, v):
        if v.strip() == '' or v == None:
            raise ValueError('zip_code should not be empty')
        if len(v) < 2:
            raise ValueError('zip_code size must be greater than 1')
        if re.search('^[0-9]{5}-[0-9]{3}$', v) == None:
            raise ValueError('zip_code doesnt match the format ^[0-9]{5}-[0-9]{3}$')
        return v