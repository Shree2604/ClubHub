from app.db.models import User, ObjectId
from app.db.client import db

# separate third-party imports from local app
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