# Import python type List.
from typing import List

# Import fastapi and a local session.
import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

# Import schemas to create and read courses as well as util functions to decide what to do.
from db.db_setup import get_db
from db.schemas.course import Course, CourseCreate
from api.utils.courses import get_course, get_courses, create_course


# Set up the router to use in main.py
router = fastapi.APIRouter()


# Create a course.
@router.post("/courses", response_model=Course)
async def create_new_course(course: CourseCreate, db: Session = Depends(get_db)):
    return create_course(db=db, course=course)


# Read a course.
@router.get("/courses/{course_id}")
async def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = get_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course


# # Update a course.
# @router.patch("/courses/{course_id}")
# async def update_course():
#     return


# Delete a course.
@router.delete("/courses/{course_id}")
async def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = get_course(db=db, course_id=course_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    db.delete(db_course)
    db.commit()
    return {"ok": True}


# Read all courses.
@router.get("/courses", response_model=List[Course])
async def read_courses(db: Session = Depends(get_db)):
    courses = get_courses(db=db)
    return courses


# Read a course's sections.
@router.get("/courses/{course_id}/sections")
async def read_course_sections():
    return {"courses": []}
