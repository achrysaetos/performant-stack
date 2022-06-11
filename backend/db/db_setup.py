# Import the tools you need to create your engine and session.
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Connect to your database. Use postgres and psycopg2.
SQLALCHEMY_DATABASE_URL = (
    "postgresql+psycopg2://fastapi-postgres-user@localhost/fastapi-postgres-database"
)


# Create the engine and db session with the params you want.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={}, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)


# The base for all your models.
Base = declarative_base()


# Let other parts of your api access the db session.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
