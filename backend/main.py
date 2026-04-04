from fastapi import FastAPI
from app.database.mongodb import connect_to_mongo, close_mongo_connection

app = FastAPI()

@app.on_event("startup")
async def startup():
    await connect_to_mongo()
    print("✅ MongoDB connected")

@app.on_event("shutdown")
async def shutdown():
    await close_mongo_connection()
    print("❌ MongoDB disconnected")