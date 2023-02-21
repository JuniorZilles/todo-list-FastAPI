import os
from waitress import serve
from src.app import app


env = os.getenv('PYTHON_ENV', default='dev')

if __name__ == '__main__':
    if env == 'dev':
        app.run(port=3000, debug=True)
    else:
        serve(app, port=300, threads=2, url_prefix='/api/v1')