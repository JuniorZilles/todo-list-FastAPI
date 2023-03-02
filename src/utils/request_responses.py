from fastapi import status
from fastapi.responses import JSONResponse

def notFound():
    response = JSONResponse(content={'status':404, 'message': 'Not found'})
    response.status_code = status.HTTP_404_NOT_FOUND
    return response

def internalError(e):
    response = JSONResponse(content={'status':500, 'message': str(e)})
    response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return response

def success():
    response = JSONResponse(content={'status':200, 'message': 'Success'})
    response.status_code = status.HTTP_200_OK
    return response

def alreadyCreated():
    response = JSONResponse(content={'status':409, 'message': 'Resource already created'})
    response.status_code = status.HTTP_409_CONFLICT
    return response