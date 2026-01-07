from app.db.models import Club
from app.db.client import db
from datetime import datetime
from dotenv import load_dotenv
import os

def create_club(
    name: str,
    description: str,
    roles: list,
    secret_key: str
) -> Club:

    load_dotenv()
    secret_club_key = os.getenv("SECRET_KEY")
    
    if not all([name, description, roles, secret_key]):
        raise ValueError("All Fields are compulsory")
    
    if secret_key != secret_club_key:
        raise ValueError("Secret key doesn't Match")
    
    club = Club(
        _id=None,
        name=name,
        description=description,
        created_at=datetime.now(),
        roles=[]
    )

    new_club_id = db.clubs.insert_one(club.conv_to_doc()).inserted_id
    club._id = new_club_id

    return club