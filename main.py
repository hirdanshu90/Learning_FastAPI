from fastapi import FastAPI, Query, Path, Body, Cookie, Header
from enum import Enum
from typing import Literal
from pydantic import BaseModel, Field,HttpUrl, EmailStr


app = FastAPI()

# Part 13 Response Model /////////////////

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price : float
#     tax : float = 10.5
#     tags : list[str] = []
    
# items = {
    
#     "foo": {"name":"foo", "price": 20.44},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 455, "tax": 20.2},
#     "baz": {"name": "baz", "description": None, "price": 40.33, "tax": 10.5, "tags": ["Just", "testing", "This"]}
    
# }



# @app.post("/items", response_model= Item)
# async def create_item(item:Item):
#     return item



# @app.get("/items/{item_id}", response_model = Item)
# async def read_item(item_id: Literal["foo", "bar","baz"]):
#     return items[item_id]


# Part 14 /////// Extra Models /////////////////

class UserBase(BaseModel):
    username: str
    email : EmailStr
    full_name: str | None = None
    
class UserIn(UserBase):
    password: str
    
class UserOut(UserBase):
    pass

class UserInDB(UserBase):
    hashed_password : str


def fake_password_hasher(raw_password: str):
    return f"supersecret{raw_password}"


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password= hashed_password)
    print("User saved")
    return user_in_db

@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


class BaseItem(BaseModel):
    description: str
    type:str

class CarItem(BaseItem):
    type: "car"
    
class PlaneItem(BaseItem):
    type: "plane"
    size: "int"
    
    
items = {
    "itme1": {"description": "items is in the description", "type":"car"},
    "item2": {
        "description": "Music is my aeroplane",
        "type": "plane",
        "size": 55
    }
}

@app.get("/items/{item_id}", response_model=Union(PlaneItem, CarItem))
async def