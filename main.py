from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()



class User(BaseModel):
    email:str
    is_active:bool
    bio:Optional[str]



users=[]


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users", response_model=List[User])
async def get_users():
    return users

@app.post("/users")
async def create_user(user:User):
    users.append(user)
    return "Success"

@app.get("/users/{id}")
async def get_emailUser(id:int = Path()):
    return users[id]
