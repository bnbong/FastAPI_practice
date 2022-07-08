import uvicorn

from typing import Union, Iterable, List
from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel


def toStrings(nums: Iterable[int]) -> List[str]:
    return [str(x) for x in nums]

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get('/users/me')
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}
    

if __name__ == "__main__":
    uvicorn.run(app="main:app",
                host="serverside-testing.bnbongcodeserver.tk",
                port=8000,
                reload=True)