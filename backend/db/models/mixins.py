# Import python datetime to keep track of time.
from datetime import datetime

# Import declarative mixin to let other classes inherit from this class.
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declarative_mixin


# Let other classes from all the other models inherit these two fields.
@declarative_mixin
class Timestamp:
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)
