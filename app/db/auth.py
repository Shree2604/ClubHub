from app.db.client import db
from app.db.models import User

from bson.objectid import ObjectId

def insert_user(user : User):
    doc = user.conv_to_doc()
    result = db.users.insert_one(doc)
    return result.inserted_id