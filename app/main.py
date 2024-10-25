import os

from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routers.router import router
from app.db.session import engine, Base

app = FastAPI()

app.include_router(router)

os.makedirs('resumes', exist_ok=True)

@asynccontextmanager
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)