# Import python type List.
from typing import List

# Import fastapi and a local session.
import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

# Import schemas to create and read users as well as util functions to decide what to do.
from db.db_setup import get_db
from db.schemas.user import UserCreate, User
from db.schemas.course import Course
from api.utils.users import get_user, get_user_by_email, get_users, create_user
from api.utils.courses import get_user_courses


# Set up the router to use in main.py
router = fastapi.APIRouter()


# Read all users.
@router.get("/users", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


# Create a user.
@router.post("/users", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email is already registered")
    return create_user(db=db, user=user)


# Read a user.
@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# Read a user's courses.
@router.get("/users/{user_id}/courses", response_model=List[Course])
async def read_user_courses(user_id: int, db: Session = Depends(get_db)):
    courses = get_user_courses(user_id=user_id, db=db)
    return courses
