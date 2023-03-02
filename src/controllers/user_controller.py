from fastapi import APIRouter
from src.utils.request_responses import alreadyCreated, internalError, notFound, success
from src.validators.user.post_schema import CreateUser
from src.validators.user.put_schema import UpdateUser
from src.use_cases.user_use_case import UserUseCase

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}, 500: {
        "description": "Internal server error"}, 400: {"description": "Bad request"}},
)

@router.post('/', status_code=201)
def create(payload:CreateUser):
    try:
        user = UserUseCase().save(payload)
        if user == None:
            return alreadyCreated()
        return user.toDict()
    except Exception as e:
        return internalError(e)


@router.get('/{id}')
def show(id: str):
    try:
        user = UserUseCase().findById(id)
        if user == None:
            return notFound()
        return user.toDict()
    except Exception as e:
        return internalError(e)

@router.get('/')
def list(offset: int = 0, limit: int = 250):
    try:
        users = UserUseCase().findAll(limit, offset)
        items = [user.toDict() for user in users]
        return {'limit':limit, 'offset': offset, 'items': items }
    except Exception as e:
        return internalError(e)

@router.put("/{id}")
async def update(id: str, payload:UpdateUser):
    try:
        qtd = UserUseCase().update(id, payload)
        if qtd > 0:
            return success()
        else:
            return notFound()
    except Exception as e:
        return internalError(e)

@router.delete("/{id}")
async def delete(id: str):
    try:
        qtd = UserUseCase().delete(id)
        if qtd > 0:
            return success()
        else:
            return notFound()
    except Exception as e:
        return internalError(e)
