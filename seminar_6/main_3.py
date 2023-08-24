# Создать API для управления списком задач.
# Каждая задача должна содержать поля "название", "описание" и "статус" (выполнена/не выполнена).
# API должен позволять выполнять CRUD операции с задачами.
# from typing import List
#
# import databases
# import sqlalchemy
# from fastapi import FastAPI
# from pydantic import BaseModel, Field, EmailStr, SecretStr
#
# DATABASE_URL = "sqlite:///seminar_6_3.db"
#
# database = databases.Database(DATABASE_URL)
#
# metadata = sqlalchemy.MetaData()
#
# users = sqlalchemy.Table(
#     "tasks",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("title", sqlalchemy.String(32)),
#     sqlalchemy.Column("description", sqlalchemy.String(128)),
#     sqlalchemy.Column("status", sqlalchemy.Boolean()),
# )
# engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# metadata.create_all(engine)
#
# app = FastAPI()
#
#
# class Task(BaseModel):
#     title: str = Field(min_length=2, max_length=32, title='Title')
#     description: str = Field(min_length=2, max_length=128, title='Description')
#     status: str = Field(default=0, max_length=32)
#
#
# @app.on_event("startup")
# async def startup():
#     await database.connect()
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()
#
#
# @app.get("/tasks/", response_model=List[Task])
# async def read_users():
#     query = users.select()
#     return await database.fetch_all(query)
#
#
# @app.get("/tasks/{tasks_id}", response_model=Task)
# async def read_user(user_id: int):
#     query = users.select().where(users.c.id == user_id)
#     return await database.fetch_one(query)
#
#
# @app.post("/tasks/", response_model=Task)
# async def create_user(task: Task):
#     query = task.insert().values(title=task.title, description=task.description, status=task.status)
#     last_record_id = await database.execute(query)
#     return {**task.dict(), "id": last_record_id}
#
#
# @app.put("/tasks/{task_id}", response_model=Task)
# async def update_user(task_id: int, new_task: Task):
#     query = users.update().where(users.c.id == task_id).values(**new_task.dict())
#     await database.execute(query)
#     return {**new_task.dict(), "id": task_id}
#
#
# @app.delete("/tasks/{task_id}")
# async def delete_task(task_id: int):
#     query = task.delete().where(task.c.id == task_id)
#     await database.execute(query)
#     return {'message': 'Task deleted'}
#

from typing import List

import databases
import sqlalchemy
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

DATABASE_URL = "sqlite:///seminar_db2.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

tasks = sqlalchemy.Table(
    "tasks",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(32)),
    sqlalchemy.Column("description", sqlalchemy.String(128)),
    sqlalchemy.Column("status", sqlalchemy.Boolean()),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
metadata.create_all(engine)

app = FastAPI()


class TaskIn(BaseModel):
    title: str = Field(max_length=32, title="Title", )
    description: str = Field(max_length=128, title="Description", )
    status: bool = Field(default=0, title="Status", )


class Task(TaskIn):
    id: int


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/tasks/', response_model=List[Task])
async def read_tasks():
    query = tasks.select()
    return await database.fetch_all(query)


@app.get('/tasks/{task_id}', response_model=Task)
async def read_task(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    return await database.fetch_one(query)


@app.post('/tasks/', response_model=Task)
async def create_task(task: TaskIn):
    query = tasks.insert().values(**task.model_dump())
    last_record_id = await database.execute(query)
    return {**task.model_dump(), "id": last_record_id}


@app.put('/tasks/{task_id}', response_model=Task)
async def update_task(new_task: TaskIn, task_id: int):
    query = tasks.update().where(tasks.c.id == task_id).values(**new_task.model_dump())
    await database.execute(query)
    return {**new_task.model_dump(), "id": task_id}


@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    await database.execute(query)
    return {"message": "User deleted"}


if __name__ == "__main__":
    uvicorn.run("task_2:app", port=8001)