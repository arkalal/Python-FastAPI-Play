from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_DB_URI = os.getenv("MONGO_DB_URI")
client = AsyncIOMotorClient(MONGO_DB_URI)
database = client.pythonApiPlay
