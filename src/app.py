from fastapi import FastAPI
from fastapi.exceptions  import RequestValidationError
from fastapi.responses import JSONResponse
from src.create_db import createDatabase
from src.routes import register_blueprints

app = FastAPI()

createDatabase()
register_blueprints(app)

@app.exception_handler(RequestValidationError)
def bad_request(request, exc):
    if isinstance(exc, RequestValidationError):
        return JSONResponse({'status':400, 'errors': exc.errors()})
    return exc

@app.exception_handler(404)
def not_found(request, exc):
    return JSONResponse({'status':404, 'message': 'resource not found'})