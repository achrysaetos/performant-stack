# Import the db session to use it.
from sqlalchemy.orm import Session

# Import the course model and schema.
from db.models.course import Course
from db.schemas.course import CourseCreate


# Function to get a course by id.
def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()


# Function to get all courses.
def get_courses(db: Session):
    return db.query(Course).all()


# Function to get a user's courses.
def get_user_courses(db: Session, user_id: int):
    courses = db.query(Course).filter(Course.user_id == user_id).all()
    return courses


# Function to create a course.
def create_course(db: Session, course: CourseCreate):
    db_course = Course(
        title=course.title,
        description=course.description,
        user_id=course.user_id
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
