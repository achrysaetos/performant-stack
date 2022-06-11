# Import python enum to build choices for the Role class.
import enum

# Import types and the ability to link model fields.
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

# Inherit Base and Timestamp for each class.
from ..db_setup import Base
from .mixins import Timestamp


# Create a list of choices for Role types using an enum.
class Role(enum.IntEnum):
    teacher = 1
    student = 2


# Model for each user.
class User(Timestamp, Base):
    __tablename__ = "users"

    # List the fields for each User.
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    role = Column(Enum(Role))
    is_active = Column(Boolean, default=False)

    # Point the relationship to Profile.owner
    profile = relationship("Profile", back_populates="owner", uselist=False)

    # Must always create a two-way relationship between different models.
    student_courses = relationship("StudentCourse", back_populates="student")
    student_content_blocks = relationship("CompletedContentBlock", back_populates="student")


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
