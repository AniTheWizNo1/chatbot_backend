from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI")
print(f"🔧 Connecting to MongoDB: {MONGO_URI}")  # TEMP DEBUG

client = MongoClient(MONGO_URI)
db = client["chatbot_db"]
