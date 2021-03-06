# Import types and the ability to link model fields.
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

# Inherit Base and Timestamp for each class.
from ..db_setup import Base
from .mixins import Timestamp


# Model for each user.
class User(Timestamp, Base):
    __tablename__ = "users"

    # List the fields for each User.
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=False)

    # Point the relationship to Profile.owner and StudentCourse.student
    profile = relationship("Profile", back_populates="owner", uselist=False)
    student_courses = relationship("StudentCourse", back_populates="student")


# Model for each profile.
class Profile(Timestamp, Base):
    __tablename__ = "profiles"

    # List the fields for each Profile.
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    bio = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Point the relationship to User.profile
    owner = relationship("User", back_populates="profile")
