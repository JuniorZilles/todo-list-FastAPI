post_schema = {
    'type': 'object',
    'properties': {
        'description': {
            'type': 'string',
            "minLength": 4
        },
        'date': {
            'type': 'string',
            'description': 'Task date-time',
            'format': 'date-time'
        },
        'user_id': {
            'type': 'string',
            'pattern': '^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$'
        },
    },
    'required': [
        'description',
        'date',
        'user_id'
    ]
}
