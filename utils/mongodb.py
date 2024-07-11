from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_DB_URI = os.getenv("MONGO_DB_URI")

client = AsyncIOMotorClient(f"{MONGO_DB_URI}&tlsAllowInvalidCertificates=true")
database = client.pythonApiPlay  # Use your database name
