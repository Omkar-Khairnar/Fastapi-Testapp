from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel
from api import users, courses, sections

app = FastAPI()

PORT = 8000




@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)


print(f'Application Running on http://localhost:{PORT}')