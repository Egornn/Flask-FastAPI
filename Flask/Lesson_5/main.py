from fastapi import FastAPI
import logging 
from typing import Optional
from pydantic import BaseModel


app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class User(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    password: str


@app.get("/")
async def read_root():
    logger.info('GET request: "Hello world!"')
    return {"Hello": "World"}

@app.post("/users/")
async def post_user(user: User):
    logger.info("POST request")
    return user

@app.get("/users/{user_id}")
async def create_user(user_id: int, username:str=None):
    return {"user_id":user_id, 'username':username}

@app.put("/users/{user_id}")
async def change_user(user_id, user: User):
    logger.info(f'PUT request for user id = {user_id}.')
    return {"user_id": user_id, "user": user}

@app.delete("/users/del/{user_id}")
async def delete_user (user_id):
    logger.info('DELETE request')
    return {"user_id":user_id}

# curl -X 'POST' 'http://127.0.0.1:8000/users/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "BestSale", "password": "bestpassword", "email": "best@mail.com"}'

# Invoke-RestMethod -Uri 'http://127.0.0.1:8000/users/' -Method Post -Headers @{
#     "accept" = "application/json"
#     "Content-Type" = "application/json"
# } -Body @{
#     "name" = "BestSale"
#     "password" = "bestpassword"
#     "email" = "best@mail.com"
# } | ConvertTo-Json


# @app.post("/items/")
# async def create_item(item: Item):
#     logger.info('Отработал POST запрос.')
#     return item

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     logger.info(f'Отработал PUT запрос для item id = {item_id}.')
#     return {"item_id": item_id, "item": item}

# @app.delete("/items/del/{item_id}")
# async def delete_item(item_id: int):
#     logger.info(f'Отработал DELETE запрос для item id = {item_id}.')
#     return {"item_id": item_id}

