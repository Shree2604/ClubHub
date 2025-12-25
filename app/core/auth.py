from app.db.models import User
from app.db.auth import *

from pymongo.errors import DuplicateKeyError
from werkzeug.security import generate_password_hash, check_password_hash

def register_user( # INCOMPLETE FUNCTION
    email: str,
    password1: str, 
    password2: str,
    first_name: str,
    last_name: str
) -> User | None:

    if(password1 != password2):
        raise ValueError("Passwords do not match!")
    
    email = email.lower().strip()

    user = User(
        _id=None,
        email=email,
        password_hash=generate_password_hash(password1),
        first_name=first_name,
        last_name=last_name
    )