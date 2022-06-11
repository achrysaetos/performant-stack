# Let some fields be optional.
from typing import Optional

# Let other classes extend from any class that themselves extend from the BaseModel.
from pydantic import BaseModel


# Shared fields from creating/reading the course.
class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    user_id: int


# Pydantic model (schema) to create the course.
class CourseCreate(CourseBase):
    ...


# Pydantic model (schema) to read the course.
class Course(CourseBase):
    id: int

    # Child class that's neccessary if you're using an orm.
    class Config:
        orm_mode = True
