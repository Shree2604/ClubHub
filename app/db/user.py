from app.db.models import User, ObjectId
from app.db.client import db

# separate third-party imports from local app imports
from werkzeug.security import generate_password_hash

def insert_user(
    email: str,
    password: str, 
    first_name: str,
    last_name: str
) -> User:
    user = User(
        _id=None,
        email=email,
        pw_hash=generate_password_hash(password),
        first_name=first_name,
        last_name=last_name
    )
    
    new_user_id = db.users.insert_one(user.conv_to_doc()).inserted_id
    user._id = new_user_id

    return user

def find_user(
    _id : ObjectId = None, 
    email : str = None,
) -> User | None:
    # Add name based searching later
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