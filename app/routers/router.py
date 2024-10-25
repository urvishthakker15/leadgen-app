import uuid
import os

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, Header
from fastapi.responses import FileResponse
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update
from datetime import datetime

from app.schemas.schemas import LeadCreate, LeadResponse, LeadUpdate
from app.db.models import Lead, LeadState
from app.db.session import get_db
from app.services.services import send_emails_to_prospect_and_attorney

router = APIRouter()

import os


async def get_api_key(x_api_key: str = Header(...)):
    expected_api_key = os.getenv("API_KEY")
    if x_api_key != expected_api_key:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return x_api_key

@router.post("/lead", response_model=LeadCreate, dependencies=[Depends(get_api_key)])
async def create_lead(
    first_name: str = Form(...),
    last_name: str = Form(...),
    email: str = Form(...),
    resume: UploadFile = File(...),
    db: AsyncSession = Depends(get_db)
):
    resume_filename = f"{uuid.uuid4()}_{resume.filename}"
    resume_path = os.path.join('resumes', resume_filename)

    with open(resume_path, "wb") as buffer:
        buffer.write(await resume.read())

    new_lead = Lead(
        first_name=first_name,
        last_name=last_name,
        email=email,
        resume_path=resume_filename,
        status=LeadState.PENDING,
        created_at=datetime.now()
    )

    db.add(new_lead)
    await db.commit()
    await db.refresh(new_lead)

    await send_emails_to_prospect_and_attorney(new_lead)

    return new_lead



@router.get("/leads", response_model=List[LeadResponse], dependencies=[Depends(get_api_key)])
async def get_leads(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Lead))
    leads = result.scalars().all()
    return leads


@router.put("/leads/{email_id}", response_model=LeadResponse)
async def update_lead(email_id: str, lead_update: LeadUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Lead).filter(Lead.email == email_id))
    lead = result.scalars().first()

    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    lead.status = lead_update.status
    await db.commit()
    await db.refresh(lead)
    return lead


   
