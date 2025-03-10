from motor.motor_asyncio import AsyncIOMotorClient
from config import database_url
from pymongo.errors import PyMongoError

try:
    client = AsyncIOMotorClient(database_url)
    db = client.get_database()
    print("Database connected successfully")
except PyMongoError as e:
    print("Failed to connect to MongoDB")
