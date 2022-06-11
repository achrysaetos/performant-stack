# Import the FastAPI class from its module.
from fastapi import FastAPI

# Import the api's, models, and engine.
from api import users, courses, sections
from db.db_setup import engine
from db.models import user, course


# Create all tables stored in the metadata for the user and course models.
user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)


# Use FastAPI and personalize the description in its docs.
app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Gwen",
        "email": "gwen@example.com",
    },
    license_info={
        "name": "MIT",
    },
)


# Import each router in order to use the routes from each api.
app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
