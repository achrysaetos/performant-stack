# Import fastapi for the router.
import fastapi


# Set up the router to use in main.py
router = fastapi.APIRouter()


# Read a section.
@router.get("/sections/{id}")
async def read_section():
    return {"courses": []}


# Read a section's content blocks.
@router.get("/sections/{id}/content-blocks")
async def read_section_content_blocks():
    return {"courses": []}


# Read a content block.
@router.get("/content-blocks/{id}")
async def read_content_block():
    return {"courses": []}
