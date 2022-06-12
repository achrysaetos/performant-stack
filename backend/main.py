# Import the FastAPI class from its module.
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import the api's, models, and engine.
from api import users, courses, sections
from db.db_setup import engine
from db.models import user, course


# Create all tables stored in the metadata for the user and course models.
user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)


# Use FastAPI and personalize the description in its docs.
app = FastAPI(
    title="FastAPI Docs",
    description="...",
    version="0.0.1",
    contact={
        "name": "Us",
        "email": "us@example.com",
    },
    license_info={
        "name": "MIT",
    },
)


# Deal with CORS easy.
origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Import each router in order to use the routes from each api.
app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
