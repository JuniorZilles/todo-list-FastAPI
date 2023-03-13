def user():
    return {
        "email": "baris@mail.com",
        "name": "teste do brasil",
        "cpf": "976.066.650-28",
        "birth_date": "2014-01-10",
        "password": "kjhelkgnkwjrengkenr",
        "address": "rua amul",
        "city":"dois vizinhos",
        "state": "RS",
        "country": "brasil",
        "zip_code": "93950-000"
    }

def update_user():
    return {
        "name": "atualização do brasil",
    }

def invalid_user():
    return {
        "email": "mail.com",
        "name": "test",
        "cpf": "976.066.650",
        "birth_date": "2014-01",
        "password": "kjhelk",
        "address": "rua amul",
        "city":"d",
        "state": "R",
        "country": "b",
        "zip_code": "93950"
    }