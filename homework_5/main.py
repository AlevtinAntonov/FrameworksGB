from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, EmailStr, SecretStr
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='./homework_5/templates')

USERS = []


class User(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    password: SecretStr


for i in range(5):
    USERS.append(User(user_id=i, name=f'User_{i}', email=f'user_{i}@domain.ru', password=f'password{i}'))
print(USERS)


@app.get('/users/')
async def all_users():
    return {'users': USERS}


@app.post('/user/add')
async def add_user(user: User):
    USERS.append(user)
    return {"user": user, "status": "added"}


@app.put('/user/update/{user_id}')
async def update_user(user_id: int, user: User):
    for u in USERS:
        if u.user_id == user_id:
            u.name = user.name
            u.email = user.email
            u.password = user.password
            return {"user": user, "status": "updated"}
    return HTTPException(404, 'User not found')


@app.delete('/user/delete/{user_id}')
async def delete_user(user_id: int, user: User):
    for u in USERS:
        if u.user_id == user_id:
            USERS.remove(u)
            return {"status": "Delete success"}
    return HTTPException(404, 'User not found')


@app.get("/users-list/")
async def read_item(request: Request):
    return templates.TemplateResponse('item.html', {'request': request, 'users': USERS})
