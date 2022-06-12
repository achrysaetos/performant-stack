# Import python enum to build choices for the ContentType class.
import enum

# Import types and the ability to link model fields.
from sqlalchemy import Enum, Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType

# Inherit Base and Timestamp for each class.
from ..db_setup import Base
from .user import User
from .mixins import Timestamp


# Create a list of choices for content types using an enum.
class ContentType(enum.Enum):
    lesson = 1
    quiz = 2
    assignment = 3


# Model for each course.
class Course(Timestamp, Base):
    __tablename__ = "courses"

    # List the fields for each Course.
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Link Course to User, Section.course, and StudentCourse.course
    created_by = relationship(User)
    sections = relationship("Section", back_populates="course", uselist=False)
    student_courses = relationship("StudentCourse", back_populates="course")


# Model for each section.
class Section(Timestamp, Base):
    __tablename__ = "sections"

    # List the fields for each Section.
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)

    # Link Section to Course.sections
    course = relationship("Course", back_populates="sections")


# Model to show which courses a student is assigned to.
class StudentCourse(Timestamp, Base):
    __tablename__ = "student_courses"

    # List the fields for each StudentCourse.
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    completed = Column(Boolean, default=False)

    # Link StudentCourse to User.student_courses and Course.student_courses
    student = relationship(User, back_populates="student_courses")
    course = relationship("Course", back_populates="student_courses")
