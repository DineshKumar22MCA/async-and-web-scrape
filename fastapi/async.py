from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/")
async def index():
    await asyncio.sleep(5)
    return {"message": "Hello, FastAPI!"}
