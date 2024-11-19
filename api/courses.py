import fastapi

router = fastapi.APIRouter()

@router.get("/courses")
async def read_courses():
    return {"courses": []}

@router.post("/courses")
async def create_course_api():
    return {"course": []}

@router.get("/courses/{id}")
async def read_course(id:int):
    return {"id":id}

@router.patch("/courses/{id}")
async def update_course(id:int):
    return {"id":id}

@router.delete("/courses/{id}")
async def delete_course(id:int):
    return {"id":id}

@router.get("/courses/{id}/sections")
async def read_course_sections(id:int):
    return {"id":id}
