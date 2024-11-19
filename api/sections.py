import fastapi

router = fastapi.APIRouter()

@router.get("/sections/{id}")
async def read_sectionByID(id:int):
    return {"id":id}

@router.get("/sections/{id}/content-blocks")
async def read_section_content_blocks(id:int):
    return {"id":id}

@router.get("/content-blocks/{id}")
async def read_content_block(id:int):
    return {"id":id}