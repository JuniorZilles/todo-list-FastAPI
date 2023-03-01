import os
from cryptography.fernet import Fernet

key = os.getenv('KEY', default='xEYR6SNfGzBvqgiTyg-V1Hbr_f0WmNuwZEpqhVu7JgA=').encode()

def encryptString(value:str):
    fernet = Fernet(key)
    return fernet.encrypt(value.encode())

def decryptString(value:str):
    fernet = Fernet(key)
    return fernet.decrypt(value.encode())