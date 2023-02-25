from fastapi import status, APIRouter
from fastapi.responses import JSONResponse
from src.validators.user.post_schema import User
from src.use_cases.user_use_case import UserUseCase

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}, 500: {
        "description": "Internal server error"}, 400: {"description": "Bad request"}},
)

@router.post('/', status_code=201)
def create(payload:User):
    try:
        user = UserUseCase().save(payload)
        return user.toDict()
    except Exception as e:
        response = JSONResponse(content={'status':500, 'message': str(e)})
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


@router.get('/{id}')
def show(id: str):
    return "<p>Hello, World!</p>"

@router.get('/')
def list():
    return "<p>Hello, World!</p>"

@router.put("/{id}")
async def update(id: str, user :User):
    return "<p>Hello, World!</p>"

@router.delete("/{id}")
async def delete(id: str):
    return "<p>Hello, World!</p>"
