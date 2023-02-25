from fastapi import status, APIRouter
from fastapi.responses import JSONResponse
from src.validators.todo.post_schema import Task
from src.use_cases.todo_use_case import TodoUseCase

router = APIRouter(
    prefix="/todo",
    tags=["todo"],
    responses={404: {"description": "Not found"}, 500: {
        "description": "Internal server error"}, 400: {"description": "Bad request"}},
)

@router.post('/', status_code=201)
def create(task: Task):
    try:
        todo = TodoUseCase().save(task)
        return todo.toDict()
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
async def update(id: str, task: Task):
    return "<p>Hello, World!</p>"

@router.delete("/{id}")
async def delete(id: str):
    return "<p>Hello, World!</p>"