from app.db.models import Club
from app.db.client import db
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

secret_key_Epoch = os.getenv("secret_key_epoch")

def create_club(
    name: str,
    description: str,
    add_roles: list,
    secret_key: str
) -> Club:
    
    if not all([name, description, add_roles, secret_key]):
        raise ValueError("All Fields are compulsory")
    
    if secret_key != secret_key_Epoch:
        raise ValueError("Secret key doesn't Match")
    
    club = Club(
        _id=None,
        name=name,
        description=description,
        created_at=datetime.now(),
        roles=add_roles
    )

    db.ClubCreation.insert_one(club.conv_to_doc())
    return club