import validators 
import re

from pydantic import BaseModel, EmailStr, field_validator
from datetime import datetime
from typing import Optional
from app.db.models import LeadState as LeadStatus


class LeadBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    resume_path: str
    status: LeadStatus

    @field_validator('email')
    def validate_email(cls, value):
        if not validators.email(value):
            raise ValueError('Invalid email address')
        return value
    
    @field_validator('first_name', 'last_name')
    def validate_name(cls, value, field):
        if not re.match("^[a-zA-Z]+$", value):
            raise ValueError(f"{field.name.capitalize()} must contain only alphabetic characters")
        return value


class LeadCreate(LeadBase):
    pass

class LeadResponse(LeadBase):
    resume_path: str
    created_at: datetime
    status: LeadStatus

    class Config:
        from_attributes = True

class LeadUpdate(BaseModel):
    status: LeadStatus