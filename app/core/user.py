from app.db.user import User, insert_user, ObjectId
from app.db.query import find_user, find_memberships, find_club

from pymongo.errors import DuplicateKeyError
from werkzeug.security import check_password_hash

def create_user(
    email: str,
    password1: str, 
    password2: str,
    first_name: str,
    last_name: str
) -> User:
    
    if not all([email, password1, password2, first_name, last_name]):
        raise ValueError("All fields are compulsory")

    if password1 != password2:
        raise ValueError("Passwords do not match")

    if len(password1) < 5:
        raise ValueError("Password must be at least 5 characters")

    if find_user(email=email) is not None:
        raise ValueError("User with this email already exists!")

    email = email.lower().strip() 
    # making the email (entered by the user) in lower cases and removing any whitespaces present in it.

    user = insert_user(
        email=email,
        password=password1,
        first_name=first_name,
        last_name=last_name
    )

    return user

def authenticate_user(
    email : str,
    password: str
) -> User:
    remote_user = find_user(email=email)

    if remote_user is None:
        raise ValueError("User with given email not found")
    else:
        if check_password_hash(remote_user.pw_hash, password):
            return remote_user
        else:
            raise ValueError("Passwords do not match!")

def get_user_clubs(
    user : User
) -> list:
    memberships = find_memberships(user_id=user._id)

    club_list = list()
    for membership in memberships:
        club_list.append(find_club(_id=membership.club_id))

    return club_list