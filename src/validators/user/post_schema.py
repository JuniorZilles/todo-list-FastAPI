post_schema = {
    'title': 'User',
    'description': 'User data to register a task',
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string',
            "minLength": 7,
            'description': 'User name'
        },
        'email': {
            'type': 'string',
            'description': 'User email',
            'format': 'email'
        },
        'cpf': {
            'type': 'string',
            'description': 'User cpf',
            'pattern': '^\d{3}.\d{3}.\d{3}-\d{2}$'
        },
        'birth_date': {
            'type': 'string',
            'description': 'User birthdate',
            'format':'date'
        },
        'password': {
            'type': 'string',
            "minLength": 6,
            'description': 'User pasword'
        },
        'address': {
            'type': 'string',
            "minLength": 5,
            'description': 'User address'
        },
        'city': {
            'type': 'string',
            "minLength": 4,
            'description': 'User city'
        },
        'state': {
            'type': 'string',
            "minLength": 2,
            'description': 'User state'
        },
        'country': {
            'type': 'string',
            "minLength": 2,
            'description': 'User country'
        },
        'zip_code': {
            'type': 'string',
            'description': 'User zip code',
            'pattern':'^[0-9]{5}-[0-9]{3}$'
        }
    },
    'required': ['email',
                 'name',
                 'cpf',
                 'birth_date',
                 'password',
                 'address',
                 'city',
                 'state',
                 'country',
                 'zip_code']
}
