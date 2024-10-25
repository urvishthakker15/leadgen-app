import enum

from sqlalchemy import Column, String, Enum, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()

class LeadState(str, enum.Enum):
    PENDING = "PENDING"
    REACHED_OUT = "REACHED_OUT"

class Lead(Base):
    __tablename__ = "leads"
    
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, primary_key=True, index=True)
    resume_path = Column(String, nullable=False)
    status = Column(Enum(LeadState), default=LeadState.PENDING)
    created_at = Column(DateTime, default=datetime.now)