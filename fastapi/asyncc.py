from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import asyncio

app = FastAPI()

DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

@app.get("/")
async def index():
    async with AsyncSessionLocal() as session:
        TorF = bool(AsyncSessionLocal())
        await asyncio.sleep(6)  
        return {"message": "its working..", "db" : str(TorF)}
    


