from pydantic import BaseModel, validator
from datetime import date
import re

from src.utils.cpf_validator import cpf_validate

class User(BaseModel):
    name: str
    email: str
    cpf: str
    birth_date: date
    password:str
    address:str
    city:str
    state:str
    country:str
    zip_code:str

    @validator('name')
    def name_size(cls, v):
        if v.strip() == '' or v == None:
            raise ValueError('name should not be empty')
        if len(v) < 7:
            raise ValueError('name size must be greater than 6')
        return v
    
    @validator('email')
    def email_format(cls, v):
        if v.strip() == '' or v == None:
            raise ValueError('email is required')
        if re.search("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", v) == None:
            raise ValueError('invalid email')
        return v

    @validator('cpf')
    def cpf_format(cls, v):
        if v.strip() == '' or v == None:
            raise ValueError('cpf is required')
        if re.search('^\d{3}.\d{3}.\d{3}-\d{2}$', v) == None:
            raise ValueError('cpf doesnt match the format ^\d{3}.\d{3}.\d{3}-\d{2}$')
        if cpf_validate(v) != True:
            raise ValueError('invalid cpf')
        return v

    @validator('birth_date')
    def birth_date_format(cls, v):
        if v == None:
            raise ValueError('birth_date is required')
        return v

    @validator('password')
    def password_size(cls, v):
        if v.strip() == '' or v == None:
            raise ValueError('password should not be empty')
        if len(v) < 6:
            raise ValueError('password size must be greater than 6')
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