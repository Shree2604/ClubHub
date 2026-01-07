from app.db.models import User, ObjectId
from app.db.client import db
from pymongo.cursor import Cursor

def find_user(
    _id: ObjectId = None, 
    email : str = None,
) -> User | None:
    if _id is not None:
        query_filter = {"_id" : _id}
    elif email is not None:
        query_filter = {"email" : email}
    else:
        raise ValueError("Atleast one query must be specified for search")
    
    user_doc = db.users.find_one(filter=query_filter)
    
    if user_doc is None:
        return None
    else:
        return User.conv_to_obj(user_doc)