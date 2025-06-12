from fastapi import APIRouter, HTTPException, status
from models.todo import Todo
from schemas.todo import GetTodo, PostTodo, PutTodo


todo_router = APIRouter(prefix="/api", tags=["Todo"])


@todo_router.get("/")
async def get_all_todos():
    return await GetTodo.from_queryset(Todo.all())


@todo_router.post("/")
async def create_todo(body: PostTodo):
    row = await Todo.create(**body.dict(exclude_unset = True))
    return await GetTodo.from_tortoise_orm(row)


@todo_router.put("/{todo_id}")
async def update_todo(todo_id: int, body: PutTodo):
    data = body.dict(exclude_unset=True)
    exists = await Todo.filter(id=todo_id).exists()
    if not exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    await Todo.filter(id=todo_id).update(**data)
    return await GetTodo.from_queryset_single(Todo.get(id=todo_id))


@todo_router.delete("/{todo_id}")
async def delete_todo(todo_id: int):
    exists = await Todo.filter(id=todo_id).exists()
    if not exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    await Todo.filter(id=todo_id).delete()
    return 'todo scueess'
   
