# Import fastapi for the router.
import fastapi


# Set up the router to use in main.py
router = fastapi.APIRouter()


# Read a section.
@router.get("/sections/{id}")
async def read_section():
    return {"courses": []}
