import fastapi
from pydantic import BaseModel
from typing import Optional, List


router = fastapi.APIRouter()

class User(BaseModel):
    email:str
    is_active:bool
    bio:Optional[str]

users=[]


@router.get("/users", response_model=List[User])
async def get_users():
    return users

@router.post("/users")
async def create_user(user:User):
    users.append(user)
    return "Success"


@router.get("/users/{id}")
async def get_emailUser(id:int ):
    return users[id]
