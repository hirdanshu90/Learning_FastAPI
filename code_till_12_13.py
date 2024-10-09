from fastapi import FastAPI, Query, Path, Body, Cookie, Header
from enum import Enum
from pydantic import BaseModel, Field,HttpUrl, EmailStr


app = FastAPI()

# ///////////////////////////  Body - Multiple Parameters /////////////////////////////  V7

# class Item(BaseModel):
#     name: str
#     description: str |None = Field(None, title="Using Field here", max_length=150)
#     price: float
#     tax: float |None = Field(..., gt= 2,description="The tax has to > than 2")
    

# class User(BaseModel):
#     username: str
#     fullname: str | None = None
    
# @app.put("/items/{item_id}")
# async def update_item(*, item_id: int = Path(..., title="The ID of the item to get", ge=2, le=140), 
#                       q: str| None = None,
#                       item: Item| None = None, 
#                       user: User| None = None,
#                       Using_body: dict = Body(..., embed=True)
#                       ):
#     results = {"items_id": item_id}
#     if q:
#         results.update({"q":q})
#     if item:
#         results.update({"item":item})
#     if user:
#         results.update({"user":user})
#     if Using_body:
#         results.update({"Using_body":Using_body})
#     return results

# ////////////////////////////////  V9  //////////////////////////////////////////////

# class Image(BaseModel):
#     url: HttpUrl
#     name:str

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price : float
#     tax : float | None = None
#     tags: list[str] = Field(default_factory=list)  # Fix for mutable default value
#     image: list[Image] | None = None
    
# class Offer(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     items : list[Item]
    
    
# @app.put("/items/{item_id}")
# async def update_item( item: Item, item_id: int = Path(..., ge=21, le= 100)):
#     results = {"item_id": item_id, "Item": item}
#     return results


# @app.post("/offers")
# async def create_offer(offer: Offer = Body(..., embed=True)):
#     return offer

# @app.post("/images/multiple")
# async def create_multiple_offer(images: list[Image] = Body(..., embed=True)):
#     return images

# @app.post("/blah")
# async def create_some_dict(blahs: dict[int, float]):
#     return blahs


# ///////////////////////////////// Declare Request Example Data ///// V10 ///////

# class Item(BaseModel):
#     name: str = Field(..., example=("Foo"))
#     description: str | None = None
#     price : float = Field(..., example= 32.54)
#     tax : float | None = Field(None, example = 23.44)
    
#     class Config:
#         scheme_extra = {
#             "example": {
#                 "name": "Foo",
#                 "description": "A very nice Item",
#                 "price": 14.33,
#                 "tax": 3.44
#             }
#         }
    
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item:Item = Body(..., description = "Type in the items")):
#     results = {"item_id": item_id, "item": item}
#     return results     


# ///////  ........ Cookie and Header Parameter ...... ///////////////

# @app.get("/items")
# async def read_items(
#     cookie_id: str | None = Cookie(None),
#     accept_encoding: str | None = Header(None),
#     Host: str | None = Header(None),
#     user_agent : str | None = Header(None)
#     ):
#     return {"cookie_id": cookie_id, "Accept_encoding": accept_encoding, "Host": Host, "user_agent": user_agent}

# ////////////////// Response Model ////////////////////////////////////

# Base model with shared fields
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

# Input model for user creation (includes password)
class Userin(UserBase):
    password: str

# Output model for user data (excludes password)
class UserOut(UserBase):
    pass

# Model for user profile view
class UserProfile(UserBase):
    bio: str | None = None
    interests: list[str] = []

# Model for admin users (extends base fields and adds role)
class AdminUser(UserBase):
    role: str = "admin"  # Specific role for admins
    permissions: list[str] = ["read", "write", "delete"]

@app.post("/user/", response_model=UserOut)
async def create_user(user: Userin):
    # Simulate saving user to the database
    return user  # Password is excluded in the response

@app.get("/user/profile/{username}", response_model=UserProfile)
async def get_user_profile(username: str):
    # Simulate retrieving user profile from the database
    return {
        "username": username,
        "email": f"{username}@example.com",
        "full_name": "John Doe",
        "bio": "I am a software developer",
        "interests": ["coding", "reading"]
    }

@app.get("/admin/{username}", response_model=AdminUser)
async def get_admin_user(username: str):
    # Simulate retrieving admin user data from the database
    return {
        "username": username,
        "email": f"{username}@admin.com",
        "full_name": "Admin User",
        "role": "admin",
        "permissions": ["read", "write", "delete"]
    }
