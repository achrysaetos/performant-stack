# Import the db session to use it.
from sqlalchemy.orm import Session

# Import the user model and schema.
from db.models.user import User
from db.schemas.user import UserCreate


# Function to get a user by id.
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


# Function to get a user by email.
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


# Function to get all users.
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


# Function to create a user.
def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
