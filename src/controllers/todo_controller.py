from fastapi import APIRouter
from src.utils.request_responses import internalError, notFound, success
from src.validators.todo.post_schema import CreateTask
from src.validators.todo.put_schema import UpdateTask
from src.use_cases.todo_use_case import TodoUseCase

router = APIRouter(
    prefix="/todo",
    tags=["todo"],
    responses={404: {"description": "Not found"}, 500: {
        "description": "Internal server error"}, 400: {"description": "Bad request"}},
)

@router.post('/', status_code=201)
def create(task: CreateTask):
    try:
        todo = TodoUseCase().save(task)
        return todo.toDict()
    except Exception as e:
        return internalError(e)

@router.get('/{id}')
def show(id: str):
    try:
        todo = TodoUseCase().findById(id)
        if todo == None:
            return notFound()
        return todo.toDict()
    except Exception as e:
        return internalError(e)

@router.get('/')
def list(offset: int = 0, limit: int = 250):
    try:
        todos = TodoUseCase().findAll(limit, offset)
        items = [todo.toDict() for todo in todos]
        return {'limit':limit, 'offset': offset, 'items': items }
    except Exception as e:
        return internalError(e)

@router.put("/{id}")
async def update(id: str, payload: UpdateTask):
    try:
        qtd = TodoUseCase().update(id, payload)
        if qtd > 0:
            return success()
        else:
            return notFound()
    except Exception as e:
        return internalError(e)

@router.delete("/{id}")
async def delete(id: str):
    try:
        qtd = TodoUseCase().delete(id)
        if qtd > 0:
            return success()
        else:
            return notFound()
    except Exception as e:
        return internalError(e)