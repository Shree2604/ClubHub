from app.db.models import Club
from app.db.client import db

# separate third-party imports from local app
from datetime import datetime

def create_club(
    name: str,
    description: str
) -> Club:
    
    club = Club(
        _id=None,
        name=name,
        description=description,
        created_at=datetime.now(),
        roles=list() # No Roles directly on club creation, user adds later
    )

    new_club_id = db.clubs.insert_one(club.conv_to_doc()).inserted_id
    club._id = new_club_id

    return club