# Import python datetime to fill out the relevant fields when the user is created.
from datetime import datetime

# Let other classes extend from any class that themselves extend from the BaseModel.
from pydantic import BaseModel


# Shared fields from creating/reading the user.
class UserBase(BaseModel):
    email: str
    role: int


# Pydantic model (schema) to create the user.
class UserCreate(UserBase):
    ...


# Pydantic model (schema) to read the user.
class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    # Child class that's neccessary if you're using an orm.
    class Config:
        orm_mode = True
