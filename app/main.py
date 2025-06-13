from fastapi import FastAPI
from routes.todo import todo_router
from tortoise.contrib.fastapi import register_tortoise
from config.config import POSTGRES_URL

app = FastAPI()
app.include_router(todo_router)
register_tortoise(
    app=app,
    db_url=POSTGRES_URL,
    add_exception_handlers=True,
    generate_schemas=True,
    modules={"models": ["models.todo"]}
)

@app.get("/")
def index():
    return "This api is running"
