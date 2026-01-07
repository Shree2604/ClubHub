from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

DB_URI = os.getenv("DB_URI")
if not DB_URI:
    raise RuntimeError("DB_URI not set")

client = MongoClient(
    DB_URI,
    server_api=ServerApi("1"),
    serverSelectionTimeoutMS=5000
)

client.admin.command("ping") 
# Standard health check used to verify that the connection to the MongoDB database is actually working

db = client["maindb"]
db.users.create_index("email", unique=True) 
# This command is used to build the index on the "email" field.