from fastapi import FastAPI, Query, Path, Body
from enum import Enum
from pydantic import BaseModel, Field,HttpUrl


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

class Item(BaseModel):
    name: str
    description: str | None = None
    price : float
    tax : float | None = None
    
    class Config:
        scheme_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 14.33,
                "tax": 3.44
            }
        }
    
@app.put("/items/{item_id}")
async def update_item(item_id: int, item:Item):
    
